#Declaração d classe
class Vini:
    def __init__(self): #Método-construtor
        #atributo de instancia
        self.nome = ''
        self.idade = 0


        #Metodo de instancia
    def aniversario(self):
        self.idade = self.idade + 1


    def msg(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade"


# Declaração de objeto
g1 = Vini()
g1.nome = 'Maria'
g1.idade = 20
print(g1.msg())
