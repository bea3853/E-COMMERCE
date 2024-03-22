def listar_produtos(produtos):
    for i, produto in enumerate(produtos):
        print(f'{i + 1}. {produto[0]}: R${produto[1]:.2f}')

def adicionar_produto_carrinho(escolha_produto, produtos, carrinho):
    if escolha_produto < 1 or escolha_produto > len(produtos):
        print("Escolha inválida. Por favor, escolha um número válido.")
        return carrinho

    carrinho.append(produtos[escolha_produto - 1])
    print("Produto adicionado ao carrinho.")
    return carrinho

def calcular_total(carrinho):
    total = sum(produto[1] for produto in carrinho)
    return total

def main():
    produtos = [
        ("Camiseta", 50.00),
        ("Calça", 80.00),
        ("Tênis", 120.00)
    ]

    print("Bem-vindo ao sistema de e-commerce!")
    print("Por favor, insira seus dados:")

    nome = input("Nome: ")
    cpf = input("CPF: ")
    email = input("E-mail: ")
    endereco = input("Endereço: ")

    carrinho = []

    while True:
        print("\nProdutos disponíveis:")
        listar_produtos(produtos)

        escolha_produto = int(input("\nEscolha o número do produto desejado (ou 0 para finalizar): "))
        if escolha_produto == 0:
            break

        carrinho = adicionar_produto_carrinho(escolha_produto, produtos, carrinho)

    print("\nProdutos no carrinho:")
    listar_produtos(carrinho)

    total = calcular_total(carrinho)
    print(f"\nTotal a pagar: R${total:.2f}")

    forma_pagamento = input("\nEscolha a forma de pagamento (ex: Cartão de Crédito, Transferência, etc.): ")

    print("\n--- Confirmação de compra ---")
    print("Dados do cliente:")
    print(f"Nome: {nome}")
    print(f"CPF: {cpf}")
    print(f"E-mail: {email}")
    print(f"Endereço: {endereco}")

    print("\nProdutos:")
    listar_produtos(carrinho)

    print("\nForma de pagamento:", forma_pagamento)
    print("\nSeu pedido será entregue em até 5 dias úteis. Obrigado pela compra!")

if __name__ == "__main__":
    main()
