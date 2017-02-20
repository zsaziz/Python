class ConservativePlayer:

    def make_bet(self, playerbank):
        return playerbank.get_wager()

    def use_ace_hi(self, hand):
        if hand.get_score() + 11 <= 21:
            return True
        return False

    def want_card(self, hand, playerbank, dealerhand, cards_dealt):
        if hand.score_hand(ConservativePlayer.use_ace_hi(self, hand)) < 15:
            return True
        return False
