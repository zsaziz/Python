from dealer_player import DealerPlayer
from hand import Hand
from player_bank import PlayerBank


class Dealer:
    def __init__(self, deck):
        self._deck = deck
        self._dealer = DealerPlayer
        self._dealer_hand = Hand()
        self._players = dict()
        self.cards_dealt = []

    def add_player(self, handle, player, playerbank):
        if self._players.__contains__(handle):
            raise RuntimeError('player handle is already a key')
        self._players[handle] = (player, Hand(), playerbank)

    def take_bets(self):
        for i in self._players:
            try:
                self._players[i][0].make_bet(self._players[i][2])
                self._players[i][2].enter_bet(self._players[i][2].get_balance())
            except RuntimeError:
                print('Bet amount is greater than current balance')

    def deal_initial_hand(self):
        for i in self._players:
            card1 = self._deck.remove_card()
            card2 = self._deck.remove_card()
            self._players[i][1].add_card(card1)
            self._players[i][1].add_card(card2)
            self.cards_dealt.append(card1)
            self.cards_dealt.append(card2)
        dcard1 = self._deck.remove_card
        dcard2 = self._deck.remove_card
        self._dealer_hand.add_card(dcard1)
        self._dealer_hand.add_card(dcard2)
        self.cards_dealt.append(dcard1)

    def deal_player_hands(self):
        for i in self._players:
            while self._players[i][0].want_card(self._players[i][1], self._players[i][2], self._dealer_hand.get_cards()[0], self.cards_dealt):
                while self._players[i][1].score_hand(self._players[i][0].use_ace_hi(self._players[i][1])) < 21:
                    card1 = self._deck.remove_card
                    self._players[i][1].add_card(card1)
                    self.cards_dealt.append(card1)
            self._players[i][1].set_score(self._players[i][1].score_hand(self._players[i][0].use_ace_hi(self._players[i][1])))

    def deal_dealer_hand(self):
        while self._dealer.want_card(self._dealer_hand, PlayerBank, [], []) \
                and self._dealer_hand.score_hand(self._dealer.use_ace_hi(self._dealer_hand)) < 21:
                card1 = self._deck.remove_card
                self._dealer_hand.add_card(card1)
                self.cards_dealt.append(card1)
        self._dealer_hand.set_score(self._dealer_hand.score_hand(self._dealer.use_ace_hi(self._dealer_hand)))

    def settle_bets(self):
        for i in self._players:
            score = self._players[i][1].get_score()
            dscore = self._dealer_hand.get_score()
            if score > 21:
                self._players[i][2].bust
            elif dscore > 21:
                self._players[i][2].pay_winner(self._players[i][2].get_wager() * 2)
            elif score == dscore:
                self._players[i][2].bust
            elif score > dscore:
                self._players[i][2].pay_winner(self._players[i][2].get_wager() * 2)
            else:
                self._players[i][2].bust

    def __str__(self):
        s = """$$$$$$  Game Summary  $$$$$$\nDealer:\nscore: """ + str(self._dealer_hand.get_score()) + '\n' + \
            self._dealer_hand.__str__()
        for i in self._players:
            s += '\n\nPlayer: ' + i + '\n score: ' + str(self._players[i][1].get_score()) + \
                 '\n' + self._players[i][1].__str__() + '\n' + self._players[i][2].__str__()
        return s
