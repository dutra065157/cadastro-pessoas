# criar a janela de longin
import flet as ft
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configurações do SQLAlchemy
Base = declarative_base()


class Pessoa(Base):
    __tablename__ = 'pessoas'
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
    engine = create_engine('sqlite:///pessoas4.db')
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

# criar a janela de longin


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

    # Definindo alinhamentos e propriedades da janela
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_resizable = False
    page.window_maximized = True

    # Definir login e senha corretos
    def verificar_login(e):
        page.bgcolor = ft.colors.GREEN_200

        if login.value == senha1 and login1.value == senha2:
            login.value = ""
            login1.value = ""

            page.update()

            # Acessar nova janela se as credenciais estiverem corretas

            page.clean()
            page.add(textop2, nome_input, sobrenome_input, endereço_input, numero_input,
                     cidade_input, estado_input, cep_input, enviar_btn, botaovoltar)

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

    def enviar_dados(e):

        engine = criar_db()

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

    def voltar(e):
        page.clean()
        page.add(texto, login, login1, botao1)
        page.update()

    login = ft.TextField(label="login", width=500)
    login1 = ft.TextField(label="senha", width=500,
                          password=True, can_reveal_password=True)
    botao1 = ft.ElevatedButton(text="Acessar", on_click=verificar_login)
    senha1 = "Renato123"
    senha2 = "123456"
    nome_input = ft.TextField(label="Nome", width=400,
                              bgcolor=ft.colors.YELLOW_800)
    sobrenome_input = ft.TextField(label="Sobrenome", width=400)
    enviar_btn = ft.ElevatedButton(text="cadastrar", on_click=enviar_dados)
    botaovoltar = ft.ElevatedButton(text="Voltar", on_click=voltar)
    endereço_input = ft.TextField(label="endereço", width=400)
    numero_input = ft.TextField(label="numero", width=400)
    cidade_input = ft.TextField(label="cidade", width=400,
                                prefix_icon=ft.icons.COLOR_LENS)
    estado_input = ft.TextField(label="estado", width=400)
    cep_input = ft.TextField(label="cep", width=400)
    textop2 = ft.Text("Cadastra", size=80, color=ft.colors.GREEN,
                      weight="bold")

    # Texto de erro

    page.add(texto, login, login1, botao1)


if __name__ == '__main__':
    ft.app(target=main)
