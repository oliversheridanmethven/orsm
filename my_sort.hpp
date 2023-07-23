//
// Created by Oliver Sheridan-Methven on 17/11/2020.
//

#include <condition_variable>
#include <mutex>
#include <stack>
#include <stdexcept>
#include <thread>
#include <utility>
#include <vector>

#ifndef MISC_MY_SORT_HPP
#define MISC_MY_SORT_HPP

// We will compare two implementations of quick sort.

template<typename T>
typename T::iterator quick_sort_partition(const typename T::iterator start, const typename T::iterator end)
{
    typename T::iterator pivot_value_ptr{end - 1};
    typename T::iterator left_insertion_position{start};
    for (typename T::iterator position{start}; position < pivot_value_ptr; position++)
    {
        if (*position <= *pivot_value_ptr)
        {
            std::swap(*left_insertion_position, *position);
            left_insertion_position++;
        }
    }
    std::swap(*left_insertion_position, *pivot_value_ptr);
    return left_insertion_position;
};

template<typename T>
void quick_sort(typename T::iterator start, typename T::iterator end)
{
    if (end - start > 1)
    {
        typename T::iterator partition = quick_sort_partition<T>(start, end);
        quick_sort<T>(start, partition);
        quick_sort<T>(partition, end);
    }
}

template<typename T>
void scalar_sort(typename T::iterator start, typename T::iterator end)
{
    quick_sort<T>(start, end);
}



typedef double T;
typedef std::vector<T> container;
typedef container::iterator iterator;
typedef std::pair<iterator, iterator> sort_job;

void parallel_sort(iterator start, iterator end);

#endif//MISC_MY_SORT_HPP
