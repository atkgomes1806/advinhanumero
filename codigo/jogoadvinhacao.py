import random  # Importa o módulo random

def guess_number():
    print("Bem-vindo ao jogo 'Teste de Adivinhação Numérica'!")

    # Confirma se o jogador quer jogar
    play = input("Você quer jogar? (s/n): ").strip().lower()
    if play != 's':
        print("Obrigado! Até a próxima.")
        return

    # Pergunta o número de tentativas
    while True:
        try:
            attempts = int(input("Quantas tentativas você quer? (mínimo 3, máximo 10): "))
            if 3 <= attempts <= 10:
                break
            else:
                print("Por favor, escolha um número entre 3 e 10.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro.")

    # Gera um número aleatório entre 1 e 100
    number_to_guess = random.randint(1, 100)
    
    # Define multiplicador baseado no número de tentativas
    multiplier = (11 - attempts) * 0.5  # 3 tentativas = 4x, 10 tentativas = 0.5x
    score = int(100 * multiplier)  # Pontuação inicial ajustada
    
    print(f"Adivinhe o número entre 1 e 100. Você tem {attempts} tentativas.")
    print(f"Multiplicador de pontos: {multiplier}x (menos tentativas = mais pontos)")

    for attempt in range(attempts):
        try:
            # Solicita a entrada do usuário e converte para inteiro
            guess = int(input(f"Tentativa {attempt + 1}: "))

            if guess == number_to_guess:
                print("Parabéns! Você acertou o número.")
                print(f"Sua pontuação: {score} pontos.")
                break
            else:
                # Calcula a diferença e fornece feedback
                difference = abs(guess - number_to_guess)
                feedback = "muito perto" if difference <= 10 else "perto" if difference <= 20 else "muito longe"
                direcao = "mais alto" if guess < number_to_guess else "mais baixo"
                
                print(f"Você está {feedback}!")
                print(f"O número correto é {direcao}.")

            # Reduz a pontuação considerando o multiplicador
            score -= int((100 * multiplier) // attempts)
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro.")
            continue
    else:
        print(f"Desculpe, você usou todas as suas tentativas. O número correto era {number_to_guess}.")
        print("Sua pontuação: 0 pontos.")

while True:
    guess_number()
    play_again = input("Quer jogar novamente? (s/n): ").strip().lower()
    if play_again != 's':
        print("Obrigado por jogar! Até a próxima.")
        break
