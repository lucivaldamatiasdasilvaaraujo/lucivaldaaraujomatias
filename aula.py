def boasVidas(nome, idade):
    print("Ola {},nem parece que voce tem{}anos.".format(nome,idade))

if __name__== "__main__":
    nome= input("Qual seu nome? ")
    idade = int(input("Qual sua idade?"))                        
    boasVidas (nome,idade)