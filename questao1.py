numero=int(input("Digite um número inteiro de 1 a 10: "))
print("TABUADA DE ", numero, ":")
for contador in range(1,11):
    numerotb=numero*contador
    print("*", numero, " x " , contador, " = ",numerotb)
print("Fim")