from dataclasses import dataclass


@dataclass(frozen=True)
class Movement:
    required_stamina: int
    stamina_cost: int
    speed: int


CRAWL = Movement(required_stamina=1, stamina_cost=1, speed=1)
HOP = Movement(required_stamina=20, stamina_cost=2, speed=3)
WALK = Movement(required_stamina=40, stamina_cost=2, speed=4)
RUN = Movement(required_stamina=60, stamina_cost=4, speed=6)
FLY = Movement(required_stamina=80, stamina_cost=4, speed=8)
ALL_MOVES = {m for m in (CRAWL, HOP, WALK, RUN, FLY)}
