#Atividade 01
#Sistema de compras
valor = float(input('Digite o valor da compra: '))
if valor > 250.00:
    desconto = valor * 16/100
    total = valor - desconto
    print(f'Desconto de 16%: {desconto:.2f} \nTotal: {total:.2f}')
else:
    print(f'Não há desconto! \nTotal: {valor}')
