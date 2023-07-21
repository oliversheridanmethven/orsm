//
// Created by Oliver Sheridan-Methven on 17/11/2020.
//

#include <vector>
#include <iostream>
#include <utility>
#include <stdexcept>
#include <stack>
#include <thread>
#include <mutex>
#include <chrono>
#include <condition_variable>
#include "my_sort.hpp"

typedef double T;
typedef std::vector<T> container;
typedef container::iterator iterator;
typedef std::pair<iterator, iterator> sort_job;

class sorting_stack
{  // A thread safe sorting stack;
public:

    sorting_stack() : n_threads_working_on_stack{0}
    {}

    bool might_have_work_to_do() const
    {
        std::lock_guard lock(stack_mutex);
        return (not stack.empty()) or (n_threads_working_on_stack > 0);
    }

    void announce_finished_work()
    {
        {
            std::lock_guard lock(stack_mutex);
            n_threads_working_on_stack--;
        }
        // We release the lock before making the notification.
        stack_condition.notify_all();
    }

    bool try_pop(sort_job &pair)
    {
        {
            std::lock_guard lock(stack_mutex);
            if (stack.empty())
            {
                return false;
            }
            pair = stack.top();
            stack.pop();
            n_threads_working_on_stack++;
            max_concurrent_threads = std::max(n_threads_working_on_stack, max_concurrent_threads);
        }
        stack_condition.notify_all();
        return true;
    }

    void push(sort_job job)
    {
        {
            std::lock_guard lock(stack_mutex);
            stack.push(job);
        }
        stack_condition.notify_all();
    }

private:
    int n_threads_working_on_stack;
    mutable std::mutex stack_mutex;
    std::condition_variable stack_condition;
    std::stack<sort_job> stack;
    int max_concurrent_threads = 0;
};

void work_on_stack(sorting_stack &sort_stack);

void parallel_sort(iterator start, iterator end)
{

    unsigned long n_items = end - start;
    if (n_items <= 1)  // Nothing to be done.
    {
        return;
    }

    unsigned int n_threads = std::thread::hardware_concurrency();
    std::vector<std::thread> threads(n_threads);

    sorting_stack sort_stack;
    sort_stack.push(sort_job(start, end)); // We get the stack started.
    for (auto &thread: threads) // Launch the threads at the stack.
    {
        thread = std::thread(work_on_stack, std::ref(sort_stack));
    }

    for (auto &thread: threads)  // Tidy up the threads.
    {
        thread.join();
    }
}

void work_on_stack(sorting_stack &sort_stack)
{

    while (sort_stack.might_have_work_to_do()) // Race condition here?
    {

        sort_job work_iterators;
        bool is_work = sort_stack.try_pop(work_iterators);  // Might be able to do this using a condition variable.
        if (not is_work)
        {
            continue;
        }

        // Doing work.
        iterator start, end, partition;
        start = work_iterators.first;
        end = work_iterators.second;
        partition = quick_sort_partition<container>(start, end);
        if (partition - start > 1)
        {
            sort_stack.push(sort_job(start, partition));
        }
        if (end - partition > 1)
        {
            sort_stack.push(sort_job(partition, end));
        }
        sort_stack.announce_finished_work();
    }
}


