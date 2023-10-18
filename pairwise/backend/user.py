from .util import Rank

class User:

    @staticmethod
    def parse_from_str(s):
        '''
            Strings will be of the form <RANK>/<LAST_NAME>/<FIRST_NAME>/<USER ID>

            i.e. 1LT/HIEBERT/MICHAEL/123456789
        '''

        rank,last,first,user_id = s.split('/')

        return User(user_id, Rank._value2member_map_[rank], last, first)
    
    def __init__(self, user_id: str, rank: Rank, last_name: str, first_name: str):
        self.user_id = user_id

        self.rank = rank
        self.last_name = last_name
        self.first_name = first_name

    @property
    def name(self):
        return f'{self.rank.value} {self.last_name}, {self.first_name}'