import random
from typing import Optional, Any, Union, List, Tuple, Dict, Iterable


class Character:

    def __init__(self, armor: int, power: int):
        self.armor = armor
        self.power = power
        self.health = 100

    def hit(self, damage: int):
        self.health -= damage - (damage * self.armor / 100)

    def is_alive(self) -> bool:
        return self.health > 0


c1 = Character(10, 20)
c1.hit(c1.power)

amount: int
amount = 10

price: Optional[int]
price = 'asd'
attack: Any = 1
print(attack)
attack = 'asd'

length: Union[int, float]
length = 1.2
print(length)
length = 1

quotes: list
quotes = [1, 2, 3]
quotes: List[int]
quotes.append(1)
quotes.append('asd')

player: Tuple[str, int] = ('Kramnik', 2750)

changes_in_rating: Tuple[int, ...]
changes_in_rating = (1, 2, 3, 4, 5)
print(changes_in_rating)
changes_in_rating = (1, 'asdaw')

chess_players: Dict[str, int] = {'Kramnik': 2750}


def random_stream(min_val: int, max_val: int) -> Iterable[int]:
    while True:
        yield random.randint(min_val, max_val)
