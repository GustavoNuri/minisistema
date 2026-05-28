def total_vendido(lista):
    soma_vendas = 0
    for venda in lista:
        soma_vendas += venda["valor"]
    return soma_vendas


def total_por_loja(lista):
    lojas = {}
    for venda in lista:
        if venda["loja"] not in lojas:
            lojas[venda["loja"]] = venda["valor"]
        else:
           lojas[venda["loja"]] += venda["valor"]
    return lojas


def total_por_vendedor(lista):
    vendedor = {}
    for venda in lista:
        if venda["vendedor"] not in vendedor:
            vendedor[venda["vendedor"]] = venda["valor"]
        else:
            vendedor[venda["vendedor"]] += venda["valor"]
    return vendedor


def cliente_mais_comprou(lista):
    maior_cliente = ""
    mais_comprou = 0
    clientes = {}
    for venda in lista:
        if venda["cliente"] not in clientes:
            clientes[venda["cliente"]] = venda["valor"]
        else:
            clientes[venda["cliente"]] += venda["valor"]
    for nome, valor in clientes.items():
        if valor > mais_comprou:
            maior_cliente = nome
            mais_comprou = valor
    return maior_cliente


def vendedor_mais_vendeu(lista):
    mais_vendeu = ""
    valor_vendas = 0
    vendedores = {}
    for venda in lista:
        if venda["vendedor"] not in vendedores:
            vendedores[venda["vendedor"]] = venda["valor"]
        else:
            vendedores[venda["vendedor"]] += venda["valor"]
    for nome, valor in vendedores.items():
        if valor > valor_vendas:
            mais_vendeu = nome
            valor_vendas = valor
    return mais_vendeu


def vendas_acima_de(lista, valor_minimo):
    acima_de = []
    for venda in lista:
        if venda["valor"] > valor_minimo:
            acima_de.append(venda)
    return acima_de


def mostrar_menu():
    print("1 - Total vendido")
    print("2 - Total por loja")
    print("3 - Total por vendedor")
    print("4 - Cliente que mais comprou")
    print("5 - Vendedor que mais vendeu")
    print("6 - Vendas acima de determinado valor")
    print("7 - Cadastrar nova venda")
    print("8 - Mostrar vendas")
    print("9 - Filtrar vendas por loja")
    print("10 - Filtrar vendas por vendedor")
    print("11 - Excluir venda")
    print("0 - Sair")


def mostrar_vendas(lista):
    for venda in lista:
        print(f"ID: {venda["id"]}  Loja:{venda["loja"]:>7} | Vendedor: {venda["vendedor"]:>7} | Cliente:{venda["cliente"]:>7} | "
              f"Valor: R$ {venda["valor"]:>7.2f}")


def cadastrar_venda(lista):
    nova_venda = {}
    nova_venda["id"] = gerar_proximo_id(lista)
    nova_venda["loja"] = selecionar_loja(lista)
    nova_venda["vendedor"] = texto_obrigatorio("Vendedor: ")
    nova_venda["cliente"] = texto_obrigatorio("Cliente: ")
    nova_venda["valor"] = numero_positivo("Valor: ")
    lista.append(nova_venda)
    print("Cadastro realizado com sucesso!")
    return lista


def inteiro_valido(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
        except (ValueError, TypeError):
            print("ERRO! Por favor digite um número inteiro válido")
        else:
            return numero


def numero_valido(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
        except (ValueError, TypeError):
            print("ERRO! Por favor digite um número válido")
        else:
            return numero


def numero_positivo(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
        except (ValueError, TypeError):
            print("ERRO! Por favor digite um número válido")
        else:
            if numero > 0:
                return numero
            else:
                print("ERRO! Por favor digite um número maior que zero")


def texto_obrigatorio(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto == "":
            print("ERRO! Por favor digite um texto")
        else:
            return texto


def selecionar_loja(lista):
    lojas = listar_lojas(lista)
    while True:
        escolha = inteiro_valido("Qual loja deseja? ")
        indice = escolha - 1
        if indice >= 0 and indice < len(lojas):
            return lojas[indice]
        else:
            print("Por favor digite uma opção válida!")


def filtrar_vendas_por_loja (lista):
    vendas_filtradas = []
    loja = selecionar_loja(lista)
    for venda in lista:
        if venda["loja"] == loja:
            vendas_filtradas.append(venda)
    mostrar_vendas(vendas_filtradas)


def listar_lojas(lista):
    lojas = []
    for unidade in lista:
        if unidade["loja"] not in lojas:
            lojas.append(unidade["loja"])
    for indice, unidade in enumerate(lojas):
        print(f"{indice+1} - {unidade}")
    return lojas


def selecionar_vendedor(lista):
    vendedores = listar_vendedores(lista)
    while True:
        escolha = inteiro_valido("Qual loja deseja? ")
        indice = escolha - 1
        if indice >= 0 and indice < len(vendedores):
            return vendedores[indice]
        else:
            print("Por favor digite uma opção válida!")


def filtrar_vendas_por_vendedor (lista):
    vendas_filtradas = []
    loja = selecionar_vendedor(lista)
    for venda in lista:
        if venda["vendedor"] == loja:
            vendas_filtradas.append(venda)
    mostrar_vendas(vendas_filtradas)


def listar_vendedores(lista):
    vendedores = []
    for unidade in lista:
        if unidade["vendedor"] not in vendedores:
            vendedores.append(unidade["vendedor"])
    for indice, unidade in enumerate(vendedores):
        print(f"{indice+1} - {unidade}")
    return vendedores

def gerar_proximo_id(lista):
    maior_id = 0
    for venda in lista:
        if venda["id"] > maior_id:
            maior_id = venda["id"]
    return maior_id + 1

def buscar_venda_por_id(lista, id):
    for venda in lista:
        if venda["id"] == id:
            return venda
    return None

def mostrar_venda(venda):
    print(f"ID: {venda["id"]}")
    print(f"Loja: {venda["loja"]}")
    print(f"Vendedor: {venda["vendedor"]}")
    print(f"Cliente: {venda["cliente"]}")
    print(f"Valor: R${venda["valor"]:.2f}")

def excluir_venda(lista):
    while True:
        venda_escolhida = inteiro_valido("Digite o ID da venda que deseja excluir: ")
        venda = buscar_venda_por_id(lista, venda_escolhida)
        if venda is None:
            print("Venda não encontrada!")
        else:
            mostrar_venda(venda)
            break
    while True:
        escolha = texto_obrigatorio("Confirma a exclusão da venda?[S/N] ").strip().upper()
        if escolha == "S":
            lista.remove(venda)
            print("Venda excluida com sucesso!")
            return lista
        elif escolha == "N":
            print("Venda não excluida")
            return lista
        else:
            print("Por favor digite somete S (SIM) ou N (Não)")

