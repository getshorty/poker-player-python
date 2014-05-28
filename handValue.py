__author__ = 'nberenyi'
import random

class HandValue(object):
    def __init__(self, cards):
        self.cards = cards
        self.card1 = cards[0]
        self.card2 = cards[1]
        self.card3 = cards[2]
        self.card4 = cards[3]

    def getValue(self):
        if self.card1['rank'] == 'A' and self.card2['rank'] == 'A':
            return 100
        if self.card1['rank'] == 'A' and self.card2['rank'] == 'K':
            return 98
        if self.card1['rank'] == 'A' and self.card2['rank'] == 'Q':
            return 97
        if self.card1['rank'] == 'A' and self.card2['rank'] == 'J':
            return 95
        if self.card1['rank'] == 'K' and self.card2['rank'] == 'K':
            return 99
        if self.card1['rank'] == 'K' and self.card2['rank'] == 'A':
            return 98
        if self.card1['rank'] == 'K' and self.card2['rank'] == 'Q':
            return 93
        if self.card1['rank'] == 'K' and self.card2['rank'] == 'J':
            return 92
        if self.card1['rank'] == 'Q' and self.card2['rank'] == 'Q':
            return 96
        if self.card1['rank'] == 'Q' and self.card2['rank'] == 'A':
            return 97
        if self.card1['rank'] == 'Q' and self.card2['rank'] == 'K':
            return 93
        if self.card1['rank'] == 'Q' and self.card2['rank'] == 'J':
            return 91
        if self.card1['rank'] == 'J' and self.card2['rank'] == 'J':
            return 90
        if self.card1['rank'] == 'J' and self.card2['rank'] == 'A':
            return 95
        if self.card1['rank'] == 'J' and self.card2['rank'] == 'K':
            return 92
        if self.card1['rank'] == 'J' and self.card2['rank'] == 'Q':
            return 94
        if self.card1['rank'] == self.card2['rank'] and (self.card1['rank'] == 'T' or self.card1['rank'] == '9'):
            return 90
        if self.card1['rank'] == self.card2['rank']:
            return 100
        if self.card1['rank'] in ["A", "K"] and self.card2['rank'] in ["T","9","8","7","6","5"]:
            return 81
        if self.card2['rank'] in ["A", "K"] and self.card1['rank'] in ["T","9","8","7","6","5"]:
            return 81
        if self.card1['rank'] in ["Q", "J"] and self.card2['rank'] in ["T","9","8","7","6","5"]:
            return 79
        if self.card2['rank'] in ["Q", "J"] and self.card1['rank'] in ["T","9","8","7","6","5"]:
            return 79
        return 0



if __name__ == "__main__":
    for x in range(0, 200):
        hv3 =HandValue([{u'rank': u''+random.choice("AKQJT98765432")+'', u'suit': u'spades'}, {u'rank': u''+random.choice("AKQJT98765432")+'', u'suit': u'diamonds'}, {u'rank': u''+random.choice("AKQJT98765432")+'', u'suit': u'diamonds'}, {u'rank': u''+random.choice("AKQJT98765432")+'', u'suit': u'diamonds'}])
        if hv3.getValue() > 78:
            #print "#",x,hv3.card1['rank'],hv3.card2['rank'],hv3.card3['rank'],hv3.card4['rank'], "Return:", hv3.getValue()
            print "#",x,hv3.card1['rank'],hv3.card2['rank'], "Return:", hv3.getValue()
