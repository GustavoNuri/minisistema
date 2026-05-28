from minisistema15.funcoes import *

vendas = [
    {"id": 1, "loja": "Osório", "vendedor": "João", "cliente": "Carlos", "valor": 150},
    {"id": 2, "loja": "Torres", "vendedor": "Maria", "cliente": "Pedro", "valor": 300},
    {"id": 3, "loja": "Osório", "vendedor": "João", "cliente": "Ana", "valor": 200},
    {"id": 4,  "loja": "Capão", "vendedor": "Lucas", "cliente": "Carlos", "valor": 500},
    {"id": 5, "loja": "Torres", "vendedor": "Maria", "cliente": "João", "valor": 100},
]

while True:
    mostrar_menu()
    opc = input("Sua opção: ")
    if opc == "1":
        print(f"O valor total vendido foi de R${total_vendido(vendas):.2f}")
    elif opc == "2":
        print(total_por_loja(vendas))
    elif opc == "3":
        print(total_por_vendedor(vendas))
    elif opc == "4":
        print(cliente_mais_comprou(vendas))
    elif opc == "5":
        print(vendedor_mais_vendeu(vendas))
    elif opc == "6":
        valor_minimo = numero_positivo("Vendas acima de quanto? R$")
        vendas_opc6 = vendas_acima_de(vendas, valor_minimo)
        mostrar_vendas(vendas_opc6)
    elif opc == "7":
        vendas = cadastrar_venda(vendas)
    elif opc == "8":
        mostrar_vendas(vendas)
    elif opc == "9":
        filtrar_vendas_por_loja(vendas)
    elif opc == "10":
        filtrar_vendas_por_vendedor(vendas)
    elif opc == "11":
        vendas = excluir_venda(vendas)
    elif opc == "0":
        print(f"Saindo do programa...")
        break
    else:
        print("Por favor digite uma das opções disponiveis!")
