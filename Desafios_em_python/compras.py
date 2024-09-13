class Produto:  
    def __init__(self, nome, codigo, preco_custo, preco_venda):  
        self.nome = nome  
        self.codigo = codigo  
        self.preco_custo = preco_custo  
        self.preco_venda = preco_venda  

    def __str__(self):  
        return f"Nome: {self.nome}\nCódigo: {self.codigo}\nPreço de Custo: R$ {self.preco_custo:.2f}\nPreço de Venda: R$ {self.preco_venda:.2f}"  

class Estoque:  
    def __init__(self):  
        self.produtos = {}  

    def adicionar_produto(self):  
        nome = input("Nome do produto: ")  
        codigo = input("Código do produto: ")  
        preco_custo = float(input("Preço de custo: R$ "))  
        preco_venda = float(input("Preço de venda: R$ "))  
        produto = Produto(nome, codigo, preco_custo, preco_venda)  
        self.produtos[codigo] = produto  
        print("Produto adicionado com sucesso!")  

    def remover_produto(self):  
        codigo = input("Código do produto a ser removido: ")  
        if codigo in self.produtos:  
            del self.produtos[codigo]  
            print("Produto removido com sucesso!")  
        else:  
            print("Produto não encontrado.")  

    def consultar_produto(self):  
        codigo = input("Código do produto a ser consultado: ")  
        if codigo in self.produtos:  
            print(self.produtos[codigo])  
        else:  
            print("Produto não encontrado.")  

    def listar_produtos(self):  
        if self.produtos:  
            for produto in self.produtos.values():  
                print(produto)  
                print("-" * 20)  
        else:  
            print("O estoque está vazio.")  

class Compra:  
    def __init__(self, data, produtos):  
        self.data = data  
        self.produtos = produtos  

    def __str__(self):  
        total = sum(produto.preco_custo * quantidade for produto, quantidade in self.produtos.items())  
        return f"Data da Compra: {self.data}\n" + "\n".join(  
            f"{produto.nome} - Quantidade: {quantidade} - Valor: R$ {(produto.preco_custo * quantidade):.2f}"  
            for produto, quantidade in self.produtos.items()  
        ) + f"\nTotal da Compra: R$ {total:.2f}"  

class Venda:  
    def __init__(self, data, produtos):  
        self.data = data  
        self.produtos = produtos  

    def __str__(self):  
        total = sum(produto.preco_venda * quantidade for produto, quantidade in self.produtos.items())  
        return f"Data da Venda: {self.data}\n" + "\n".join(  
            f"{produto.nome} - Quantidade: {quantidade} - Valor: R$ {(produto.preco_venda * quantidade):.2f}"  
            for produto, quantidade in self.produtos.items()  
        ) + f"\nTotal da Venda: R$ {total:.2f}"  

class Sistema:  
    def __init__(self):  
        self.estoque = Estoque()  
        self.compras = []  
        self.vendas = []  

    def menu(self):  
        print("\n--- Sistema de Cadastro de Compras e Vendas ---")  
        print("1. Cadastrar Produto")  
        print("2. Remover Produto")  
        print("3. Consultar Produto")  
        print("4. Listar Produtos")  
        print("5. Registrar Compra")  
        print("6. Registrar Venda")  
        print("7. Listar Compras")  
        print("8. Listar Vendas")  
        print("0. Sair")  

    def executar(self):  
        while True:  
            self.menu()  
            opcao = input("Digite a opção desejada: ")  

            if opcao == '1':  
                self.estoque.adicionar_produto()  
            elif opcao == '2':  
                self.estoque.remover_produto()  
            elif opcao == '3':  
                self.estoque.consultar_produto()  
            elif opcao == '4':  
                self.estoque.listar_produtos()  
            elif opcao == '5':  
                self.registrar_compra()  
            elif opcao == '6':  
                self.registrar_venda()  
            elif opcao == '7':  
                self.listar_compras()  
            elif opcao == '8':  
                self.listar_vendas()  
            elif opcao == '0':  
                print("Saindo do sistema...")  
                break  
            else:  
                print("Opção inválida.")  

    def registrar_compra(self):  
        data = input("Data da compra (dd/mm/aaaa): ")  
        produtos = {}  
        while True:  
            codigo = input("Código do produto (ou digite 'fim' para finalizar): ")  
            if codigo.lower() == 'fim':  
                break  
            if codigo in self.estoque.produtos:  
                quantidade = int(input("Quantidade: "))  
                produtos[self.estoque.produtos[codigo]] = quantidade  
            else:  
                print("Produto não encontrado no estoque.")  
        compra = Compra(data, produtos)  
        self.compras.append(compra)  
        print("Compra registrada com sucesso!")  

    def registrar_venda(self):  
        data = input("Data da venda (dd/mm/aaaa): ")  
        produtos = {}  
        while True:  
            codigo = input("Código do produto (ou digite 'fim' para finalizar): ")  
            if codigo.lower() == 'fim':  
                break  
            if codigo in self.estoque.produtos:  
                quantidade = int(input("Quantidade: "))  
                if quantidade <= self.estoque.produtos[codigo]:  
                    produtos[self.estoque.produtos[codigo]] = quantidade  
                else:  
                    print(f"Quantidade em estoque insuficiente para {self.estoque.produtos[codigo].nome}")  
            else:  
                print("Produto não encontrado no estoque.")  
        venda = Venda(data, produtos)  
        self.vendas.append(venda)  
        print("Venda registrada com sucesso!")  

    def listar_compras(self):  
        if self.compras:  
            for compra in self.compras:  
                print(compra)  
                print("-" * 20)  
        else:  
            print("Não há compras registradas.")  

    def listar_vendas(self):  
        if self.vendas:  
            for venda in self.vendas:  
                print(venda)  
                print("-" * 20)  
        else:  
            print("Não há vendas registradas.")  

if __name__ == "__main__":  
    sistema = Sistema()  
    sistema.executar()