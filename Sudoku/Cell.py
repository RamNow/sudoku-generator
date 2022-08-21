class Cell:

    def __init__(self, row, col, box):
        """defining the cell, each cell keeps track of its own value and location"""
        self.row = row
        self.col = col
        self.box = box

        self.value = 0

    def __str__(self) -> str:
        """returns a string representation of cell (for debugging)"""
        return f"Value: {self.value:d}, Row: {self.row:d}, Col: {self.col:d}, Box: {self.box:d}"
