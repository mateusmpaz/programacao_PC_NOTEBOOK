from desafios.exercicio_25.transportes import *

def main():
    distancia = 0

    entrega = Drone(distancia)
    print(f"Frete de {type(entrega).__name__} em {distancia}Km = {entrega.calc_frete()}")


if __name__ == "__main__":
    main()