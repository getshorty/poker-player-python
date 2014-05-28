import ConfigParser

config = ConfigParser.ConfigParser()
config.read("config.ini")

version = config.getint("basic", "version")


class Player:
    VERSION = "GetShorty version " + str(version)

    def betRequest(self, game_state):
        global version

        if version == 4:
            try:
                from pre_flop_strategy1 import Strategy
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
                    return stack
                elif hv.getValue() >= 80:
                    return smallBlind * 6
                else:
                    return 3
            except:
                version = 2
        elif version < 3:
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

