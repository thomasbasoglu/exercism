#include "darts.h"

uint8_t score(coordinate_t landing_position){
    float distance = (landing_position.x * landing_position.x) + (landing_position.y * landing_position.y);
    if(distance <= 1){
        return 10;
    }

    if(distance <= 25){
        return 5;
    }

    if(distance <= 100){
        return 1;        
    }

    return 0;
}
