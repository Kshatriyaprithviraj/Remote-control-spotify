from enum import Enum, auto

# An enumeration to represent both kinds of authentication
# flow that spotify provides.

class authMethod(Enum):
    CLIENT_CREDENTIALS = auto()
    AUTHORIZATION_CODE = auto()