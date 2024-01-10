import math

def circle_diameter(sides, side_length): 
    
    perimeter = sides*side_length
    apothem = side_length/(2*math.tan(math.pi/sides))
    area = (perimeter*apothem)/2
    return apothem * 2


circle_diameter(4, 4)
    


