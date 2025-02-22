# https://leetcode.cn/problems/design-an-atm-machine/description/

from typing import List


class ATM:

    def __init__(self):
        self.note_count = [0] * 5
        self.notes = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.note_count[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        result = [0] * 5
        for i in range(4, -1, -1):
            result[i] = min(self.note_count[i], amount // self.notes[i])
            amount -= self.notes[i] * result[i]
        if amount != 0:
            return [-1]
        for i in range(5):
            self.note_count[i] -= result[i]
        return result


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
