class ATM:
    def __init__(self):
        self.denominations = [20, 50, 100, 200, 500]
        self.counts = [0, 0, 0, 0, 0]

    def deposit(self, banknotesCount: List[int]) -> None:
        self.counts = [current + new for current, new in zip(self.counts, banknotesCount)]

    def withdraw(self, amount: int) -> List[int]:
        if amount % 10 != 0:
            return [-1]

        withdrawal_counts = [0, 0, 0, 0, 0]

        for i in range(4, -1, -1):
            if amount >= self.denominations[i] and self.counts[i] > 0:
                withdrawal_counts[i] = min(self.counts[i], amount // self.denominations[i])
                amount -= withdrawal_counts[i] * self.denominations[i]

        if amount != 0:
            return [-1]

        for i in range(5):
            self.counts[i] -= withdrawal_counts[i]

        return withdrawal_counts





# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)