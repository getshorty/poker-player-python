# -*- coding: utf-8 -*-

state = {u'community_cards': [], u'minimum_raise': 10, u'small_blind': 10, u'pot': 30, u'orbits': 0, u'players': [{u'status': u'active', u'hole_cards': [{u'rank': u'J', u'suit': u'spades'}, {u'rank': u'A', u'suit': u'diamonds'}], u'name': u'Peter Python', u'id': 0, u'version': u'Default Python folding player', u'stack': 980, u'bet': 20}, {u'status': u'folded', u'name': u'Peter P2', u'stack': 1000, u'version': u'Default Python folding player', u'id': 1, u'bet': 0}, {u'status': u'folded', u'name': u'Peter P3', u'stack': 1000, u'version': u'Default Python folding player', u'id': 2, u'bet': 0}, {u'status': u'folded', u'name': u'Peter P4', u'stack': 990, u'version': u'Default Python folding player', u'id': 3, u'bet': 10}], u'in_action': 0, u'dealer': 2, u'current_buy_in': 20}

class Strategy(object):

    def doPreFlop(self):
        cards = self.getCards()
        ranks = self.getRanks(cards)
        print "card ranks: " + ranks

    def getRanks(self, cards):
        ranks = ""
        for card in cards:
            ranks = ranks + card['rank']
        return ''.join(sorted(ranks))

    def getCards(self):
        pos = self.getPosition()
        print "our position: " + str(pos)
        players = state['players']
        player = players[pos]
        print "player: " + str(player)
        cards = player['hole_cards']
        print "cards at me: " + str(cards)
        return cards

    def getPosition(self):
        return state['in_action']


s = Strategy()
s.doPreFlop()
