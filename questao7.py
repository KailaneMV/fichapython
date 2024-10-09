divida=float(input("Digite o valor da dívida: R$ "))
tabela=[(1, 0),(3, 10),(6, 15),(9, 20),(12, 25)]
print(f"{'Valor da Dívida'} | {'Juros'} | {'Parcelas'} | {'Valor da Parcela'}")
print("---------------------------------------------------------")
for parcelas, juros in tabela:
    valorComJuros=divida*(1+(juros/100)) 
    valorParcela=valorComJuros/parcelas  
    print(f"R$ {valorComJuros:.2f} | {juros}(%) | {parcelas} | R${valorParcela:.2f}")