#pragma once

#include <cstddef>
#include <stdexcept>


template <class T>
class stack
{
public:
	stack(std::size_t max_size)
		: max_size_(max_size),
		  top_(0),
		  stack_(new T[max_size_])
	{
	}

	~stack()
	{
		delete[] stack_;
	}

	void push(const T& value)
	{
		if(top_ >= max_size_) {
			throw std::runtime_error("Stack full");
		}

		stack_[top_] = value;
		top_++;
	}

	T pop()
	{
		if(!top_) {
			throw std::runtime_error("Stack empty");
		}

		top_--;
		return stack_[top_];
	}

	T peek() const
	{
		if(!top_) {
			throw std::runtime_error("Stack empty");
		}
		return stack_[top_ - 1];
	}

	std::size_t max_size()
	{
		return max_size_;
	}

	std::size_t size()
	{
		return top_;
	}

private:
	std::size_t max_size_;
	std::size_t top_ = 0;
	T* stack_;
};
