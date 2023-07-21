//
// Created by Oliver Sheridan-Methven on 15/11/2020.
//
#include <vector>
#include <stdexcept>
#include <algorithm>
#include <thread>
#include <future>
#include <mutex>

#ifndef MISC_MY_MINIMUM_HPP
#define MISC_MY_MINIMUM_HPP

namespace my_minimum
{
    template<typename T>
    T scalar_minimum(typename std::vector<T>::const_iterator beginning, typename std::vector<T>::const_iterator end)
    {
        if (beginning == end) return std::numeric_limits<T>::max();

        T running_min = std::numeric_limits<T>::max();
        for (typename std::vector<T>::const_iterator iterator{beginning}; iterator < end; iterator++)
        {
            running_min = std::min(*iterator, running_min);
        }
        return running_min;
    }

    template<typename T>
    T parallel_minimum(typename std::vector<T>::const_iterator beginning, typename std::vector<T>::const_iterator end)
    {
        if (beginning == end) return 0;
        unsigned int n_threads = std::thread::hardware_concurrency();
        std::vector<std::thread> threads(n_threads);
        std::vector<std::future<T> > partial_sums(n_threads);
        unsigned long n_items = end - beginning;
        for (unsigned int t = 0; t < n_threads; t++)
        {
            unsigned long step = n_items / n_threads;
            typename std::vector<T>::const_iterator lower = beginning + step * t;
            typename std::vector<T>::const_iterator upper = (t == n_threads - 1) ? end : lower + step;
            // The final thread might need to handle some surplus items.
            partial_sums[t] = std::async(scalar_minimum<T>, lower, upper);
        }

        T running_min = std::numeric_limits<T>::max();
        for (auto &partial_sum: partial_sums)
        {
            running_min = std::min(running_min, partial_sum.get());
        }

        return running_min;
    }
}
#endif //MISC_MY_MINIMUM_HPP
