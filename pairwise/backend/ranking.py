from typing import List,Tuple
import numpy as np
import math

class PairwiseRanking:

    @staticmethod
    def from_user_list(user_ids: List[str]):
        return PairwiseRanking(user_ids, np.zeros((2, len(user_ids), len(user_ids))))

    def __init__(self, user_ids: List[str], matrix: np.array):
        self._assert_matrix_checks(user_ids, matrix)

        self._user_ids = user_ids
        self._matrix = matrix

        self._NUMBER_OF_PAIRS = self._calculate_pairs()

        for i in range(len(user_ids)):
            self._matrix[1,i,i] = self._NUMBER_OF_PAIRS

    def _assert_matrix_checks(self, user_ids: List[str], matrix: np.array):
        assert matrix.shape == (2, len(user_ids), len(user_ids)), f'Expected matrix to have shape {(2, len(user_ids), len(user_ids))}, got {matrix.shape}'

    def _calculate_pairs(self):
        n = len(self._user_ids)
        k = 2

        return math.comb(n, k)

    def _adjust_matrix(self, better_index: int, worse_index: int, both_equal = False):
        # adjust rankings
        self._matrix[0, better_index, worse_index] = 1 if not both_equal else 0.5
        self._matrix[0, worse_index, better_index] = 0 if not both_equal else 0.5

        # adjust counts
        self._matrix[1, better_index, worse_index] += 1
        self._matrix[1, worse_index, better_index] += 1

    def pick_left(self, left_user: str, right_user: str):
        self._adjust_matrix(self._user_ids.index(left_user), self._user_ids.index(right_user))

    def pick_right(self, left_user: str, right_user: str):
        self._adjust_matrix(self._user_ids.index(right_user), self._user_ids.index(left_user))

    def both_equal(self, left_user: str, right_user: str):
        self._adjust_matrix(self._user_ids.index(left_user), self._user_ids.index(right_user), both_equal = True)

    @property
    def is_complete(self):
        s = np.sum(self._matrix[1,:,:])
        return s == (len(self._user_ids) + 2) * self._NUMBER_OF_PAIRS

    def suggest_new_pairing(self):
        if not self.is_complete:
            suggested_index = np.unravel_index(np.argmin(self._matrix[1,:,:]), self._matrix.shape[1:])

            return self._user_ids[suggested_index[0]], self._user_ids[suggested_index[1]]
        else: return None

    @property
    def rankings(self):
        tallies = np.sum(self._matrix[0,:,:], axis = 1)

        return sorted(zip(self._user_ids, tallies), reverse = False)
    
    def __str__(self):
        '''
            Returns <self._matrix.shape>***<self.matrix.flatten()>***<self._user_ids>
        '''

        return

if __name__ == '__main__':
    USERS = [
        'A',
        'B',
        'C'
    ]

    pr = PairwiseRanking.from_user_list(USERS)

    suggested = pr.suggest_new_pairing()
    while suggested is not None:
        l,r = suggested

        print(l, r)

        inp = input('choice:')

        if inp == 'l':
            pr.pick_left(*suggested)
        elif inp == 'r':
            pr.pick_right(*suggested)
        elif inp == 'e':
            pr.both_equal(*suggested)

        suggested = pr.suggest_new_pairing()

        print(pr._matrix)

    print(pr.rankings)
