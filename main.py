import random 


num = int(input("Input the number of credit cards that you want: "))
cards = []


while len(cards) < num :

  test = random.randint(1000000000000000,9999999999999999)
  card = str(test)
  digit_sum = 0

  for i, digit in enumerate(reversed(card)):
      n = int(digit)

      if i % 2 == 0:
          digit_sum += n
      elif n >= 5:
          digit_sum += n * 2 - 9
      else:
          digit_sum += n * 2

  if digit_sum % 10 == 0:
      cards.append(card)
      testing = False

print(cards)