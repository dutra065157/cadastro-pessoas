# criar a janela de longin
import flet as ft
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd

# Configurações do SQLAlchemy
Base = declarative_base()


class Pessoa(Base):
    __tablename__ = 'pessoas'  # Define o nome da tabela no banco de dados
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    sobrenome = Column(String, nullable=False)
    endereco = Column(String, nullable=False)
    numero = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    estado = Column(String, nullable=False)
    cep = Column(String, nullable=False)


# Função para criar a tabela no banco de dados


def criar_db():
    engine = create_engine('sqlite:///pessoas45.db')
    Base.metadata.create_all(engine)
    return engine

# Função para adicionar pessoa ao banco de dados


def adicionar_pessoa(nome, sobrenome, endereco, numero, cidade, estado, cep, engine):
    Session = sessionmaker(bind=engine)
    session = Session()

    nova_pessoa = Pessoa(nome=nome, sobrenome=sobrenome, endereco=endereco, numero=numero,
                         cidade=cidade, estado=estado, cep=cep)
    session.add(nova_pessoa)
    session.commit()
    session.close()

# criar a janela de login


def main(page: ft.Page):

    texto = ft.Text(
        spans=[
            ft.TextSpan(
                "Cadastror de Pessoas",
                ft.TextStyle(
                    size=40,
                    weight=ft.FontWeight.BOLD,
                    foreground=ft.Paint(
                        gradient=ft.PaintLinearGradient(
                            (0, 20), (150, 20), [
                                ft.colors.RED, ft.colors.BLUE_GREY_500]
                        )
                    ),
                ),
            ),
        ],
    )

    page.title = "Cadastro de Pessoas"

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Função para verificar o login

    def verificar_login(e):

        if login.value == senha1 and login1.value == senha2:
            login.value = ""
            login1.value = ""

            page.update()

            # Acessar nova janela se as credenciais estiverem corretas
            page.clean()

            page.controls.append
            # Barra de Rolagem
            page.scroll = "always"
            page.update()
            page.add(textocadastro)

            page.add(nome_input, sobrenome_input, endereço_input, numero_input)
            page.add(cidade_input, estado_input,
                     cep_input, enviar_btn)

            page.add(janeladados, botaosair)

            page.update()

        else:
            login.value = ""
            login1.value = ""

            page.update
            page.clean

            page.add(ft.Text("Login ou senha incorretos"))
            page.update()

            page.add(login, login1, botao1)

            page.update
    # Função para enviar os dados para o banco de dados

    def enviar_dados(e):

        engine = criar_db()  # Cria o banco de dados (se não existir) e retorna o engine

        nome = nome_input.value
        sobrenome = sobrenome_input.value
        endereco = endereço_input.value
        numero = numero_input.value
        cidade = cidade_input.value
        estado = estado_input.value
        cep = cep_input.value
        nome_input.value = ""
        sobrenome_input.value = ""
        endereço_input.value = ""
        numero_input.value = ""
        cidade_input.value = ""
        estado_input.value = ""
        cep_input.value = ""

        if nome and sobrenome and endereco and numero and cidade and estado and cep:

            adicionar_pessoa(nome, sobrenome, endereco, numero,
                             cidade, estado, cep, engine)
            page.snack_bar = ft.SnackBar(

                ft.Text(f" cadastrado concluido com sucesso!"))
            page.snack_bar.open = True
            page.update()

        else:

            page.snack_bar = ft.SnackBar(
                ft.Text("Por favor, preencha todos os campos!"))
            page.snack_bar.open = True
            page.update()
    # Função para sair da tela de cadastro e voltar para a tela de login

    def sair(e):
        page.clean()

        page.add(texto, login, login1, botao1)
        page.update()

    # Função para exibir a tabela de dados

    def tabeladados(e):
        page.clean()
        page.vertical_alignment = ft.MainAxisAlignment.START

        page.add(textodados)
        try:
            dados = pd.read_sql_table('pessoas', 'sqlite:///pessoas45.db')
        except Exception as e:
            page.add(ft.Text(f"Erro ao ler o banco de dados: {e}"))
            return
        dados = dados.to_dict(orient='records')
        dados_filtrados = dados.copy()

        def filtrar_dados(e):
            texto_filtro = campo_filtro.value.lower()
            dados_filtrados.clear()
            if texto_filtro:
                for item in dados:
                    if isinstance(item, dict):  # verifica se item é um dicionario
                        if (
                            texto_filtro in item.get("nome", "").lower()
                            or texto_filtro in str(item.get("sobrenome", "")).lower()
                            or texto_filtro in item.get("endereco", "").lower()
                            or texto_filtro in str(item.get("numero", "")).lower()
                            or texto_filtro in item.get("cidade", "").lower()
                            or texto_filtro in item.get("estado", "").lower()
                            or texto_filtro in item.get("cep", "").lower()
                        ):
                            dados_filtrados.append(item)
            else:
                dados_filtrados.extend(dados)
            atualizar_tabela()
            page.update()

        def atualizar_tabela():
            linhas = []
            for item in dados_filtrados:
                if isinstance(item, dict):
                    linhas.append(
                        ft.DataRow(
                            cells=[
                                ft.DataCell(
                                    ft.Text(str(item.get("nome", "")))),
                                ft.DataCell(
                                    ft.Text(str(item.get("sobrenome", "")))),
                                ft.DataCell(ft.Text(item.get("endereco", ""))),
                                ft.DataCell(
                                    ft.Text(str(item.get("numero", "")))),
                                ft.DataCell(ft.Text(item.get("cidade", ""))),
                                ft.DataCell(ft.Text(item.get("estado", ""))),
                                ft.DataCell(ft.Text(item.get("cep", ""))),
                            ]
                        )
                    )
            dt.rows = linhas
            page.update()

        campo_filtro = ft.TextField(
            label="Filtrar",
            on_change=filtrar_dados,
            expand=True,
            width=400,
        )
        dt = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Nome")),
                ft.DataColumn(ft.Text("sobrenome")),
                ft.DataColumn(ft.Text("Endereco")),
                ft.DataColumn(ft.Text("Numero")),
                ft.DataColumn(ft.Text("Cidade")),
                ft.DataColumn(ft.Text("Estado")),
                ft.DataColumn(ft.Text("Cep")),
            ],
            rows=[],
            expand=True
        )
        atualizar_tabela()
        page.add(
            ft.Column(
                [
                    campo_filtro,
                    ft.Container(dt, expand=True),
                ],
                expand=True
            )
        )

        page.add(botaovoltar)
        page.scroll = "always"

        page.update()

    def Voltar(e):
        page.clean()
        page.add(textocadastro)
        page.add(nome_input, sobrenome_input, endereço_input, numero_input)
        page.add(cidade_input, estado_input,
                 cep_input, enviar_btn, botaosair)

        page.add(janeladados)
        page.update()

    login = ft.TextField(label="login", width=500)
    login1 = ft.TextField(label="senha", width=500,
                          password=True, can_reveal_password=True)
    botao1 = ft.CupertinoFilledButton(text="Acessar", on_click=verificar_login)
    senha1 = "Renato123"
    senha2 = "123456"
    nome_input = ft.TextField(label="Nome", width=400)
    sobrenome_input = ft.TextField(label="Sobrenome", width=400)
    enviar_btn = ft.TextButton(text="cadastrar", on_click=enviar_dados)
    botaosair = ft.TextButton(text="sair", on_click=sair)
    endereço_input = ft.TextField(label="endereço", width=400)
    numero_input = ft.TextField(label="numero", width=400)
    cidade_input = ft.TextField(label="cidade", width=400)
    estado_input = ft.TextField(label="estado", width=400)
    cep_input = ft.TextField(label="cep", width=400)
    janeladados = ft.TextButton(text="Dados", on_click=tabeladados)
    botaovoltar = ft.TextButton(text="Voltar", on_click=Voltar)
    textodados = ft.Text("Dados Cadastrados", size=80,
                         color=ft.colors.LIGHT_GREEN_ACCENT_400)
    textocadastro = ft.Text("Cadastro de Pessoas", size=80,
                            color=ft.colors.LIGHT_BLUE_ACCENT, italic=True)

    page.add(texto, login, login1, botao1)


if __name__ == '__main__':
    ft.app(target=main)
