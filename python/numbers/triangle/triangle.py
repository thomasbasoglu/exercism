def equilateral(sides):
    side_a, side_b, side_c = sides
    
    if not min(sides)>0:
        return False
    
    return side_a == side_b == side_c
    


def isosceles(sides):

    side_a, side_b, side_c = sides

    if not min(sides) > 0 or sum(sides) < 2 * max(sides):
        return False
    
    return side_a == side_b or side_b == side_c or side_a == side_c

def scalene(sides):
    side_a, side_b, side_c = sides

    if not min(sides) > 0 or sum(sides) < 2 * max(sides):
        return False
 
    return side_a != side_b and side_b != side_c and side_a != side_c
