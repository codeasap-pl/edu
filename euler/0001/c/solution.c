#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>


/*
  Multiples of 3 and 5
  Problem 1

  If we list all the natural numbers below 10 that are multiples of 3 or 5,
  we get 3, 5, 6 and 9. The sum of these multiples is 23.
  Find the sum of all the multiples of 3 or 5 below 1000.
*/


long long calculate_sum(unsigned long limit)
{
	unsigned long long sum = 0;
	unsigned long i = 0;

	while(i < limit) {
		if(i % 3 == 0 || i % 5 == 0) {
			sum += i;
		}
		i++;
	}

	return sum;
}


int main(int argc, char** argv)
{
	unsigned long range0 = (argc > 1 ? strtoul(argv[1], 0, 10) : 1000);
	unsigned long range1 = (argc > 2 ? strtoul(argv[2], 0, 10) : 0);

	if(errno) {
		fprintf(stderr, strerror(errno));
		return 1;
	}

	if(!range1) {
		printf("%lld\n", calculate_sum(range0));
	}
	else {
		if(range1 <= range0) {
			fprintf(stderr, "Invalid range: (%ld - %ld)\n", range0, range1);
			return 1;
		}

		while(range0 <= range1) {
			printf("%lld # %ld\n", calculate_sum(range0), range0);
			range0++;
		}
	}

	return 0;
}
