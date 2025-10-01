from enum import Enum


class CustomEnum(Enum):

    pass


@CustomEnum
class AccountType:
    SAVINGS = "savings"
    CURRENT = "current"

print(AccountType.SAVINGS.value)
