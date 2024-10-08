valor=1.99
quantidade=int(input("Digite a quantidade de produtos(máximo 50 produdos): "))
for contador in range(1,quantidade+1):
    valor1= valor*contador
    print(contador,": R$", valor1)
  
