# Basic Syntax
value = 20

match value:
    case 1:
        print(1)
    case 2:
        print(2)
    case _:
        print("No listed before.")

# Veryfing lists
numbers = [1, 2, 3]

match numbers:
    case [1, 2, 3]:
        print("Rule list")
    case [1, _, _]:
        print("1 is the first number!")
    case [_, 2, _]:
        print("2 is the second number!")

# Veryfing lists with _
numbers = [1, 10, "1.0"]

match numbers:
    case [_, _, str(_)]:
        print(f"1 is the first number!")

numbers = [30, 2, 80]

match numbers:
    case [_, 2, _]:
        print("2 is the second number!")

# Advanced forms
numbers = [1, 2, 3]

match numbers:
    case [] | [_]:
        print("One or No one Element")
    case [1, 2]:
        print("List == [1, 2]")
    case [1, *other_elements]:
        print(f"1 is the first of a list > 1 | {other_elements=}")

# Colors
color = (155, 155, 155)

match color:
    case r, g, b:
        print(f"Where's alpha? {r=} {g=} {b=} a=???")
    case r, g, b, a if a == 255:
        print(f"Cannot be transparent {r=} {g=} {b=} {a=}")
    case r, g, b, a if r == 255:
        print(f"It's too red {r=} {g=} {b=} {a=}")
    case r, g, b, a if g == 255:
        print(f"It's too green {r=} {g=} {b=} {a=}")
    case r, g, b, a if b == 255:
        print(f"It's too blue {r=} {g=} {b=} {a=}")
    case r, g, b, a:
        print(f"Now it's a valid color :P {r=} {g=} {b=} {a=}")

# Advanced cases
def move(action: str):
    match action.lower().split():
        case ['move']:
            return 'To where? (left, right, up, down)'
        case ['jump']:
            return 'Jumping'
        case 'move', 'left' | 'right' as direction:
            return f'Moving horizontally to {direction}'
        case 'move', 'up' | 'down' as direction:
            return f'Moving vertically to {direction}'


print(move(action="move up"))

# Dictionaries

dictionary = {"a": 15, "b": 32}
# dictionary = {"error": "There is a error in dictionary", "b": 2}

match dictionary:
    case {'a': 1}:
        print('Literal Match')
    case {'a': _, 'b': 2}:
        print('Match on key b')
    case {'a': 1, 'b': _}:
        print('Match on key a')
    case {'a': _, 'b': _}:
        print('No match')
    case {'error': error}:
        print(f'Error -> {error}')

# Match exactly one key
payload = {"id": "123",
           "cpf": "1234567890",
           "name": "Fulan",
           "age": 32,
           "created_at": "2022-02-02",
           }

match payload:
    case {"name": name, **kwargs}:
        print(f"Match name: {name} and {kwargs}")

# Objects

from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    is_partner: bool = False


def price(pessoa: Person, event_cost: float = 35) -> str:
    match pessoa:
        case Person(name, age) if age >= 65:
            return f"{name.capitalize()} must to pay a half {event_cost / 2}"
        case Person(name, _, True):
            return f"{name.capitalize()} works here, cost: {event_cost / 3:.2f}"
        case Person(name, _):
            return f"{name.capitalize()} must to pay normal ticket, cost: {event_cost:.2f}"


print(price(Person("Fulan", 68)))
print(price(Person("William", 18, True)))
print(price(Person("Robert", 18)))


class Customer:
    __match_args__ = "name", "age", "is_partner"

    def __init__(self, name: str, age: int, is_partner: bool = False):
        self.name = name
        self.age = age
        self.is_partner = is_partner


def price(pessoa: Customer, event_cost: float = 35) -> str:
    match pessoa:
        case Customer(name, age) if age >= 65:
            return f"{name.capitalize()} must to pay a half {event_cost / 2}"
        case Customer(name, _, True) as worker:
            return f"{name.capitalize()} works here {worker.is_partner=}, cost: {event_cost / 3:.2f}"
        case Customer(name, _):
            return f"{name.capitalize()} must to pay normal ticket, cost: {event_cost:.2f}"


print(price(Customer("Fulan", 68)))
print(price(Customer("William", 18, True)))
print(price(Customer("Robert", 18)))
