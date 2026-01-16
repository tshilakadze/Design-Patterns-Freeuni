from BodyParts import BodyParts


class Teeth(BodyParts):
    def __init__(self, boost):
        super().__init__(
            name="teeth",
            attack_add=boost,
            attack_mul=1,
            movements_provided=None,
            count=1,
        )
