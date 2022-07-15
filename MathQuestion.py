
class Math:
    def __init__(self):
        self.pergunta = input("Escreva todos os dez primeiros numeros primos em sequencia: (1, 2, 3)")

    def pergunta_primos(self):
        lista_pergunta = []
        self.pergunta = self.pergunta.split(',')
        for i in self.pergunta:
            lista_pergunta.append(int(i.replace(' ', '')))
        if lista_pergunta == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
            print("Resposta correta")
        else:
            print ("Você errou, tente novamente")

if __name__=="__main__":
    math = Math() 
    math.pergunta_primos()
