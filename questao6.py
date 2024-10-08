salario=1000
anoAtual=2025
crescimento=0.015
for ano in range(1996,anoAtual + 1):
    salario= salario +(salario*crescimento)
    crescimento= crescimento*2 
print(f"O salário em {anoAtual} será de R$ {salario:.2f}")