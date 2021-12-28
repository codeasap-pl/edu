#include <iostream>


int main()
{
	int limit = 4000000;
	int prev = 0;
	int curr = 1;
	int temp = 0;
	int total = 0;

  fib:
	temp = prev + curr;
	if (temp > limit) goto end;
	total += (temp % 2 == 0) ? temp : 0;
	prev = curr;
	curr = temp;
	goto fib;

  end:
	std::cout << total << std::endl;
}
