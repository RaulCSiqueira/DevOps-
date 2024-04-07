import random

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(hand):
  if sum(hand) == 21 and len(hand) == 2:
    return 0
  if 11 in hand and sum(hand) > 21:
    hand.remove(11)
    hand.append(1)
  return sum(hand)

def blackjack():
  user_cards = []
  computer_cards = []
  game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print("Suas cartas: ", user_cards, ", pontuação atual: ", user_score)
    print("Carta inicial do computador: ", computer_cards[0])

    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      should_continue = input("Digite 'y' para receber outra carta, 'n' para passar: ")
      if should_continue == 'y':
        user_cards.append(deal_card())
      else:
        game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print("Suas cartas finais: ", user_cards, ", pontuação final: ", user_score)
  print("Cartas finais do computador: ", computer_cards, ", pontuação final: ", computer_score)

  if user_score > 21:
    return "Você perdeu 😭"
  elif computer_score > 21:
    return "Você ganhou 🥳"
  elif user_score == computer_score:
    return "Empate 🙃"
  elif user_score == 0:
    return "Ganhou com um Blackjack 😎"
  elif computer_score == 0:
    return "Perdeu, oponente tem Blackjack 😱"
  elif user_score > computer_score:
    return "Você ganhou 🥳"
  else:
    return "Você perdeu 😭"

print(blackjack())
