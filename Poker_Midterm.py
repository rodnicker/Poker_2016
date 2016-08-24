# -*- coding: utf-8 -*-

from pokerdeck import *
from random import choice, shuffle

#ranks = [str(n) for n in range(2, 11)] + list('JQKA')
#suits = '♥ ♦ ♣ ♠'.split()
#suits = 'spades diamonds clubs hearts'.split()

deck = PokerDeck()

shuffle(deck)

myCard = choice(deck)

#print(myCard)
#print(myCard.rank)
theCard = Card(rank='K', suit='♥')

#print(theCard.rank, theCard.suit)

hand = []
#hand.append(Card(rank='A',suit='♥'))
#hand.append(Card(rank='A',suit='♠'))
#hand.append(Card(rank='2',suit='♠'))
#hand.append(Card(rank='2',suit='♣'))
def deal_hand():
    while len(hand) <5:
        card = choice(deck)
        deck.remove(card)
        hand.append(card)
    return hand

hand = deal_hand()
#for _ in range(5):
#    hand.append(choice(deck))
    
for card in hand:
    print(card)  
        
ranks = []
suits = '♥ ♦ ♣ ♠'.split()
for card in hand:
    ranks.append(card.rank)

    
def find_pairs(ranks):
    pairs = []
    for card in ranks:
        if ranks.count(card) == 2 and card not in pairs:
            pairs.append(card)
    if len(pairs) >0 and len(pairs) <2:
        print('You have a pair: ', pairs)
    elif len(pairs) == 2:
        print('You have two pair: ', pairs)
find_pairs(ranks)

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
find_set(ranks)                

def find_four(ranks):
    four_kind = set()
    for card in ranks:
        if ranks.count(card) == 4:
            four_kind.add(card)
        if len(four_kind) == 1:
            print('You have 4 of a kind: ', four_kind) 
find_four(ranks)

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
find_fullhouse(ranks)
          
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
    if ranks[4] - ranks[0] == 4:
        print('You have a strait!')
        return True
find_strait(ranks)           
        
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
    if ranks[4] - ranks[0] == 4 and suits.count(suits[0]) == 5:
        return True
find_straitFlush(ranks, suits)        

#if __name__ == '__main__':
#    deck = PokerDeck()
#    shuffle(deck)
#    hand = deal_hand()

            
  
  



       













    
'''    rank_list = []
    
    for card in hand:
        rank_list.append(card.rank)
    print(rank_list)
     
    def find_twoPairs(rank_list):    
        for rank in rank_list:
            if rank_list.count(rank) +- 1 :
                print('You have two pair')
                break
            else:
                return False
            return True
        
    def find_pairs(rank_list):    
        for rank in rank_list:
            if rank_list.count(rank) == 2:
                print('You have a pair')
                break
            else:
                return False
            return True
        
    def find_set(rank_list):    
        for rank in rank_list:
            if rank_list.count(rank) == 3:
                print('You have 3 of a kind')
                break
            else:
                return False
            return True'''




#print(find_set(rank_list))    
#print(find_twoPairs(rank_list))    
#print(find_pairs(rank_list))