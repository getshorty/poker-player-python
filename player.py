import ConfigParser

config = ConfigParser.ConfigParser()
config.read("config.ini")

version = config.getint("basic", "version")


class Player:
    VERSION = "GetShorty version " + str(version)

    def betRequest(self, game_state):
        global version

        if version == 6:
            try:
                players = game_state['players']
                if players is not None or len(players) > 2:
#                    from pre_flop_strategy1_v4 import Strategy
                    from pre_flop_strategy1 import Strategy
                    s = Strategy()
                    return s.do(game_state)
                else:
                    from headsUp import HeadsUp
                    hu = HeadsUp()
                    in_action_num = game_state[u'in_action']
                    in_action = game_state[u'players'][in_action_num]
                    hand = in_action['hole_cards']
                    stack = in_action['stack']
                    return hu.do(hand, stack)

            except:
                version = 4

        if version == 5:
            try:
                in_action_num = game_state[u'in_action']
                in_action = game_state[u'players'][in_action_num]
                cards = in_action['hole_cards']
                stack = in_action['stack']
                smallBlind = game_state['small_blind']
                pot = game_state['pot']

                commonCards = game_state['community_cards']
                if commonCards is None or len(commonCards) == 0:
                    from handValue import HandValue

                    hv = HandValue(cards)

                    if hv > 95:
                        return stack
                    elif hv > 90 and stack <= smallBlind * 8:
                        return smallBlind * 6
                    elif hv > 80 and stack <= smallBlind * 4:
                        return smallBlind * 4
                    elif hv > 70 and stack <= smallBlind * 2:
                        return smallBlind * 2
                    else:
                        return 5

                else:
                    from cardValue import CardValue
                    downValue = CardValue(commonCards)

                    allCards = list(commonCards)
                    allCards.extend(cards)
                    allValue = CardValue(allCards)

                    if allValue >= downValue*2:
                        return stack
                    else:
                        return 0

            except:
                version = 4

        if version == 4:
            try:
                from pre_flop_strategy1_v4 import Strategy
                s = Strategy()
                return s.do(game_state)
            except:
                version = 3

        if version == 3:
            try:
                from handValue import HandValue
                in_action_num = game_state[u'in_action']
                in_action = game_state[u'players'][in_action_num]
                cards = in_action['hole_cards']
                stack = in_action['stack']
                smallBlind = game_state['small_blind']

                hv = HandValue(cards)

                if hv.getValue() >= 90:
                    return stack / 2
                elif hv.getValue() >= 80:
                    return smallBlind * 6
                else:
                    return 0
#                    return smallBlind * 2
            except:
                version = 2
        if version < 3:
            in_action_num = game_state[u'in_action']
            in_action = game_state[u'players'][in_action_num]
            stack = in_action['stack']

            cards = in_action['hole_cards']

            if not cards[0]['rank'].isnumeric() and not cards[1]['rank'].isnumeric():
#    print state['']
                return stack
            else:
                return 2
        else:
            return 100

    def showdown(self, game_state):
        pass

