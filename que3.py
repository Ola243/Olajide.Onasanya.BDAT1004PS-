class Marsupial:
    def __init__(self):
        self.pouch = []

    def pouch_contents(self):
        return self.pouch

    def put_in_pouch(self, item):
        self.pouch.append(item)


class Kangaroo(Marsupial):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__()

    def jump(self, x, y):
        self.x += x
        self.y += y

    def __str__(self):
        return f"I am a Kangaroo located at coordinates ({self.x},{self.y})"


