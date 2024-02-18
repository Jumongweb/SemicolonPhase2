class Gun:
    def __init__(self):
        self.bullet = 0

    def getChamber(self):
        return self.bullet

    def load_bullet(self):
        self.bullet = 40

    def add_bullet(self):
        if 0 <= self.bullet < 40:
            self.bullet += 1

    def shoot(self):
        if self.bullet > 0:
            self.bullet -= 1

    def reload(self):
        self.bullet = 40
