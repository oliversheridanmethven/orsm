#ifndef TESTING_MEET_IN_MIDDLE_RECURSIVE_HPP
#define TESTING_MEET_IN_MIDDLE_RECURSIVE_HPP

#include "rubik/solvers/solver.hpp"
#include "logging/logging.hpp"
#include <algorithm>
#include <execution>

template<typename Shape>
class MeetInMiddleRecursive final : Solver<Shape> {
    using ShapeFront = std::unordered_set<Shape>;
    using Distance = std::optional<int>;

private:

    static auto next_generation_of_shapes_without_paths(const ShapeFront &shapes) {
        CHECK(not shapes.empty());
        ShapeFront shapes_next;
        /* ^ It might be useful to reserve some space for this... */
        auto moves = shapes.begin()->moves();
        for (const auto &shape: shapes) {
            for (const auto &move: moves) {
                auto moved = shape.move(move);
                shapes_next.insert(moved);
            }
        }
        CHECK(not shapes_next.empty());
        return shapes_next;
    }

    static auto intermediate_shape_and_turns(const Shape &start, const Shape &target) {
        size_t turns = 0;
        ShapeFront shape_front_1 = {target};
        ShapeFront shape_front_2 = {start};
        std::array<ShapeFront, 2> shape_fronts = {shape_front_1,
                                                  shape_front_2};

        ShapeFront overlaps;
        while (true) {
            const auto [smaller_front, larger_front] = std::ranges::minmax(shape_fronts,
                                                                           [](const auto &first, const auto &second) {
                                                                               return first.size() < second.size();
                                                                           });

            CHECK_LE(smaller_front.size(), larger_front.size()) << "The sizing of our fronts is mis-matched.";

            std::for_each(/*std::execution::par,*/ smaller_front.begin(), smaller_front.end(),
                                                   [&](const auto &shape) {
                                                       if (larger_front.contains(shape)) {
                                                           overlaps.insert(shape);
                                                       }
                                                   });
            if (not overlaps.empty()) {
                LOG_DEBUG << "We have found " << overlaps.size() << " solutions with turns = " << turns;
                break;
            }
            std::reverse(shape_fronts.begin(), shape_fronts.end());
            shape_fronts.at(0) = next_generation_of_shapes_without_paths(shape_fronts.at(0));
            turns += 1;
        }

        auto turns_from_start = (turns + 1) / 2;
        auto turns_from_target = turns / 2;
        CHECK_GE(turns_from_start, turns_from_target) <<
                                                      "We expect equal or more turns from the starting shape than from the target.";
        for (auto turn_amount: {turns_from_start, turns_from_target}) {
            CHECK_GE(turn_amount, 0) << "The turn amount must be positive.";
        }
        CHECK_EQ(turns_from_start + turns_from_target, turns)
            << "We have not correctly split the turns = " << turns << " turns_from_start = "
            << turns_from_start << " turns_from_target = " << turns_from_target;
        auto overlap = *overlaps.begin();
        LOG_DEBUG << "The item that overlaps from both sets is: " << overlap;
        return std::make_tuple(overlap, turns_from_start, turns_from_target);
    }

    static bool distance_not_final(const Distance &distance) {
        return (not distance.has_value()) or distance.value() > 1;
    }

public:
    virtual Path solve(const Shape &start, const Shape &target) const override final {
        std::vector<Shape> shapes = {start, target};
        std::vector<Distance> distances = {std::nullopt};

        while (std::any_of(distances.begin(), distances.end(), &distance_not_final)) {
            size_t index_start = -1;
            for (size_t i = 0; i < distances.size(); i++) {
                if (distance_not_final(distances.at(i))) {
                    index_start = i;
                    break;
                }
            }
            CHECK_GE(index_start, 0) << "We have not correctly set the starting index.";
            auto index_intermediate = index_start + 1;
            auto [intermediate_shape, distance_start, distance_target] = intermediate_shape_and_turns(
                    shapes.at(index_start), shapes.at(index_intermediate));
            distances.at(index_start) = distance_start;
            distances.insert(distances.begin() + index_intermediate, distance_target);
            shapes.insert(shapes.begin() + index_intermediate, intermediate_shape);
        }


        CHECK(not distances.empty()) << "We expect there to be some distances.";
        for (auto distance: distances) {
            CHECK(distance == 1 or distance == 0) << "All the distances must be one or less.";
        }
        CHECK_GT(shapes.size(), 2) << "We are expecting some intermediate shapes.";
        CHECK_EQ(shapes.size(), distances.size() + 1) << "The number of shapes and distances don't match.";

        /*
         * Now we clean up the distances and shapes, removing zero distance steps.
         * We remove redundant entries from the target towards the start, hence we
         * reverse the containers to "right/end-align" the indices.
         *
         * */
        std::reverse(shapes.begin(), shapes.end());
        std::reverse(distances.begin(), distances.end());
        decltype(shapes) cleaned_shapes;
        decltype(distances) cleaned_distances;
        for (size_t i = 0; i < distances.size(); i++) {
            if (distances.at(i).value()) {
                cleaned_shapes.push_back(shapes.at(i));
                cleaned_distances.push_back(distances.at(i));
            }
        }
        cleaned_shapes.push_back(shapes.back());
        shapes = cleaned_shapes;
        distances = cleaned_distances;
        std::reverse(shapes.begin(), shapes.end());
        std::reverse(distances.begin(), distances.end());

        if (not distances.empty()) {
            for (auto distance: distances) {
                CHECK_EQ(distance.value(), 1) << "All the distances must be one.";
            }
        }
        CHECK(not shapes.empty()) << "We are expecting some shapes.";
        CHECK_EQ(shapes.size(), std::unordered_set(shapes.begin(), shapes.end()).size())
            << "All our intermediate shapes must be unique.";
        CHECK_EQ(shapes.size(), distances.size() + 1) << "There is a mismatch between our shapes and our distances.";

        /*
         * Now we reconstruct the path.
         *
         * */
        Path path;
        for (size_t i = 0; i < shapes.size() - 1; i++) {
            Shape shape = shapes.at(i);
            Shape next_shape = shapes.at(i + 1);

            bool found_match = false;
            for (auto move: shape.moves()) {
                auto moved = shape.move(move);
                if ((found_match = (moved == next_shape))) {
                    bool reverse = false;

                    path = path.add(move, reverse);
                    break;
                }
            }
            CHECK(found_match) << "We should have found the next_shape = " << next_shape
                               << " when searching through the moves generated from shape: " << shape;
        }
        LOG_DEBUG << "The solution path we found was: " << path;
        return path;
    }
};

#endif //TESTING_MEET_IN_MIDDLE_RECURSIVE_HPP
