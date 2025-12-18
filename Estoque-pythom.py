print(f"=====Estoque=====\n")

nome_produto = input("Digite o nome do produto: ")

preço_caixa = float(input("Digite o preço da caixa R$: "))

unidade_caixa = int(input("Digite a quantidade de unidades por caixa: "))

margem_lucro = float(input("Digite a margem de lucro (%): "))

lucro = preço_caixa + ( preço_caixa * margem_lucro / 100)

preço_unidade = lucro / unidade_caixa

print("O preço de venda do produto:", nome_produto, "é de R$",preço_unidade)