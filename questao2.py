pares=0
impares=0

for contador in range(1,11):
    numero=int(input(f"Digite o {contador} ° numero "))
    if ( numero%2==0 ):
        pares+=1
    else:
        impares+=1
print("A quantidade de números pares é: ", pares)
print("A quantidade de números impares é: ", impares)