#include "stack.hxx"
#include <cassert>


int main()
{
	{ // Test: sizes
		stack<int> s(8);
		assert(s.max_size() == 8);
		assert(s.size() == 0);
	}

	{ // Test: push
		stack<int> s(8);
		s.push(1);
		assert(s.size() == 1);

		s.push(2);
		assert(s.size() == 2);

		s.push(3);
		assert(s.size() == 3);
	}

	{ // Test: pop
		stack<int> s(8);
		s.push(1);
		assert(s.size() == 1);

		assert(s.pop() == 1);
		assert(s.size() == 0);
	}

	{ // Test: push - stack full
		stack<int> s(3);
		s.push(1);
		s.push(2);
		s.push(3);
		assert(s.size() == 3);

		bool raised = false;
		try {
			s.push(4);
		}
		catch(const std::runtime_error& e) {
			raised = true;
		}

		assert(raised);
	}

	{ // Test: pop - stack empty
		stack<int> s(1);
		s.push(1);
		assert(s.size() == 1);

		assert(s.pop() == 1);

		bool raised = false;
		try {
			s.pop();
		}
		catch(const std::runtime_error& e) {
			raised = true;
		}

		assert(raised);
	}

	{ // Test: peek
		stack<int> s(3);
		s.push(1);
		assert(s.peek() == 1);
		s.push(2);
		assert(s.peek() == 2);
		s.push(3);
		assert(s.peek() == 3);
	}

	{ // Test: peek - stack empty
		stack<int> s(0);
		bool raised = false;
		try {
			s.peek();
		}
		catch(const std::runtime_error& e) {
			raised = true;
		}

		assert(raised);
	}

	return 0;
}
