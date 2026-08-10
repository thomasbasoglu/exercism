def equilateral(sides):
    sorted_s = sorted(sides)
    if sorted_s[0] <= 0:
        return False
    return  sorted_s[0] == sorted_s[1] and sorted_s[1] == sorted_s[2]
    


def isosceles(sides):
    sorted_s = sorted(sides)
    if sorted_s[0] <= 0 or (sorted_s[0] + sorted_s[1] < sorted_s[2]):
        return False
    
    return sorted_s[0] == sorted_s[1] or sorted_s[1] == sorted_s[2]

def scalene(sides):
    sorted_s = sorted(sides)
    if sorted_s[0] <= 0 or (sorted_s[0] + sorted_s[1] <= sorted_s[2]):
        return False


    return sorted_s[0] != sorted_s[1] and sorted_s[1] != sorted_s[2]
