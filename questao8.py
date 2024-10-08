list=[]
acertos=0
contador2="sim"
quantidadeDeAlunos=0
for contador in range(1,11):
    resposta=input(f"Digite a letra da {contador} questao (em letra maiuscula):")
    list.append(resposta)

if (list[0]=="A"):
    acertos=acertos+1
if(list[1]=="B"):
    acertos=acertos+1
if(list[2]=="C"):
    acertos=acertos+1
if(list[3]=="D"):
    acertos=acertos+1
if(list[4]=="E"):
    acertos=acertos+1
if(list[5]=="E"):
    acertos=acertos+1
if(list[6]=="D"):
    acertos=acertos+1
if(list[7]=="C"):
    acertos=acertos+1
if(list[8]=="B"):
    acertos=acertos+1
if(list[9]=="A"):
    acertos=acertos+1
print("você Acertou ",acertos, "questões")
    


