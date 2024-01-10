import math

# def circle_diameter(sides, side_length): 
    

def polygon_square(sides, side_length):

    pols_sq = math.sqrt(((sides*side_length**2)/4)*(1/math.tan(180/sides)))
    print(pols_sq)
    return pols_sq

polygon_square(3, 4)
    


