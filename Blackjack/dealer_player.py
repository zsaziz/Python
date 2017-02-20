class DealerPlayer:

    @staticmethod
    def make_bet(playerbank):
        return playerbank.get_wager()

    @staticmethod
    def use_ace_hi(hand):
        if hand.get_score() + 11 <= 21:
            return True
        return False

    @staticmethod
    def want_card(hand, playerbank, dealerhand, cards_dealt):
        if hand.score_hand(DealerPlayer.use_ace_hi(hand)) < 17:
            return True
        else:
            return False
