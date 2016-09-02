# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 17:40:27 2016

@author: rodney.rietcheck
"""

from Poker_Midterm import *
from pokerdeck import *

def test_deal_hand():
    assert(len(deal_hand()) == 5)
    
def test_no_dupes():
    hand = deal_hand()
    for card in hand:
        assert hand.count(card) == 1
        
# pair_hand = [Card('9', '♦'), Card('9', '♥'), Card('4', '♠'), Card('J', '♠'), Card('Q', '♠')]
# no_pair_hand = [Card('8', '♦'), Card('9', '♥'), Card('4', '♠'), Card('J', '♠'), Card('Q', '♠')]
def test_find_flush():
    suits = [Card('8', '♥'), Card('K', '♥'), Card('K', '♥'), Card('J', '♥'), Card('4', '♥')]
    assert find_flush(suits) == ['♥', '♥', '♥', '♥', '♥']

def test_find_pairs():
    pairs = [Card('8', '♦'), Card('K', '♥'), Card('K', '♠'), Card('J', '♠'), Card('4', '♠')]
    assert find_ranks(pairs) == ['8', 'K', 'K', '4', 'J']
    assert find_len(pairs) == 2

def test_find_set():
    three_kind = [Card('K', '♦'), Card('K', '♥'), Card('K', '♠'), Card('J', '♠'), Card('4', '♠')]
    assert find_set(ranks) == ['K', 'K', 'K', 'J', '4']

def test_find_four():
    four_kind = [Card('K', '♦'), Card('K', '♥'), Card('K', '♠'), Card('K', '♣'), Card('4', '♠')]
    assert find_four(ranks) == ['K', 'K', 'K', 'K', '4']

def test_find_fullhouse():
    fullhouse_kind = [Card('K', '♦'), Card('K', '♥'), Card('K', '♠'), Card('4', '♥'), Card('4', '♠')]
    assert find_fullhouse(ranks) == ['K', 'K', 'K', '4', '4']
    
def test_find_strait():
    strait_kind = [Card('6', '♦'), Card('2', '♥'), Card('3', '♠'), Card('4', '♠'), Card('5', '♠')]
    assert find_strait(ranks) == ['2', '3', '4', '5', '6']
    
def test_find_straitFlush():
    straitFlush_kind = [Card('10', '♠'), Card('J', '♠'), Card('Q', '♠'), Card('K', '♠'), Card('A', '♠')]
    assert find_straitFlush(ranks, suits) == ['10', '♠', 'J', '♠', 'Q', '♠', 'K', '♠', 'A', '♠']

def test_ranks():
    ranks_kind = [Card('10', '10'), Card('J', '11'), Card('Q', '12'), Card('K', '13'), Card('A', '14')]
    assert find_ranks[i] == ['10', '11', '12', '13', '14']


    
