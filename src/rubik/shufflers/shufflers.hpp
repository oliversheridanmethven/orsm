#ifndef TESTING_SHUFFLERS_HPP
#define TESTING_SHUFFLERS_HPP

#include "rubik/shapes/shape.hpp"
#include "rubik/paths/path.hpp"
#include <variant>

auto specific(auto start, std::variant<int, std::string> turns, std::optional<int> seed) {
    Path path;
    using ShapesAndPaths = std::unordered_map<decltype(start), Path>;
    ShapesAndPaths shapes_and_paths_new = {{start, Path{}}};
    ShapesAndPaths shapes_and_paths_encountered;

    auto is_god = [](auto turns) {
        return std::holds_alternative<std::string>(turns) and std::get<std::string>(turns) == "god";
    };

    for (int generation = 0; is_god(turns) or generation < std::get<int>(turns); generation++) {
        LOG_DEBUG << "Generation = " << generation << ", we have encountered " << shapes_and_paths_encountered.size()
                  << " shapes previously";
        shapes_and_paths_encountered.merge(shapes_and_paths_new);
        auto shapes_and_paths_new_previous = shapes_and_paths_new;
        auto shapes_and_paths_next_gen = next_generation_of_shapes_with_paths(shapes_and_paths_new);
        shapes_and_paths_new.clear();
        for (const auto &[shape, path]: shapes_and_paths_next_gen) {
            if (not shapes_and_paths_encountered.contains(shape)) {
                shapes_and_paths_new.insert({shape, path});
            }
        }

        if (shapes_and_paths_new.empty()) {
            if (is_god(turns)) {
                LOG_DEBUG << "We have found a god shuffle after {generation = }";
                shapes_and_paths_new = shapes_and_paths_new_previous;
                break;
            }
            LOG_ERROR
                    << "The requested difficulty is too hard, and we could not generate any new paths after generation "
                    << generation << " when requesting " << std::get<int>(turns) << " turns.";
        }
    }

    LOG_INFO << "We were able to find " << shapes_and_paths_new.size() << " matching the specific difficulty (turns = "
             << ").";
    auto [shuffled, shuffle_path] = shapes_and_paths_new.front();
    return std::tuple{shuffled, shuffle_path};
}

auto god(auto start, std::optional<int> seed) {
    return specific(start, "god", seed);
}


#endif //TESTING_SHUFFLERS_HPP
