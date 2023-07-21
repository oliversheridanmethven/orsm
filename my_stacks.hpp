//
// Created by Oliver Sheridan-Methven on 14/11/2020.
//

#ifndef MISC_MYSTACK_HPP
#define MISC_MYSTACK_HPP

#include <stdexcept>
#include <memory>
#include <mutex>

namespace my_stacks
{
    template<typename T>
    class Stack
    {
    public:
        virtual T pop() = 0;

        virtual void push(const T data) = 0;
    };

    template<typename T, int MAX_ITEMS>
    class Stack_1 : public Stack<T>
    {
        /* A templated stack where I use a backend container for the storage. */
    public:

        Stack_1() : free_position{items}, n_items{0}
        {}

        T pop()
        {
            if (not n_items) throw std::logic_error("The stack is empty.");
            T data = *--free_position;
            n_items--;
            return data;
        }

        void push(const T data)
        {
            if (n_items == MAX_ITEMS) throw std::length_error("The stack is full.");
            *free_position++ = data;
            n_items++;
        }

    private:
        T items[MAX_ITEMS];
        T *free_position;
        unsigned int n_items;
    };

    template<typename T, int MAX_ITEMS>
    class Stack_2 : public Stack<T>
    {
        /* A templated stack where I use do my own data allocation. */
    public:
        Stack_2() : free_position{items}, n_items{0}
        {}

        T pop()
        {
            if (not n_items) throw std::logic_error("The stack is empty.");
            n_items--;
            T *data_ptr = *--free_position;
            T data = *data_ptr;
            delete data_ptr;
            return data;
        }

        void push(const T data)
        {
            if (n_items == MAX_ITEMS) throw std::length_error("The stack is full.");
            T *data_ptr = new T;
            *data_ptr = data;
            *free_position++ = data_ptr;
            n_items++;
        }

    private:
        T *items[MAX_ITEMS];
        T **free_position;
        unsigned int n_items;
    };

    template<typename T, int MAX_ITEMS>
    class Stack_3 : public Stack<T>
    {
        /* A templated stack where I using unique pointers. */

    public:

        Stack_3() : free_position{items}, n_items{0}
        {}

        T pop()
        {
            if (not n_items) throw std::logic_error("The stack is empty.");
            n_items--;
            std::unique_ptr<T> data_ptr{std::move(*--free_position)};
            T data = *data_ptr;
            return data;
        }

        void push(const T data)
        {
            if (n_items == MAX_ITEMS) throw std::length_error("The stack is full.");

            n_items++;
            *free_position = std::unique_ptr<T>(new T);
            **free_position++ = data;
        }


    private:
        std::unique_ptr<T> items[MAX_ITEMS];
        std::unique_ptr<T> *free_position;
        unsigned int n_items;
    };

}

#endif //MISC_MYSTACK_HPP
