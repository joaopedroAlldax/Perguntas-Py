class Port:
    def __init__(self):
        print("0 - ambiguo | 1 - diesel | 2 - entreterimento | 3 - praticidade")
        self.pergunta = int(input("Informe qual dessas palavras possuem acentuação: "))

    def pergunta_acento(self):
        
        if self.pergunta == '':
            
                print("Insira o numero")
        else:
            if type(self.pergunta)== int:
                if self.pergunta == 0:
                    print ("Resposta correta")
                elif self.pergunta == 1:
                    print ("Resposta incorreta")
                elif self.pergunta == 2:
                    print ("Resposta incorreta")
                elif self.pergunta == 3:
                    print ("Resposta incorreta")

                else:
                    print(self.pergunta)


if __name__ == "__main__":
    port = Port()
    port.pergunta_acento()


