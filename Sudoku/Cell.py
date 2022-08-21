class Cell:

    def __init__(self, row, col, box):
        """defining the cell, each cell keeps track of its own value and location"""
        self.row = row
        self.col = col
        self.box = box

        self.value = 0

    def __str__(self):
        """returns a string representation of cell (for debugging)"""
        temp = (self.value, self.row, self.col, self.box)
        return "Value: %d, Row: %d, Col: %d, Box: %d" % temp
