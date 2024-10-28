import random

def jogar():
    print("Bem-vindo ao jogo de Adivinhação!")
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    while not acertou:
        try:
            chute = int(input("Digite um número entre 1 e 100: "))
            tentativas += 1
            
            if chute < 1 or chute > 100:
                print("Por favor, escolha um número entre 1 e 100.")
                continue

            if chute < numero_secreto:
                print("Tente um número maior!")
            elif chute > numero_secreto:
                print("Tente um número menor!")
            else:
                print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
                acertou = True
        except ValueError:
            print("Por favor, digite um número válido.")

if __name__ == "__main__":
    jogar()
