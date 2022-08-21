from typing import Optional

from Sudoku.Cell import Cell


class Board:

    def __init__(self, numbers: Optional[list[int]] = None) -> None:

        # we keep list of cells and dictionaries to point to each cell
        # by various locations
        self.rows = {}
        self.columns = {}
        self.boxes = {}
        self.cells = []

        for row in range(0, 9):
            for col in range(0, 9):
                # calculating box
                box = 3 * (row // 3) + (col // 3)

                # creating cell instance
                cell = Cell(row, col, box)

                # if initial set is given, set cell value
                if numbers is not None:
                    cell.value = numbers.pop(0)
                else:
                    cell.value = 0

                # initializing dictionary keys and corresponding lists
                # if they are not initialized
                if row not in self.rows:
                    self.rows[row] = []
                if col not in self.columns:
                    self.columns[col] = []
                if box not in self.boxes:
                    self.boxes[box] = []

                # adding cells to each list
                self.rows[row].append(cell)
                self.columns[col].append(cell)
                self.boxes[box].append(cell)
                self.cells.append(cell)

    def get_used_cells(self) -> list[Cell]:
        """returning cells in puzzle that are not set to zero"""
        return [x for x in self.cells if x.value != 0]

    def get_unused_cells(self) -> list[Cell]:
        """returning cells in puzzle that are set to zero"""
        return [x for x in self.cells if x.value == 0]

    def get_possibles(self, cell) -> list[int]:
        """returning all possible values that could be assigned to the cell provided as argument"""
        possibilities = self.rows[cell.row] + self.columns[cell.col] + self.boxes[cell.box]
        excluded = set([x.value for x in possibilities if x.value != 0 and x.value != cell.value])
        results = [x for x in range(1, 10) if x not in excluded]
        return results

    def get_density(self, cell) -> float:
        """calculates the density of a specific cell's context"""
        possibilities = self.rows[cell.row] + self.columns[cell.col] + self.boxes[cell.box]
        if cell.value != 0:
            possibilities.remove(cell)
        return len([x for x in set(possibilities) if x.value != 0]) / 20.0

    def get_excluded(self, cell) -> set[int]:
        """gets complement of possibles, values that cell cannot be"""
        possibilities = self.rows[cell.row] + self.columns[cell.col] + self.boxes[cell.box]
        return set([x.value for x in possibilities if x.value != 0 and x.value != cell.value])

    def swap_row(self, row_index1, row_index2, allow=False) -> None:
        """swaps two rows"""
        if allow or row_index1 // 3 == row_index2 // 3:
            for x in range(0, len(self.rows[row_index2])):
                temp = self.rows[row_index1][x].value
                self.rows[row_index1][x].value = self.rows[row_index2][x].value
                self.rows[row_index2][x].value = temp
        else:
            raise Exception('Tried to swap non-familial rows.')

    def swap_column(self, col_index1, col_index2, allow=False) -> None:
        """swaps two columns"""
        if allow or col_index1 // 3 == col_index2 // 3:
            for x in range(0, len(self.columns[col_index2])):
                temp = self.columns[col_index1][x].value
                self.columns[col_index1][x].value = self.columns[col_index2][x].value
                self.columns[col_index2][x].value = temp
        else:
            raise Exception('Tried to swap non-familial columns.')

    def swap_stack(self, stack_index1, stack_index2) -> None:
        """swaps two stacks"""
        for x in range(0, 3):
            self.swap_column(stack_index1 * 3 + x, stack_index2 * 3 + x, True)

    def swap_band(self, band_index1, band_index2) -> None:
        """swaps two bands"""
        for x in range(0, 3):
            self.swap_row(band_index1 * 3 + x, band_index2 * 3 + x, True)

    def copy(self) -> 'Board':
        """copies the board"""
        b = Board()
        for row in range(0, len(self.rows)):
            for col in range(0, len(self.columns)):
                b.rows[row][col].value = self.rows[row][col].value
        return b

    def __str__(self) -> str:
        """returns string representation"""
        output = []
        for index, row in self.rows.items():
            my_set = map(str, [x.value for x in row])
            new_set = []
            for x in my_set:
                if x == '0':
                    new_set.append("_")
                else:
                    new_set.append(x)
            output.append('|'.join(new_set))
        return '\r\n'.join(output)

    def html(self) -> str:
        """exporting puzzle to a html table for prettier visualization"""
        html = "<table>"
        for index, row in self.rows.items():
            values = []
            row_string = "<tr>"
            for x in row:
                if x.value == 0:
                    values.append(" ")
                    row_string += "<td>%s</td>"
                else:
                    values.append(x.value)
                    row_string += "<td>%d</td>"
            row_string += "</tr>"
            html += row_string % tuple(values)
        html += "</table>"
        return html
