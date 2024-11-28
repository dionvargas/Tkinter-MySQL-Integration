# Tkinter MySQL Integration
<div style="display: inline_block">
  <img src="https://img.shields.io/badge/Python-3.12-blue">
</div>

Este projeto implementa uma aplicação Python para gerenciar produtos usando MySQL e interface tkinter. Ele utiliza a biblioteca `mysql-connector-python` para se conectar ao banco de dados e realizar operações CRUD (Create, Read, Update, Delete).

## Requisitos

- Python 3.x 
- mysql-connector-python 
- MySQL

## Instalação

### 1. **Clone o repositório**
```bash
git clone https://github.com/dionvargas/Tkinter-MySQL-Integration
cd Tkinter-MySQL-Integration
```

### 2. Instale as dependências
Certifique-se de que você possui a biblioteca mysql-connector-python instalada:
```
pip install mysql-connector-python
```
ou
```
python -m pip install mysql-connector-python
```

### 3. Exexuteo o arquivo ``banco.sql``
Execute o arquivo ``banco.sql`` para criar o banco e o popular.

### 4. Configure a conexão com o banco

Altere as linhas 44 e 76 do arquivo ``telas.py`` para as configurações do seu banco de dados:
```python
# Conexão com o banco de dados
dao = ProdutoDAO(host="localhost", user="root", password="123456", database="produtos_ti")
```

## Estrutura do Projeto

- `produto.py`: Contém a classe Produto e a classe ProdutoDAO que gerenciam as operações no banco de dados.

- `main.py`: Arquivo principal que inicializa a aplicação.

- `telas.py`: Arquivo que gerencia a navegação entre as telas.

- `banco.sql`: Arquivo inicial do banco de dados

- `assets/`: Diretório contendo os recursos gráficos utilizados na interface.

## Uso
 ``` bash
 python main.py
 ```

 ## Funcionalidades

 ### Tela principal
- Lista todos os produtos cadastrados.
- Possui uma barra de rolagem para navegação.
- Botão para visualizar detalhes de um produto específico.

### Tela Secundária
- Exibe os detalhes do produto selecionado.
- Mostra o nome, descrição e preço do produto.
- Botão para voltar à tela principal.

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.