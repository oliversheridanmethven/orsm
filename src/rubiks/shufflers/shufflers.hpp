#ifndef TESTING_SHUFFLERS_HPP
#define TESTING_SHUFFLERS_HPP

#include "logging/logging.hpp"
#include "rubiks/paths/path.hpp"
#include "rubiks/shapes/shape.hpp"
#include "rubiks/shufflers/seed.hpp"
#include <variant>

namespace rubiks
{
    namespace shufflers
    {
        using namespace rubiks::paths;

        auto next_generation_of_shapes_with_paths(auto shapes_and_paths)
        {

            decltype(shapes_and_paths) shapes_and_paths_next;
            CHECK(not shapes_and_paths.empty());
            for (const auto &[shape, path]: shapes_and_paths)
            {
                for (const auto &move: shape.moves())
                {
                    shapes_and_paths_next.insert({shape.move(move), path.add(move)});
                }
            }
            /* Limited compiler support currently for parallel algorithm execution policies sadly... */
            CHECK(not shapes_and_paths_next.empty());
            return shapes_and_paths_next;
        }

        auto specific(auto start, std::variant<int, std::string> turns, const Seed &seed = std::nullopt)
        {
            Path path;
            using ShapesAndPaths = std::unordered_map<decltype(start), Path>;
            ShapesAndPaths shapes_and_paths_new = {{start, Path{}}};
            ShapesAndPaths shapes_and_paths_encountered;

            auto is_god = [](auto turns) {
                return std::holds_alternative<std::string>(turns) and std::get<std::string>(turns) == "god";
            };

            for (int generation = 0; is_god(turns) or generation < std::get<int>(turns); generation++)
            {
                LOG_DEBUG << "Generation = " << generation << ", we have encountered " << shapes_and_paths_encountered.size()
                          << " shapes previously";
                shapes_and_paths_encountered.merge(ShapesAndPaths(shapes_and_paths_new));
                /* ^ .merge() is destructive, so we pass a new object. */
                auto shapes_and_paths_new_previous = shapes_and_paths_new;
                auto shapes_and_paths_next_gen = next_generation_of_shapes_with_paths(shapes_and_paths_new);
                shapes_and_paths_new.clear();
                for (const auto &[shape, path]: shapes_and_paths_next_gen)
                {
                    if (not shapes_and_paths_encountered.contains(shape))
                    {
                        shapes_and_paths_new.insert({shape, path});
                    }
                }

                if (shapes_and_paths_new.empty())
                {
                    if (is_god(turns))
                    {
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
                     << (is_god(turns) ? std::get<std::string>(turns) : std::to_string(std::get<int>(turns))) << ").";
            auto [shuffled, shuffle_path] = *shapes_and_paths_new.begin();
            return std::tuple{shuffled, shuffle_path};
        }

        auto god(auto start, const Seed &seed)
        {
            return specific(start, "god", seed);
        }
    }// namespace shufflers
}// namespace rubiks

#endif//TESTING_SHUFFLERS_HPP
