from typing import List

class Assessment:
    
    @staticmethod
    def parse_from_str(s):
        '''
            Example str:

            a>b>c=d>e=f=g>h>j
        '''

        if s == '': return None

        rankings = s.split('>')

        first_grouping = rankings[0].split('=')
        other_groupings = '>'.join(rankings[1:])

        user_id = first_grouping.pop(0)

        return Assessment(user_id, first_grouping, Assessment.parse_from_str(other_groupings))

    def __init__(self, user_id:str, equal_to: List[str], better_than):
        self.equal_to = equal_to.copy()
        self.better_than = better_than

    @property
    def has_next(self):
        return self.better_than is not None

    @property
    def next(self):
        return self.better_than
    
    def insert(self, other_assessment):
        pass