import ConfigParser

config = ConfigParser.ConfigParser()
config.read("config.ini")

version = config.getint("basic", "version")


class Player:
    VERSION = "Default Python folding player, version " + str(version)

    def betRequest(self, game_state):
        if version < 3:
            in_action_num = game_state[u'in_action']
            in_action = cards = game_state[u'players'][in_action_num]
            stack = in_action['stack']

            cards = in_action['hole_cards']

            if not cards[0]['rank'].isnumeric() and not cards[1]['rank'].isnumeric():
#    print state['']
                return stack
            else:
                return 0
        else:
            return 100

    def showdown(self, game_state):
        pass

