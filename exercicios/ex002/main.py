from ex002 import *
from rich import inspect, print

def main():

    av1 = Avaliacao("Pedro", "matematica", 9.5)
    av1.set_nota(3.5)
    inspect(av1 , private=True)
    # print(av1.get_nota())

    

if __name__ == "__main__":
    main()