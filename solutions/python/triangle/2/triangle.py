def equilateral(sides):
    s = sorted(sides)
    if s[0] <= 0 or s[0] + s[1] < s[2]:
        return False
    return s[0] == s[1] == s[2]
    


def isosceles(sides):
    s = sorted(sides)
    if s[0] <= 0 or s[0] + s[1] < s[2]:
        return False
    return s[0] == s[1] or s[1] == s[2]

def scalene(sides):
    s = sorted(sides)
    if s[0] <= 0 or s[0] + s[1] < s[2]:
        return False
    return s[0] != s[1] and s[1] != s[2]
