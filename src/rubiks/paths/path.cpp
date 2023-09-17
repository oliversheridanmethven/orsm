#include "rubiks/paths/path.hpp"
#include <algorithm>

namespace rubiks
{
    namespace paths
    {

        Path Path::add(const Move &move, const bool reverse) const
        {
            Path result = *this;
            result.push_back({move, reverse});
            return result;
        }

        Path Path::reversed(void) const
        {
            Path result = *this;
            std::ranges::reverse(result);
            for (auto &[move, reverse]: result)
            {
                reverse = not reverse;
            }
            return result;
        }

        std::ostream &operator<<(std::ostream &os, const Path &path)
        {
            if (path.empty())
            {
                os << "Empty path.\n";
                return os;
            }

            for (size_t turn = 0; auto [move, reverse]: path)
            {
                os << "\nTurn = " << turn++ << " " << move << (reverse ? " in reverse" : "");
            }
            os << "\n";
            return os;
        }

    }// namespace paths
}// namespace rubiks
