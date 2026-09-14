from funcionarios import *

def main():

    f1 = Horista("Julio", 12, 400)
    f1.calc_sal()
    f1.analisar_salario()

    f2 = Mensalista("Amanda", 9500)
    f2.calc_sal()
    f2.analisar_salario()

if __name__ == "__main__":
    main()