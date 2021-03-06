# Prog-03: Card Game
# 6???????21 Name ?

import time
import random

def generate_deck(n_cards, n_shuffles):
    print('Shuffle', end='')
    deck = ''
    for suit in 'CDHS':
        for face in 'A23456789TJQK':
            deck += '|' + face + suit + '|'
    for i in range(n_shuffles):
        deck = cut(deck, random.randint(0,n_cards))
        deck = shuffle(deck)
        time.sleep(0.1)
        print('.', end='')
    print()
    return deck[:4*n_cards]

def play(n_cards):
    print('Start a card game.')
    deck = generate_deck(n_cards, 20)

    p1, deck = deal_n_cards(deck, 5)
    p2, deck = deal_n_cards(deck, 5)
    players = [p1, p2]
    
    table_cards, deck = deal_n_cards(deck, 1)
    fail = False
    turn = 0
    
    while True:
        show_table_cards(table_cards, 10)
        show_player_cards(players[turn], turn+1)
        k = select_card_number(players[turn])
        valid = (k != 0)
        if valid:
            cards = players[turn]
            card = peek_kth_card(cards, k)
            valid = eq_suit_or_value(card, table_cards[-4:])
            if valid:
                table_cards += card
                players[turn] = remove_kth_card(cards, k)
                fail = False
        if not valid:
            print('  ** Invalid **')
            if len(deck) == 0:
                if fail: break
                fail = True
            if len(deck) > 0:
                print('  >> get a new card')
                card, deck = deal_n_cards(deck, 1) 
                players[turn] = card + players[turn]
                
        show_player_cards(players[turn], turn+1)
        print(len(players[turn]))
        print(players[turn])
        if len(players[turn]) == 2: break
        turn = (turn + 1) % len(players)

    if len(deck) == 0:
        print('\n** No more cards **')
    print('*****************')
    if len(deck) == 0 and \
         len(players[0]) == len(players[1]):
            print('Draw!!!')
    elif len(players[0]) < len(players[1]):
        print('Player # 1 win!!!')
    else:
        print('Player # 2 win!!!')        

def eq_suit_or_value(card1, card2):
    return card1[1] == card2[1] or \
                 card1[2] == card2[2]

def show_player_cards(cards, k):
    print('  Player #', k, ':', cards)

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            pass

def select_card_number(cards):
    n = len(cards)//4
    k = input_int('  Select card # (1-'+ str(n)+') : ')
    if not(1 <= k <= n): k = 0
    return k

#---------------------------------------
def peek_kth_card(cards, k):
    #print(cards, "1")
    cards = cards[1:len(cards)-1]
    d = cards.split("||")
    the_kth_card = "|"+d[k-1]+"|"

    return the_kth_card
#---------------------------------------
def remove_kth_card(cards, k):
    #print(cards, "2")
    cards = cards[1:len(cards)-1]
    d = cards.split("||")
    d.pop(k-1)
    new_cards = "|" + "||".join(d) + "|"

    return new_cards
#---------------------------------------
def deal_n_cards(deck, n):
    #print(deck, "3")
    deck = deck[1:len(deck)-1]
    d = deck.split("||")
    cards = d[:n]
    new_deck = d[n:]
    if len(new_deck) == 0 or len(cards) == 0:
        new_deck = ""
        cards = ""
        return cards, new_deck
    cards = "|"+ "||".join(cards) + "|"
    new_deck = "|"+"||".join(new_deck)+"|"
    #print(new_deck)

    return cards, new_deck
#---------------------------------------
def cut(deck, m):
    deck = deck[1:len(deck)-1]
    d = deck.split("||")
    d1 = d[m:]
    d2 = d[:m]
    new_deck = d2+d1
    #print(new_deck)
    new_deck = "|" + "||".join(new_deck) + "|"
    return new_deck
#---------------------------------------
def shuffle(deck):
    new_deck = []
    deck = deck[1:len(deck)-1]
    d = deck.split("||")
    half = len(d)//2
    left = d[:half]
    right = d[half:]
    #left = max(left, right)
    #right = min(left, right)
    while True:
        try:
            new_deck.append(left.pop(0))
            new_deck.append(right.pop(0))
        except:
            break
    new_deck = "|" + "||".join(new_deck) + "|"
    #print(new_deck)
    return new_deck
#---------------------------------------
def show_table_cards(cards, m):
#    print(cards, "4")
    print(cards)
    cards = cards[1:len(cards)-1]
    d = cards.split("||")
    if len(d) <= m:
        string = "|" + "||".join(d) + "|"
        print("-"* (7+len(string)))
        print("Table:", string)
        print("-"* (7+len(string)))
    else:
        string = "|" +  "...." + "||".join(d[m:]) + "|"
        print("-"* (7+len(string)))
        print("Table:", string)
        print("-"* (7+len(string)))
    
#-----------------------------------------    
play(51)
