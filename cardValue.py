__author__ = 'nberenyi'

class CardValue(object):
    def __init__(self, cards):
        self.cards = cards
        self.card1 = cards[0]
        self.card2 = cards[1]

    def getValue(self):
        if self.card1['rank'] == 'A' and self.card2['rank'] == 'A':
            return 100
        return 0


hv =CardValue([{u'rank': u'J', u'suit': u'spades'}, {u'rank': u'A', u'suit': u'diamonds'}, {u'rank': u'4', u'suit': u'diamonds'}, {u'rank': u'3', u'suit': u'diamonds'}, {u'rank': u'2', u'suit': u'diamonds'}])
print hv.getValue()
