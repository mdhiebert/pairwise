import enum

class Rank(enum.Enum):
    SECOND_LIEUTENANT = '2LT'
    FIRST_LIEUTENANT = '1LT'
    CAPTAIN = 'CPT'
    MAJOR = 'MAJ'
    LIEUTENANT_COLONEL = 'LTC'
    COLONEL = 'COLONEL'

print(Rank._value2member_map_)