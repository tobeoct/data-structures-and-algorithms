from enum import Enum
class TraversalType(Enum):
    LTR = 1
    RTL=2

TraversalType = Enum('TraversalType', ['LTR', 'RTL'])