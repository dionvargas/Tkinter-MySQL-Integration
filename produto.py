import mysql.connector  # Importa o módulo mysql.connector para se conectar e interagir com o banco de dados MySQL

# Define a classe Produto que representa um produto com nome, descrição e preço
class Produto:
    def __init__(self, nome, descricao, preco):
        self.nome = nome  # Atribui o nome do produto
        self.descricao = descricao  # Atribui a descrição do produto
        self.preco = preco  # Atribui o preço do produto
        self.id = None  # Inicializa o ID do produto como None
    
    def imprimir(self):
        # Método para imprimir as informações do produto
        print(f"Id: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Descrição: {self.descricao}")
        print(f"Preço: R$ {self.preco}")

# Define a classe ProdutoDAO que gerencia as operações no banco de dados
class ProdutoDAO:
    
    def __init__(self, host, user, password, database):
        # Construtor que estabelece a conexão com o banco de dados usando as credenciais fornecidas
        self.conexao = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conexao.cursor()  # Cria um cursor para executar comandos SQL

    def criar_tabela(self):
        # Método para criar a tabela de produtos no banco de dados, se não existir
        query = """
        CREATE TABLE IF NOT EXISTS produto (
            id INT AUTO_INCREMENT PRIMARY KEY,  # ID do produto, gerado automaticamente
            nome VARCHAR(255) NOT NULL,  # Nome do produto, obrigatório
            descricao TEXT,  # Descrição do produto
            preco DECIMAL(10, 2) NOT NULL  # Preço do produto, obrigatório
        );
        """
        self.cursor.execute(query)  # Executa a query para criar a tabela
        self.conexao.commit()  # Confirma a execução da query

    def inserir(self, produto):
        # Método para inserir um novo produto na tabela de produtos
        query = "INSERT INTO produto (nome, descricao, preco) VALUES (%s, %s, %s)"
        valores = (produto.nome, produto.descricao, produto.preco)  # Valores do produto a serem inseridos
        self.cursor.execute(query, valores)  # Executa a query com os valores
        self.conexao.commit()  # Confirma a execução da query

    def listar(self):
        # Método para listar todos os produtos na tabela de produtos
        query = "SELECT * FROM produto"
        self.cursor.execute(query)  # Executa a query para selecionar todos os produtos
        resultados = self.cursor.fetchall()  # Recupera todos os resultados
        produtos = []  # Lista para armazenar os objetos Produto
        for resultado in resultados:
            # Cria um objeto Produto para cada registro retornado
            produto = Produto(resultado[1], resultado[2], resultado[3])
            produto.id = resultado[0]  # Atribui o ID do produto
            produtos.append(produto)  # Adiciona o produto à lista
        return produtos  # Retorna a lista de produtos

    def atualizar(self, produto_id, produto):
        # Método para atualizar um produto existente na tabela de produtos
        query = """
        UPDATE produto
        SET nome = %s, descricao = %s, preco = %s
        WHERE id = %s
        """
        valores = (produto.nome, produto.descricao, produto.preco, produto_id)  # Valores atualizados do produto
        self.cursor.execute(query, valores)  # Executa a query com os valores
        self.conexao.commit()  # Confirma a execução da query

    def deletar(self, produto_id):
        # Método para deletar um produto da tabela de produtos pelo ID
        query = "DELETE FROM produto WHERE id = %s"
        self.cursor.execute(query, (produto_id,))  # Executa a query com o ID do produto
        self.conexao.commit()  # Confirma a execução da query

    def buscar_por_id(self, produto_id):
        # Método para buscar um produto na tabela de produtos pelo ID
        query = "SELECT * FROM produto WHERE id = %s"
        self.cursor.execute(query, (produto_id,))  # Executa a query com o ID do produto
        resultado = self.cursor.fetchone()  # Recupera o resultado
        if resultado:
            # Cria um objeto Produto se o resultado for encontrado
            produto = Produto(resultado[1], resultado[2], resultado[3])
            produto.id = resultado[0]  # Atribui o ID do produto
            return produto  # Retorna o produto
        return None  # Retorna None se o produto não for encontrado

    def __del__(self):
        # Destrutor que fecha a conexão com o banco de dados e o cursor
        self.cursor.close()  # Fecha o cursor
        self.conexao.close()  # Fecha a conexão