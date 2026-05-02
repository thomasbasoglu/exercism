def equilateral(sides):
    side_a, side_b, side_c = sides
    is_valid = (side_a > 0 and side_b > 0 and side_c > 0 and side_a + side_b >= side_c and side_b + side_c >= side_a and side_a + side_c >= side_b)
    
    if not is_valid:
        return False
    
    return side_a == side_b == side_c
    


def isosceles(sides):
    side_a, side_b, side_c = sides

    is_valid = (side_a > 0 and side_b > 0 and side_c > 0 and side_a + side_b >= side_c and side_b + side_c >= side_a and side_a + side_c >= side_b)
    
    if not is_valid:
        return False
    
    return side_a == side_b or side_b == side_c or side_a == side_c

def scalene(sides):
    side_a, side_b, side_c = sides

    is_valid = (side_a > 0 and side_b > 0 and side_c > 0 and side_a + side_b >= side_c and side_b + side_c >= side_a and side_a + side_c >= side_b)
    
    if not is_valid:
        return False
    
    return side_a != side_b and side_b != side_c and side_a != side_c
