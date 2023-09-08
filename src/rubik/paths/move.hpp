#ifndef TESTING_MOVE_HPP
#define TESTING_MOVE_HPP

#include <iostream>
#include <string>
#include <vector>
#include <functional>
#include <boost/functional/hash.hpp>
#include "logging/logging.hpp"

class Move {
private:
    std::string description;

public:
    std::vector<size_t> indices;

    Move() {};

    Move(std::string description, std::vector<size_t> forward_indices) :
            description(description), indices(forward_indices) {}

    friend std::ostream &operator<<(std::ostream &os, const Move &move) {
        os << move.description;
        return os;
    }

    bool operator==(const Move &other) const = default;

    friend std::hash<Move>;
};

template<>
struct std::hash<Move> {
    std::size_t operator()(const Move &move) const noexcept {
        size_t combined_hash = 0; /* <- Must be seeded. */
        boost::hash_combine(combined_hash, move.description);
        boost::hash_combine(combined_hash, boost::hash_range(move.indices.begin(), move.indices.end()));
        return combined_hash;
    }
};


#endif //TESTING_MOVE_HPP
