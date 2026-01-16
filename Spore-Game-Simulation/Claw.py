from BodyParts import BodyParts


class Claw(BodyParts):
    def __init__(self, mul):
        # size_l = size.lower()
        super().__init__(
            name="claw",
            attack_add=0,
            attack_mul=mul,
            movements_provided=None,
            count=1,
        )
