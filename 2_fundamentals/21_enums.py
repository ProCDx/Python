# Enums - readable names bound to constant values
from enum import Enum

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(State.ACTIVE)          # State.ACTIVE
print(State.ACTIVE.value)    # 1
print(State(1))              # State.ACTIVE
print(State["ACTIVE"])       # State.ACTIVE

print(list(State))           # all members
print(len(State))            # 2
