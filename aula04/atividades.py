#Atividade 01
#Sistema de compras
# valor = float(input('Digite o valor da compra: '))
# if valor > 250.00:
#     desconto = valor * 16/100
#     total = valor - desconto
#     print(f'Desconto de 16%: {desconto:.2f} \nTotal: {total:.2f}')
# else:
#     print(f'Não há desconto! \nTotal: {valor}')

#Atividade 02
#Liberaçao de pedido
qtd_disponivel = int(input("Informe a quantidade diponivel em estoque: "))
qtd_cliente = int(input('Informe o pedido do cliente: '))
peso = float(input('Informe o peso total do pedido: '))
if qtd_disponivel >= qtd_cliente:
    if peso <= 50:
        print('Pedido enviado!')
    else:
        print('Pedido não pode ser enviado! Muito pesado...')
else:
    print('Pedido não pode ser enviado! Não há a quantidade disponível em estoque...')
