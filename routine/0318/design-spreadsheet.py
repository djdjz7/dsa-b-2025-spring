# https://leetcode.cn/problems/design-spreadsheet/description/


class Spreadsheet:

    def __init__(self, rows: int):
        self.spreadsheet = [[0] * 26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        self.spreadsheet[int(cell[1:]) - 1][ord(cell[0]) - 65] = value

    def resetCell(self, cell: str) -> None:
        self.spreadsheet[int(cell[1:]) - 1][ord(cell[0]) - 65] = 0

    def getValue(self, formula: str) -> int:
        ref1, ref2 = formula[1:].split("+")
        v1 = (
            int(ref1)
            if ref1.isdecimal()
            else self.spreadsheet[int(ref1[1:]) - 1][ord(ref1[0]) - 65]
        )
        v2 = (
            int(ref2)
            if ref2.isdecimal()
            else self.spreadsheet[int(ref2[1:]) - 1][ord(ref2[0]) - 65]
        )
        return v1 + v2
