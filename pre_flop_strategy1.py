# -*- coding: utf-8 -*-

state = {u'community_cards': [], u'minimum_raise': 10, u'small_blind': 10, u'pot': 30, u'orbits': 0, u'players': [{u'status': u'active', u'hole_cards': [{u'rank': u'J', u'suit': u'spades'}, {u'rank': u'A', u'suit': u'diamonds'}], u'name': u'Peter Python', u'id': 0, u'version': u'Default Python folding player', u'stack': 980, u'bet': 20}, {u'status': u'folded', u'name': u'Peter P2', u'stack': 1000, u'version': u'Default Python folding player', u'id': 1, u'bet': 0}, {u'status': u'folded', u'name': u'Peter P3', u'stack': 1000, u'version': u'Default Python folding player', u'id': 2, u'bet': 0}, {u'status': u'folded', u'name': u'Peter P4', u'stack': 990, u'version': u'Default Python folding player', u'id': 3, u'bet': 10}], u'in_action': 0, u'dealer': 2, u'current_buy_in': 20}

class Strategy(object):

    # returns with the raise amount for preflop state
    def doPreFlop(self):
        #cards = self.getOurCards()
        #ranks = self.getRanks(cards)
        ranks = "A9"   # for test only
        print "card ranks: " + ranks

        # rule 1 - 4
        if (ranks == "AA" or ranks == "KK" or ranks == "QQ" or ranks == "JJ"):
            print "all in AA: " + str(self.getAllin())
            return self.getAllin()

        # rule 3 AK
        if (ranks == "AK"):
            print "all in AK: " + str(self.getAllin())
            return self.getAllin()

        # rule 5 - 6: one pair or high cards
        if (ranks == "TT" or ranks == "99" or ranks == "88" or ranks == "77"
            or ranks == "66" or ranks == "55" or ranks == "44" or ranks == "33" or ranks == "22"
            or ranks == "AQ" or ranks == "AJ" or ranks == "KQ"):
            print "6 x small blind: " + str(6 * self.getSmallBlind())
            return 6 * self.getSmallBlind()


        return 0

    def getOurPlayer(self):
        pos = self.getPosition()
        print "our position: " + str(pos)
        players = state['players']
        player = players[pos]
        print "player: " + str(player)
        return player

    def getSmallBlind(self):
        print "small blind: " + str(state['small_blind'])
        return state['small_blind']

    # returns the stack of our player
    def getAllin(self):
        player = self.getOurPlayer()
        print "all in: " + str(player['stack'])
        return player['stack']

    def getRanks(self, cards):
        ranks = ""
        for card in cards:
            ranks = ranks + card['rank']
        return ''.join(sorted(ranks))

    def getOurCards(self):
        player = self.getOurPlayer()
        cards = player['hole_cards']
        print "cards at me: " + str(cards)
        return cards

    def getPosition(self):
        return state['in_action']


s = Strategy()
s.doPreFlop()
