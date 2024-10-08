total=0
numero=int(input("Digite um numero: "))
for contador in range(1,numero+1):
    if (numero%contador==0):
        total+=1
if (total==2):
    print("Este numero é primo")
else:
    print("Este numero não é primo")