class PlayerBank:
    def __init__(self, balance=0):
        self._balance = balance
        self._bets_placed = 0
        self._is_winner = False

    def pay_winner(self, amount):
        self._is_winner = True
        self._balance = self._balance + amount

    def bust(self):
        self._is_winner = False

    def get_balance(self):
        return self._balance

    def get_wager(self):
        return self._bets_placed

    def enter_bet(self, amount):
        if amount > self._balance:
            raise RuntimeError('Bet amount is greater than current balance')
        self._bets_placed += amount
        self._balance -= amount

    def __str__(self):
        s = 'Player assets:\nbet ' + str(self._bets_placed) + ' balance ' + str(self._balance)
        if self._is_winner:
            s += ' winner!'
        else:
            s += ' bust.'
        return s
