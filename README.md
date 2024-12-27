Este projeto demonstra a criação de um aplicativo desktop de cadastro de pessoas utilizando a biblioteca Flet, que permite o desenvolvimento rápido de interfaces gráficas multiplataforma com Python, inspiradas no Flutter. O aplicativo oferece uma interface amigável para o usuário realizar o login, cadastros, visualização de dados e gerenciado pelo DB Browser for SQLite.

Funcionalidades Principais:

Tela de Login: Autenticação de usuários com validação de credenciais,senha criada por usuario.
Cadastro de Pessoas: Formulário interativo para inserir informações como nome, sobrenome, endereço, com validação de campos.
Armazenamento de Dados: 
Persistência dos dados cadastrados em um banco de dados SQLite local, garantindo a integridade e disponibilidade das informações.
Visualização de Dados:
Listagem e detalhamento dos registros cadastrados, permitindo a consulta e a gestão das informações.
Interface Interativa:
Utilização de componentes Flet como botões, campos de texto, tabelas e caixas de diálogo para uma experiência de usuário rica e intuitiva.
Aplicativo Desktop:
Empacotamento do aplicativo para distribuição em diferentes sistemas operacionais (Windows, macOS, Linux) usando PyInstaller.
Bibliotecas Utilizadas:
Flet: Framework Python para criação de interfaces gráficas multiplataforma.
DB Browser for SQLite: Ferramenta para gerenciamento e visualização do banco de dados SQLite.
Pandas: Biblioteca para manipulação e análise de dados, utilizada para formatar e exibir os dados na interface.
PyInstaller: Utilitário para empacotar o aplicativo Python em um executável único.
