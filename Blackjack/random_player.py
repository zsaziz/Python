class RandomPlayer:

    def make_bet(self, playerbank):
        return playerbank.get_wager()

    def use_ace_hi(self, hand):
        if hand.get_score() + 11 <= 21:
            return True
        return False

    def want_card(self, hand, cards_dealt):
        if hand.score_hand(RandomPlayer.use_ace_hi(hand)) < 19:
            return True
        return False
