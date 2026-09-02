from poligono import *

def main():

    q1 = Quadrado(12)
    c1 = Circulo(2)

    print(f"Perimetro = {q1.perimetro():.2f}")
    print(f"Area = {q1.area():.2f}")

    print()

    print(f"Perimetro = {c1.perimetro():.2f}")
    print(f"Area = {c1.area():.2f}")
    
if __name__ == "__main__":
    main()
