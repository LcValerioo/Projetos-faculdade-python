class Pessoa:
    def __init__(self, cpf, nome, data_nascimento, usa_oculos):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.usa_oculos = usa_oculos
        self.veiculos = []

class Marca:
    def __init__(self, id, nome, sigla):
        self.id = id
        self.nome = nome
        self.sigla = sigla

class Veiculo:
    def __init__(self, placa, ano, cor, motor, proprietario, marca):
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.motor = motor
        self.proprietario = proprietario
        self.marca = marca


class Livro:
    def __init__(self, titulo, autor, preco):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco

class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Pedido:
    def __init__(self, cliente_id, livro_id, quantidade, data_pedido):
        self.cliente_id = cliente_id
        self.livro_id = livro_id
        self.quantidade = quantidade
        self.data_pedido = data_pedido