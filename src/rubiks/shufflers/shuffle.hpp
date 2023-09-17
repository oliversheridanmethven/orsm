#ifndef TESTING_SHUFFLE_HPP
#define TESTING_SHUFFLE_HPP

#include "rubiks/moves/move.hpp"
#include "rubiks/paths/path.hpp"
#include "rubiks/shufflers/seed.hpp"
#include <random>
#include <type_traits>

namespace rubiks
{
    namespace shufflers
    {
        using namespace rubiks::paths;
        using namespace rubiks::moves;

        template<typename Self>
        std::pair<Self, Path> shuffle(const Self &shape, const unsigned int turns, const Seed &seed)
        {
            Path path;
            Self shuffled;

            std::random_device rd;
            std::mt19937 gen(rd());
            gen.seed(
                    seed.has_value() ? seed.value()
                                     : std::chrono::high_resolution_clock::now().time_since_epoch().count());
            std::optional<Move> last_move;
            for (std::decay_t<decltype(turns)> turn = 0; turn < turns; turn++)
            {
                Move move;
                while (true)
                {
                    auto possible_moves = shape.moves();
                    std::sample(possible_moves.begin(), possible_moves.end(), &move, 1, gen);
                    if (last_move and shape.commutative(move, last_move.value()))
                    {
                        continue;
                    }
                    last_move = move;
                    break;
                }

                LOG_TRACE << "turn = " << turn << " shuffling with move: " << move;
                shuffled = shuffled.move(move);
                LOG_DEBUG << "The shuffled shape is: " << shuffled;
                path = path.add(move);
                LOG_DEBUG << "The current path is: " << path;
            }
            return {shuffled, path};
        }
    }// namespace shufflers
}// namespace rubiks

#endif//TESTING_SHUFFLE_HPP
