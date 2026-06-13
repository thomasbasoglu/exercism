#include "difference_of_squares.h"

unsigned int sum_of_squares(unsigned int number){
	unsigned int sum = 0;
	for(unsigned int i = 1; i <= number; i++){
		sum += i * i;
	}
	return (unsigned int)sum;
}

unsigned int square_of_sum(unsigned int number){
	unsigned int sum = 0;
	for(unsigned int i = 1; i <= number; i++){
		sum += i;
	}
	return (unsigned int) sum * sum;
}

unsigned int difference_of_squares(unsigned int number){
	unsigned long square = square_of_sum(number);
	unsigned long squares = sum_of_squares(number);
	return (unsigned int)(square-squares);
}