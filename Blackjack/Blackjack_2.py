import random
import os

#Return the sum of the hand
def calc_hand(hand):
	sum = 0

	non_aces = [card for card in hand if card != 'A']
	aces = [card for card in hand if card == 'A']

	for card in non_aces:
		if card in 'JQK':
			sum += 10
		else:
			sum += int(card)

	for card in aces:
		if sum <= 10:
			sum += 11
		else:
			sum += 1

	return sum

#Cards deck
cards = [
	'2','3','4','5','6','7','8','9','10','J','Q','K','A',
	'2','3','4','5','6','7','8','9','10','J','Q','K','A',
	'2','3','4','5','6','7','8','9','10','J','Q','K','A',
	'2','3','4','5','6','7','8','9','10','J','Q','K','A',
]

random.shuffle(cards)

dealer = []
player_1 = []
player_2 = []

player_1.append(cards.pop()) #Put one item into the player list
player_2.append(cards.pop()) 
dealer.append(cards.pop())
player_1.append(cards.pop())
player_2.append(cards.pop())
dealer.append(cards.pop())

standing = [False, False]
first_hand = [True, True]
player_busted = [False, False]

while True:
	os.system('cls' if os.name == 'nt' else 'clear')

	player_score = [calc_hand(player_1), calc_hand(player_2)]
	dealer_score = calc_hand(dealer)

	if standing[0] and standing[1]:
		print('Dealer Cards : [{}] ({})'.format(']['.join(dealer), dealer_score))
	else:
		print('Dealer Cards : [{}][?]'.format(dealer[0]))

	print('Player 1 Cards : [{}] ({})'.format(']['.join(player_1), player_score[0]))
	print('Player 2 Cards : [{}] ({})'.format(']['.join(player_2), player_score[1]))
	print('')

	if standing[0] and standing[1]:
		if player_busted[0] == False:
			if dealer_score > 21:
				print('(Player 1) Dealer Busted, You Win !')
			elif player_score[0] == dealer_score:
				print('(Player 1) Push, nobody wins or loses')
			elif player_score[0] > dealer_score:
				print('(Player 1) You Win !')
			elif player_score[0] < dealer_score:
				print('(Player 1) You Lose :(')
		if player_busted[0]:
			print('(Player 1) You busted! Game Over!')
		if player_busted[1] == False:
			if dealer_score > 21:
				print('(Player 2) Dealer Busted, You Win !')
			elif player_score[1] == dealer_score:
				print('(Player 2) Push, nobody wins or loses')
			elif player_score[1] > dealer_score:
				print('(PLayer 2) You Win !')
			elif player_score[1] < dealer_score:
				print('(Player 2) You Lose :(')
		if player_busted[1]:
			print('(Player 2) You busted! Game Over!')
		break



	if first_hand[0] and player_score[0] == 21:
		print('(Player 1) BlackJack !')
		standing[0] = True

	# first_hand_1 = False

	if first_hand[1] and player_score[1] == 21:
		print('(Player 2) BlackJack !')
		standing[1] = True

	if first_hand and player_score == [21, 21]:
		break

	if player_score[0] > 21:
		print('(Player 1) You busted! Game Over!')
		standing[0] = True
		player_busted[0] = True
		
	if player_score[1] > 21:
		print('(Player 2) You busted! Game Over!')
		standing[1] = True
		player_busted[1] = True
		
	if player_score[0] > 21 and player_score[1] > 21:
		break

	if standing[0] == False:
		print('(Player 1) What would you like to do ?')
		print(' [1] Hit')
		print(' [2] Stand')

		print('')
		choice_player_1 = input('(Player 1) Your Choice: ')
		print('')

		if choice_player_1 == '1':
			player_1.append(cards.pop())
			first_hand[0] = False
		elif choice_player_1 == '2':
			standing[0] = True

	if standing[1] == False:
		print('(Player 2) What would you like to do ?')
		print(' [1] Hit')
		print(' [2] Stand')

		print('')
		choice_player_2 = input('(Player 2) Your Choice: ')
		print('')

		if choice_player_2 == '1':
			player_2.append(cards.pop())
			first_hand[1] = False
		elif choice_player_2 == '2':
			standing[1] = True

	print('Standing Player 1 : {}'.format(standing[0]))
	print('Standing Player 2 : {}'.format(standing[1]))

	if standing[0] and standing[1]:
			while calc_hand(dealer) <= 16:
				dealer.append(cards.pop())


