class Hand:
    def __init__(self):
        self._cards = []
        self._score = 0

    def add_card(self, card):
        self._cards.append(card)

    def get_score(self):
        return self._score

    def set_score(self, score):
        self._score = score

    def has_ace(self):
        for i in range (len(self._cards)):
            if self._cards[i].rank == 'A':
                return True
        return False

    def score_hand(self, ace):
        score = 0
        for i in range (len(self._cards)):
            if self._cards[i].rank == 'A' and ace:
                score += 11
            elif self._cards[i].rank == 'A' and not ace:
                score += 1
            elif type(self._cards[i].rank) != int:
                score += 10
            else:
                score += int(self._cards[i].rank)
        return score

    def get_cards(self):
        return self._cards

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        return str(self._cards)
