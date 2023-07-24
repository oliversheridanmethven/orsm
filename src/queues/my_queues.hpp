//
// Created by Oliver Sheridan-Methven on 14/11/2020.
//

#ifndef MISC_MYQUEUES_HPP
#define MISC_MYQUEUES_HPP

#include <algorithm>
#include <mutex>
#include <stdexcept>
#include <thread>

namespace my_queues
{
    template<typename T>
    class Queue
    {
    public:
        virtual T pop() = 0;
        virtual void push(const T data) = 0;
    };

    template<typename T, int MAX_SIZE>
    class LinearQueue : public Queue<T>
    {
    public:
        LinearQueue() : free_position{items}, n_items{0} {}

        T pop()
        {
            std::lock_guard<std::mutex> lock(guard);
            if (not n_items) throw std::logic_error("The queue is empty");
            T data = items[0];
            for (int i = 1; i < n_items; i++)
            {
                items[i - 1] = items[i];
            }
            n_items--;
            return data;
        }

        void push(const T data)
        {
            std::lock_guard<std::mutex> lock(guard);
            if (n_items == MAX_SIZE) throw std::length_error("The queue is full.");
            *free_position++ = data;
            n_items++;
        }

    private:
        T items[MAX_SIZE];
        T *free_position;
        int n_items;
        std::mutex guard;
    };

    template<typename T, int MAX_SIZE>
    class CircularQueue : public Queue<T>
    {
    public:
        CircularQueue() : n_items{0}, start{items}, first{items}, free{items}, end{start + MAX_SIZE}
        {}

        void push(const T data)
        {
            if (n_items == MAX_SIZE) throw std::length_error("The queue is full.");

            *free++ = data;
            n_items++;

            if (free == end) free = start; /* Wrapping the free around to the start. */
        }

        T pop()
        {
            if (not n_items) throw std::length_error("The queue is empty.");

            n_items--;
            return *first++;
        }

    private:
        T items[MAX_SIZE];
        T *const start, *first, *free, *const end;
        int n_items;
    };
}// namespace my_queues

#endif//MISC_MYQUEUES_HPP
