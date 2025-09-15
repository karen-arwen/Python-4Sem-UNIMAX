# Definindo a classe Carro
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca  # Atributo de instância
        self.modelo = modelo  # Atributo de instância
        self.ano = ano  # Atributo de instância

    def exibir_dados(self):
        # Método para exibir os dados do carro
        return f"{self.marca} {self.modelo} ({self.ano})"

# Definindo a classe Comprador
class Comprador:
    def __init__(self, nome, idade, endereco, carro):
        self.nome = nome  # Atributo de instância
        self.idade = idade  # Atributo de instância
        self.endereco = endereco  # Atributo de instância
        self.carro = carro  # Atributo de instância, que será uma instância da classe Carro

    def exibir_dados(self):
        # Método para exibir os dados do comprador e do carro
        print(f"Comprador: {self.nome}, Idade: {self.idade}, Endereço: {self.endereco}")
        print(f"Carro: {self.carro.exibir_dados()}")  # Chama o método exibir_dados da classe Carro

# Criando instâncias da classe Carro
carro1 = Carro("Volkswagen", "Fusca", 1975)
carro2 = Carro("Fiat", "Uno", 1995)
carro3 = Carro("Lamborghini", "Aventador", 2020)
carro4 = Carro("Jaguar", "F-Type", 2021)
carro5 = Carro("Ferrari", "488 Spider", 2019)
carro6 = Carro("Mercedes-Benz", "Classe A", 2020)

# Criando instâncias da classe Comprador e associando um carro a cada comprador
comprador1 = Comprador("João Silva", 30, "Rua das Flores, 123", carro1)
comprador2 = Comprador("Maria Oliveira", 25, "Avenida Brasil, 456", carro2)

# Exibindo os dados dos compradores e seus carros
comprador1.exibir_dados()
print()# Adiciona uma linha em branco para separar
comprador2.exibir_dados()