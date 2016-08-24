# -*- coding: utf-8 -*-

from pokerdeck import *
from random import choice, shuffle


def deal_hand():
    hand = []
    deck = PokerDeck()
    shuffle(deck)
    while len(hand) <5:
        card = choice(deck)
        deck.remove(card)
        hand.append(card)
    return hand   
   
    
def find_pairs(ranks):
    pairs = []
    for card in ranks:
        if ranks.count(card) == 2 and card not in pairs:
            pairs.append(card)
    if len(pairs) >0 and len(pairs) <2:
        print('You have a pair: ', pairs)
    elif len(pairs) == 2:
        print('You have two pair: ', pairs)


def find_set(ranks):
    three_kind = set()    
    for card in ranks:  
        if ranks.count(card) == 3:
            three_kind.add(card)
    if len(three_kind) == 1:   
        print('You have 3 of a kind: ', three_kind)
        return True
    else:
        return False
               

def find_four(ranks):
    four_kind = set()
    for card in ranks:
        if ranks.count(card) == 4:
            four_kind.add(card)
    if len(four_kind) == 1:
        print('You have 4 of a kind: ', four_kind) 


def find_fullhouse(ranks):
    f_h = []
    fullhouse_kind = set()
    for card in ranks:
        if ranks.count(card) == 2 or ranks.count(card) == 3:
            f_h.append(card)
            fullhouse_kind.add(card)
        if len(f_h) == 5:
            print('You have a fullhouse!')
            for card in fullhouse_kind:
                print(card, end = ' ')            
            return True            
        else:
            return False

          
def find_flush(suits):
    if suits.count(suits[0]) == 5:
        print('You have a flush!', find_flush)
        return True
    else:
        return False 


def find_strait(ranks):      
   # strait = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
    for i in range(len(ranks)):
        if ranks[i] == 'J':
            ranks[i] = 11
        elif ranks[i] == 'Q':
            ranks[i] = 12
        elif ranks[i] == 'K':
            ranks[i] = 13
        elif ranks[i] == 'A':
            ranks[i] = 14
        else:
            ranks[i] = int(ranks[i])    
    ranks.sort()
    for rank in ranks:
        if ranks.count(rank) > 1:
            return False
    if ranks[4] - ranks[0] == 4:
        print('You have a strait!')
        return True
         
        
def find_straitFlush(ranks, suits):
    for i in range(len(ranks)):
        if ranks[i] == 'J':
            ranks[i] = 11
        elif ranks[i] == 'Q':
            ranks[i] = 12
        elif ranks[i] == 'K':
            ranks[i] = 13
        elif ranks[i] == 'A':
            ranks[i] = 14
        else:
            ranks[i] = int(ranks[i])
    ranks.sort()
    for rank in ranks:
        if ranks.count(rank) > 1:
            return False       
    if ranks[4] - ranks[0] == 4 and suits.count(suits[0]) == 5:
        return True
      

def main(): 
    
    hand = deal_hand()
    for card in hand:
        print(card)  
    ranks = []
    suits = '♥ ♦ ♣ ♠'.split()          
    for card in hand:
        ranks.append(card.rank)

    find_pairs(ranks)
    find_set(ranks) 
    find_four(ranks)
    find_fullhouse(ranks)
    find_straitFlush(ranks,suits) 
    find_strait(ranks)  
    find_flush(ranks)   

if __name__ == '__main__':
    main()











    
