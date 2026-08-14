#include "leap.h"
#include <stdio.h>
#include <stdbool.h>

bool leap_year(int year){
	if(year % 400 == 0){
		return true;
	}

	if(year % 100 == 0){
		return false;
	}
	if(year % 4 == 0){
		return true;
	}
	else{
		return false;
	}

}

