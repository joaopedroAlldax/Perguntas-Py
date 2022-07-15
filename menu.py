from MathQuestion import Math
from PortQuestion import Port

class Menu:
    def __init__(self):
        self.questao1 = Math()
        self.questao1.pergunta_primos()
        self.questao2 = Port()
        self.questao2.pergunta_acento()
    
if __name__ == '__main__':
    menu = Menu()



