# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 17:40:27 2016

@author: rodney.rietcheck
"""

from Poker_Midterm_test import *
from pokerdeck import *

def test_deal_hand():
    assert(len(deal_hand()) == 5)
    
def test_no_dupes():
    hand = deal_hand()
    for card in hand:
        assert hand.count(card) == 1
        
# pair_hand = [Card('9', '♦'), Card('9', '♥'), Card('4', '♠'), Card('J', '♠'), Card('Q', '♠')]
# no_pair_hand = [Card('8', '♦'), Card('9', '♥'), Card('4', '♠'), Card('J', '♠'), Card('Q', '♠')]


def test_find_pairs():
    pairs = ['8', '8', '6', '5', '4']
    two_pairs = ['8', '8', '6', '6', '5']
    pairs_set = set()
    two_pairs_set = set()
    for card in pairs:
        if pairs.count(card) == 2:
            pairs_set.add(card)
    assert len(pairs_set) == 1
    for card in two_pairs:
        if two_pairs.count(card) == 2:
            two_pairs_set.add(card)
    assert len(two_pairs_set) == 2
#    len(pairs) == 2
#   assert find_pairs(pairs) == ['8', 'K', 'K', '4', 'J']
#    assert find_len(pairs) == 2

def test_find_set():
    three_kind = [Card('K', '♦'), Card('K', '♥'), Card('K', '♠'), Card('J', '♠'), Card('4', '♠')]
    assert find_set(['K', 'K', 'K', 'J', '4']) == True

def test_find_four():
    four_kind = [Card('K', '♦'), Card('K', '♥'), Card('K', '♠'), Card('K', '♣'), Card('4', '♠')]
    assert find_four(['K', 'K', 'K', 'K', '4']) == True

def test_find_fullhouse():
    f_h = ()
    fullhouse_kind = [Card('K', '♦'), Card('K', '♥'), Card('K', '♠'), Card('4', '♥'), Card('4', '♠')]
    assert find_fullhouse(['K', 'K', 'K', '4', '4']) == True
    
def test_find_flush():
    suits = [Card('8', '♥'), Card('K', '♥'), Card('Q', '♥'), Card('J', '♥'), Card('4', '♥')]
    assert find_flush(['♥', '♥', '♥', '♥', '♥']) == True  
   
def test_find_strait():
    strait_kind = [Card('6', '♦'), Card('2', '♥'), Card('3', '♠'), Card('4', '♠'), Card('5', '♠')]
    assert find_strait(['2', '3', '4', '5', '6']) == True
    
def test_find_straitFlush():
    ranks = ['10', 'J', 'Q', 'K', 'A']
    suites = ['♠', '♠', '♠', '♠', '♠']
    assert find_straitFlush(ranks, suites) == True
    
#def test_ranks():
#    ranks = [('J', '11'), ('Q', '12'), ('K', '13'), ('A', '14')]
#    assert ranks() == ['11', '12', '13', '14']
    


    
