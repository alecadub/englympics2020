import numpy as np
from weighted_levenshtein import lev


class MatchString:

    def __init__(self):
        self.insert_costs = np.ones(128,
                                    dtype=np.float64)  # make an array of all 1's of size 128, the number of ASCII characters
        # Insert Weight Distance
        self.insert_costs[ord(' ')] = 2
        self.insert_costs[ord('1')] = 1
        self.insert_costs[ord('2')] = 1
        self.insert_costs[ord('3')] = 1
        self.insert_costs[ord('4')] = 1
        self.insert_costs[ord('5')] = 1
        self.insert_costs[ord('6')] = 1
        self.insert_costs[ord('7')] = 1
        self.insert_costs[ord('8')] = 1
        self.insert_costs[ord('9')] = 1

        self.substitute_costs = np.ones((128, 128), dtype=np.float64)  # make a 2D array of 1's

        # Common OCR Deletion Mistakes
        self.delete_costs = np.ones(128, dtype=np.float64)
        self.delete_costs[ord(' ')] = 2

        # Common OCR Mistakes - Group 1
        self.substitute_costs[ord('O'), ord('D')] = 0.25
        self.substitute_costs[ord('D'), ord('O')] = 0.25

        self.substitute_costs[ord('Q'), ord('D')] = 0.25
        self.substitute_costs[ord('D'), ord('Q')] = 0.25

        self.substitute_costs[ord('O'), ord('Q')] = 0.25
        self.substitute_costs[ord('Q'), ord('O')] = 0.25

        # Common OCR Mistakes - Group 2
        self.substitute_costs[ord('I'), ord('J')] = 0.25
        self.substitute_costs[ord('J'), ord('I')] = 0.25

        self.substitute_costs[ord('I'), ord('L')] = 0.25
        self.substitute_costs[ord('L'), ord('I')] = 0.25

        self.substitute_costs[ord('I'), ord('T')] = 0.25
        self.substitute_costs[ord('T'), ord('I')] = 0.25

        self.substitute_costs[ord('J'), ord('L')] = 0.25
        self.substitute_costs[ord('L'), ord('J')] = 0.25

        self.substitute_costs[ord('J'), ord('T')] = 0.25
        self.substitute_costs[ord('T'), ord('J')] = 0.25

        self.substitute_costs[ord('L'), ord('T')] = 0.25
        self.substitute_costs[ord('T'), ord('L')] = 0.25

        # Common OCR Mistakes - Group 3

        self.substitute_costs[ord('U'), ord('V')] = 0.25
        self.substitute_costs[ord('V'), ord('U')] = 0.25

        # Common OCR Mistakes - Group 4

        self.substitute_costs[ord('F'), ord('P')] = 0.5
        self.substitute_costs[ord('P'), ord('F')] = 0.5

        # Common OCR Mistakes - Group 5

        self.substitute_costs[ord('C'), ord('G')] = 0.5
        self.substitute_costs[ord('G'), ord('C')] = 0.5

    def match(self, string1, string2):
        # Testing
        return lev(string1.lower(), string2.lower(), substitute_costs=self.substitute_costs, delete_costs=self.delete_costs, insert_costs=self.insert_costs)
