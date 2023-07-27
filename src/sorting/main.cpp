#include <algorithm>
#include <chrono>
#include <iostream>
#include <map>
#include <random>
#include <stdexcept>
#include <vector>

#include "../minimum/my_minimum.hpp"
#include "../queues/my_queues.hpp"
#include "../stacks/my_stacks.hpp"
#include "my_sort.hpp"

int main()
{
    //    constexpr unsigned int stack_size = 3;
    //    constexpr unsigned int queue_size = stack_size;
    //    typedef double data_type;
    //
    //    my_stacks::Stack_1<data_type, stack_size> stack_1;
    //    my_stacks::Stack_2<data_type, stack_size> stack_2;
    //    my_stacks::Stack_3<data_type, stack_size> stack_3;
    //    std::vector<my_stacks::Stack<data_type> *> stacks = {&stack_1, &stack_2, &stack_3};
    //
    //    my_queues::LinearQueue<data_type, queue_size> linear_queue;
    //    my_queues::CircularQueue<data_type, queue_size> circular_queue;
    //    std::vector<my_queues::Queue<data_type> *> queues = {&linear_queue, &circular_queue};
    //
    //    for (auto &queue_ptr: queues)
    //    {
    //        try
    //        {
    //            for (unsigned int i = 1; i <= 100; i++)
    //            {
    //                queue_ptr->push(i);
    //            }
    //        }
    //        catch (std::length_error &e)
    //        {
    //            std::cout << e.what() << std::endl;
    //        }
    //
    //        try
    //        {
    //            for (unsigned int i = 1; i <= 100; i++)
    //            {
    //                std::cout << queue_ptr->pop() << std::endl;
    //            }
    //        }
    //        catch (std::logic_error &e)
    //        {
    //            std::cout << e.what() << std::endl;
    //        }
    //
    //    }
    //
    //    for (auto &stack_ptr: stacks)
    //    {
    //        try
    //        {
    //            for (unsigned int i = 1; i <= 100; i++)
    //            {
    //                stack_ptr->push(i);
    //            }
    //        }
    //        catch (std::length_error &e)
    //        {
    //            std::cout << e.what() << std::endl;
    //        }
    //
    //        try
    //        {
    //            for (unsigned int i = 1; i <= 100; i++)
    //            {
    //                std::cout << stack_ptr->pop() << std::endl;
    //            }
    //        }
    //        catch (std::logic_error &e)
    //        {
    //            std::cout << e.what() << std::endl;
    //        }
    //
    //    }
    //
    //

    //    unsigned int n_values = 5000000;
    //    typedef double data_type;
    //    std::vector<data_type> values(n_values);
    //    for (unsigned int i = 0; i < n_values; i++) values[i] = i;
    //    values[n_values / 2] = -10;
    //    std::cout << std::endl;
    //
    //    typedef std::chrono::high_resolution_clock timer;
    //    std::chrono::time_point<timer> time;
    //    time = timer::now();
    //    my_minimum::scalar_minimum<data_type>(values.begin(), values.end());
    //    std::cout << "Scalar time: \t" << std::chrono::duration_cast<std::chrono::milliseconds>(timer::now() - time).count() << std::endl;
    //    time = timer::now();
    //    my_minimum::parallel_minimum<data_type>(values.begin(), values.end());
    //    std::cout << "Parallel time: \t" << std::chrono::duration_cast<std::chrono::milliseconds>(timer::now() - time).count() << std::endl;

    //    /* Name             Good for parallelisation?
    //     * Insertion sort   No
    //     * Merge Sort       Somewhat (makes copies)
    //     * Heap Sort        Not really.
    //     * Quick Sort       Somewhat (inplace or out of place.)
    //     * Bubble Sort      a tiny bit but not really.
    //     * */
    //
    //    typedef std::chrono::high_resolution_clock timer;
    //    std::chrono::time_point<timer> time;
    //
    //    typedef double data_type;
    //    std::random_device rd;
    //    std::mt19937 rng(rd());
    //    std::vector<data_type> values(1000000);
    //    std::generate(values.begin(), values.end(), std::rand);
    //    std::cout << "is sorted: " << std::is_sorted(values.begin(), values.end()) << std::endl;
    //    time = timer::now();
    //    std::sort(values.begin(), values.end());
    //    std::cout << "STL time: \t" << std::chrono::duration_cast<std::chrono::milliseconds>(timer::now() - time).count() << std::endl;
    //    std::cout << "is sorted: " << std::is_sorted(values.begin(), values.end()) << std::endl;
    //
    //    std::shuffle(values.begin(), values.end(), rng);
    //    std::cout << "is sorted: " << std::is_sorted(values.begin(), values.end()) << std::endl;
    //    time = timer::now();
    //    scalar_sort<std::vector<data_type>>(values.begin(), values.end());
    //    std::cout << "Scalar time: \t" << std::chrono::duration_cast<std::chrono::milliseconds>(timer::now() - time).count() << std::endl;
    //    std::cout << "is sorted: " << std::is_sorted(values.begin(), values.end()) << std::endl;
    //
    //    std::shuffle(values.begin(), values.end(), rng);
    //    std::cout << "is sorted: " << std::is_sorted(values.begin(), values.end()) << std::endl;
    //    time = timer::now();
    //    parallel_sort(values.begin(), values.end());
    //    std::cout << "Parallel time: \t" << std::chrono::duration_cast<std::chrono::milliseconds>(timer::now() - time).count() << std::endl;
    //    std::cout << "is sorted: " << std::is_sorted(values.begin(), values.end()) << std::endl;
}