import math

print("Digite as coordenadas de tres pontos -> Triangulo: ")

# Coordenadas de um triângulo
ax = int(input("Valor para aX:"))
ay = int(input("Valor para aY:"))

bx = int(input("Valor para bX:"))
by = int(input("Valor para bY:"))

cx = int(input("Valor para cX:"))
cy = int(input("Valor para cY:"))

valX = [ax, bx, cx]
valY = [ay, by, cy]

print("")

def baricentro():
    gx = (ax + bx + cx) / 3
    gy = (ay + by + cy) / 3

    return gx, gy

def rotate_point(x, y, angle, center):
    # Translate the point so that the center becomes the origin
    translated_x = x - center[0]
    translated_y = y - center[1]
    
    # Apply rotation
    new_x = translated_x * math.cos(angle) - translated_y * math.sin(angle)
    new_y = translated_x * math.sin(angle) + translated_y * math.cos(angle)
    
    # Translate back
    new_x += center[0]
    new_y += center[1]
    
    return new_x, new_y

def rotate_triangle(angle):
    # Find centroid
    centroid = baricentro()
    
    # Rotate each point around centroid
    rotated_points = []
    for x, y in zip(valX, valY):
        new_x, new_y = rotate_point(x, y, angle, centroid)
        rotated_points.append((new_x, new_y))
    
    return rotated_points

angle = math.radians(float(input("Enter rotation angle in degrees: ")))

rotated_triangle = rotate_triangle(angle)

print("Rotated Triangle:")
for point in rotated_triangle:
    print("(", point[0], ",", point[1], ")")

