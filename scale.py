import math

print("Digite as coordenadas de três pontos -> Triângulo: ")

# Coordinates of a triangle
ax = int(input("Value for aX: "))
ay = int(input("Value for aY: "))

bx = int(input("Value for bX: "))
by = int(input("Value for bY: "))

cx = int(input("Value for cX: "))
cy = int(input("Value for cY: "))

valX = [ax, bx, cx]
valY = [ay, by, cy]

print("")

def baricenter():
    gx = (ax + bx + cx) / 3
    gy = (ay + by + cy) / 3

    return gx, gy

def scale_triangle(sx, sy):
    # Find the centroid of the triangle
    gx, gy = baricenter()

    # Apply scaling transformation relative to the centroid
    ax_scaled = (ax - gx) * sx + gx
    ay_scaled = (ay - gy) * sy + gy

    bx_scaled = (bx - gx) * sx + gx
    by_scaled = (by - gy) * sy + gy

    cx_scaled = (cx - gx) * sx + gx
    cy_scaled = (cy - gy) * sy + gy

    return ax_scaled, ay_scaled, bx_scaled, by_scaled, cx_scaled, cy_scaled

# Asking for scaling factors
sx = float(input("Enter the scaling factor for X: "))
sy = float(input("Enter the scaling factor for Y: "))

# Apply scaling
ax_scaled, ay_scaled, bx_scaled, by_scaled, cx_scaled, cy_scaled = scale_triangle(sx, sy)

# Print scaled coordinates
print("\nScaled Coordinates:")
print(f"A': ({ax_scaled}, {ay_scaled})")
print(f"B': ({bx_scaled}, {by_scaled})")
print(f"C': ({cx_scaled}, {cy_scaled})")
