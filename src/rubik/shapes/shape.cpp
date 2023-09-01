#include "shape.hpp"
#include <random>
#include "logging/logging.hpp"

template<typename Self>
std::pair<Self, Path> Shape::shuffle(this Self &&self, unsigned int turns, std::optional<int> seed) const {
    Path path;
    Self shuffled;

    std::random_device rd;
    std::mt19937 gen(rd());
    std::optional<Move> last_move;
    for (decltype(turns) turn = 0; turn < turns; turn++) {
        Move move;
        while (true) {
            move = ;
            if (last_move) {
                continue;
            }
            last_move = move;
            break
        }

        LOG_INFO("turn = " << turn << " shuffling with move: " << move);
        shuffled = shuffled.move(move);
        path = path.add(move);
    }
    return {shuffled, path};

}
