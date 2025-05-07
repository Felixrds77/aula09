
class NomeClasse:
    def __init__(self, nome, idade, peso, dormindo, andando):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.dormindo = dormindo
        self.andando = andando
    def comprimentar (self):
        print( f"falou que seu nome é {self.nome}")
    def aniversario (self):
        print( f"e completou {self.idade} Anos ontem")
    def comer (self,comida):
        if self.dormindo == True :
            print(f"mas tentou comer em quanto dorme, precisa acordar")
        else:
            print( f"e comeu um {comida} para comemorar")
    def dormir (self):
        if self.dormindo == True:
            print(f"{self.nome} já está dormindo")
        else:
            print(f"{self.nome} foi dormir")
    def andar (self):
        if self.andando == True:
            print(f"{self.nome} já está andando")
        elif self.dormindo:
            print(f"{self.nome} está dormindo e não pode andar")
        else:
            print(f"{self.nome} pode andar")
