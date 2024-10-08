paisA=80000
paisB=200000
crescimentoA=0
crescimentoB=0
anos=0
while paisA<paisB:
    crescimentoA=paisA*0.03
    crescimentoB=paisB*0.015
    paisA+=crescimentoA
    paisB+=crescimentoB
    anos=anos+1
print("Serão necessários ",anos," anos para que o país A deixe de ter uma população menor do que o país B")
