import math

def get_coordinates(label):
    x = int(input(f"Valor para {label}X: "))
    y = int(input(f"Valor para {label}Y: "))
    return x, y

def translate_triangle(x_values, y_values):
    tx = int(input("Digite quantos você deseja somar nas coordenadas de X: "))
    ty = int(input("Digite quantos você deseja somar nas coordenadas de Y: "))

    translated_x = [x + tx for x in x_values]
    translated_y = [y + ty for y in y_values]

    return translated_x, translated_y

def main():
    print("Digite as coordenadas de três pontos -> Triângulo: ")

    # Coordenadas de um triângulo
    ax, ay = get_coordinates("a")
    bx, by = get_coordinates("b")
    cx, cy = get_coordinates("c")

    x_values = [ax, bx, cx]
    y_values = [ay, by, cy]

    print("")

    print("Coordenadas Originais:", x_values, y_values)

    translated_x, translated_y = translate_triangle(x_values, y_values)

    print("Novas coordenadas:", translated_x, translated_y)

main()
