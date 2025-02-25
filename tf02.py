# Inventário de Produtos
class Inventario:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, nome, preco, quantidade):
        if nome in self.produtos:
            self.produtos[nome]['quantidade'] += quantidade
        else:
            self.produtos[nome] = {'preco': preco, 'quantidade': quantidade}

    def remover_produto(self, nome):
        if nome in self.produtos:
            del self.produtos[nome]
        else:
            print(f"Produto {nome} não encontrado no inventário.")

    def listar_produtos(self):
        if not self.produtos:
            print("Inventário vazio.")
        else:
            for nome, info in self.produtos.items():
                print(f"Produto: {nome}, Preço: {info['preco']:.2f}, Quantidade: {info['quantidade']}")

# Exemplo de uso
if __name__ == "__main__":
    inventario = Inventario()
    while True:
        print("\n1. Adicionar Produto\n2. Remover Produto\n3. Listar Produtos\n4. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            nome = input("Nome do produto: ")
            preco = input("Preço do produto (use vírgula para decimais): ").replace(',', '.')
            quantidade = int(input("Quantidade do produto: "))
            inventario.adicionar_produto(nome, float(preco), quantidade)
        elif escolha == '2':
            nome = input("Nome do produto a ser removido: ")
            inventario.remover_produto(nome)
        elif escolha == '3':
            inventario.listar_produtos()
        elif escolha == '4':
            break
        else:
            print("Opção inválida.")
