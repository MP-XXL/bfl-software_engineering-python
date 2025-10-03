from enum import Enum


def CustomEnum(cls):

    enum_members = {}

    for key, value in cls.__dict__.items():
        if not key.startswith("__"):
            enum_members[key] = value
    
    return Enum(cls.__name__, enum_members)


@CustomEnum
class AccountType:
    SAVINGS = "savings"
    CURRENT = "current"

print(AccountType.SAVINGS.value)


