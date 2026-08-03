#include "resistor_color.h"
resistor_band_t array[] = {
		(resistor_band_t)0,
		(resistor_band_t)1,
		(resistor_band_t)2,
		(resistor_band_t)3,
		(resistor_band_t)4,
		(resistor_band_t)5,
		(resistor_band_t)6,
		(resistor_band_t)7,
		(resistor_band_t)8,
		(resistor_band_t)9
};

int color_code(resistor_band_t color){
    return (int)color;
}

const resistor_band_t *colors(){
		return array;
}
