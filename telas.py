from pathlib import Path  # Importa a classe Path para manipular caminhos de arquivos
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, Scrollbar  # Importa os componentes do Tkinter
from produto import ProdutoDAO  # Importa a classe ProdutoDAO do módulo produto

# Classe TelaPrincipal, herda de Frame
class TelaPrincipal(Frame):
    def __init__(self, parent, assets_path, on_navigate):
        super().__init__(parent)  # Chama o construtor da classe base Frame
        self.assets_path = Path(assets_path)  # Define o caminho para os assets
        self.on_navigate = on_navigate  # Função para alternar entre telas
        self.setup_ui()  # Configura a interface do usuário

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)  # Gera o caminho absoluto para os assets

    def setup_ui(self):
        self.configure(bg="#A3D2FF")  # Configura a cor de fundo do frame

        # Cria um canvas para a tela principal
        canvas = Canvas(self, bg="#A3D2FF", height=568, width=320, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)
        canvas.create_rectangle(10.0, 9.0, 310.0, 559.0, fill="#A3D2FF", outline="")
        canvas.create_text(29.0, 20.0, anchor="nw", text="Produtos", fill="#000000", font=("Graduate Regular", 36 * -1))

        # Frame rolável
        container = Frame(self, bg="#A3D2FF")  # Cria um container para o frame rolável
        container.place(x=10, y=80, width=300, height=470)

        # Configura a barra de rolagem
        scrollbar = Scrollbar(container, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        # Configura o canvas rolável
        scroll_canvas = Canvas(container, bg="#A3D2FF", yscrollcommand=scrollbar.set, width=300, height=470)
        scroll_canvas.pack(side="left", fill="both", expand=True)

        # Frame interno rolável
        scrollable_frame = Frame(scroll_canvas, bg="#A3D2FF")
        scrollable_frame.bind("<Configure>", lambda e: scroll_canvas.configure(scrollregion=scroll_canvas.bbox("all")))
        scroll_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        scrollbar.config(command=scroll_canvas.yview)

        # Conexão com o banco de dados
        dao = ProdutoDAO(host="localhost", user="root", password="123456", database="produtos_ti")
        products = dao.listar()  # Lista todos os produtos do banco de dados

        # Cria a seção para cada produto
        for i, produto in enumerate(products):
            self.create_product_section(scrollable_frame, produto.nome, "view.png", lambda n=produto.id: self.on_button_click(n), y_start=60 * i)

    def create_product_section(self, parent, product_name, button_image, command, y_start):
        # Cria um frame para cada produto
        section_frame = Frame(parent, bg="#D9D9D9", relief="solid", bd=1)
        section_frame.pack(fill="x", padx=10, pady=5)

        # Adiciona um rótulo com o nome do produto
        label = Canvas(section_frame, bg="#D9D9D9", height=50, width=180, bd=0, highlightthickness=0, relief="ridge")
        label.pack(side="left", padx=10, pady=10)
        label.create_text(10, 10, anchor="nw", text=product_name, fill="#000000", font=("Gudea", 20 * -1))

        # Adiciona um botão para visualizar o produto
        button_img = PhotoImage(file=self.relative_to_assets(button_image))
        button = Button(section_frame, image=button_img, borderwidth=0, highlightthickness=0, command=command, relief="flat")
        button.image = button_img  # Armazena a imagem para evitar que seja descartada pelo garbage collector
        button.pack(side="right", padx=10, pady=10)

    def on_button_click(self, product_id):
        self.on_navigate(product_id)  # Chama a função de navegação passando o ID do produto

# Classe TelaSecundaria, herda de Frame
class TelaSecundaria(Frame):
    def __init__(self, parent, assets_path, on_back):
        super().__init__(parent)  # Chama o construtor da classe base Frame
        self.assets_path = Path(assets_path)  # Define o caminho para os assets
        self.on_back = on_back  # Função para voltar à tela principal
        self.dao = ProdutoDAO(host="localhost", user="root", password="123456", database="produtos_ti")  # Instancia o DAO do Produto
        self.setup_ui()  # Configura a interface do usuário

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)  # Gera o caminho absoluto para os assets

    def setup_ui(self):
        self.configure(bg="#FFFFFF")  # Configura a cor de fundo do frame

        # Cria um canvas para a tela secundária
        self.canvas = Canvas(self, bg="#FFFFFF", height=568, width=320, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(10.0, 9.0, 310.0, 559.0, fill="#A3D2FF", outline="")
        self.canvas.create_text(34.0, 101.0, anchor="nw", text="Descrição:", fill="#000000", font=("Gudea", 24 * -1))
        self.canvas.create_text(34.0, 302.0, anchor="nw", text="Valor:", fill="#000000", font=("Gudea", 24 * -1))
        self.canvas.create_rectangle(33.0, 71.0, 282.0, 72.0, fill="#000000", outline="")
        self.produto_nome_text = self.canvas.create_text(28.0, 30.0, anchor="nw", text="", fill="#000000", font=("Graduate Regular", 24 * -1))

        # Campo para exibir o preço do produto
        self.entry_1 = Entry(self, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=101.0, y=305.0, width=181.0, height=25.0)

        # Campo para exibir a descrição do produto
        self.entry_2 = Text(self, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=34.0, y=140.0, width=248.0, height=154.0)

        # Botão para voltar à tela principal
        button_img = PhotoImage(file=self.relative_to_assets("button_1.png"))
        back_button = Button(self, image=button_img, borderwidth=0, highlightthickness=0, command=self.on_back, relief="flat")
        back_button.image = button_img  # Armazena a imagem para evitar que seja descartada pelo garbage collector
        back_button.place(x=34.0, y=499.0, width=248.0, height=40.0)

    def atualizar_detalhes(self, product_id):
        # Atualiza os detalhes do produto na tela secundária
        produto = self.dao.buscar_por_id(product_id)
        if produto:
            self.canvas.itemconfig(self.produto_nome_text, text=produto.nome)
            self.entry_1.config(state='normal')
            self.entry_1.delete(0, 'end')
            self.entry_1.insert(0, f"R$ {produto.preco:.2f}")
            self.entry_1.config(state='disabled')

            self.entry_2.config(state='normal')
            self.entry_2.delete('1.0', 'end')
            self.entry_2.insert('1.0', produto.descricao)
            self.entry_2.config(state='disabled')

# Classe principal do aplicativo
class App:
    def __init__(self, root):
        self.root = root  # Referência à janela principal
        self.assets_path = Path(__file__).resolve().parent / "build" / "assets"  # Define o caminho para os assets
        # Instancia as telas principal e secundária
        self.frames = {
            "TelaPrincipal": TelaPrincipal(root, self.assets_path / "frame0", self.show_tela_secundaria),
            "TelaSecundaria": TelaSecundaria(root, self.assets_path / "frame1", self.show_tela_principal)
        }
        # Posiciona as telas na janela principal
        for frame in self.frames.values():
            frame.place(x=0, y=0, width=320, height=568)
        self.show_tela_principal()  # Exibe a tela principal inicialmente

    def show_tela_principal(self):
        self.frames["TelaPrincipal"].tkraise()  # Eleva a tela principal ao topo, tornando-a visível

    def show_tela_secundaria(self, product_id):
        self.frames["TelaSecundaria"].atualizar_detalhes(product_id)  # Atualiza os detalhes do produto na tela secundária
        self.frames["TelaSecundaria"].tkraise()  # Eleva a tela secundária ao topo, tornando-a visível