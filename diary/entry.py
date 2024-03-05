class Entry:
    def __init__(self, identity, title, body):
        self.identity = identity
        self.title = title
        self.body = body
        # self.date = datetime

    def get_id(self):
        return self.identity

    def get_title(self):
        return self.title

    def set_body(self, body):
        self.body = body

    def get_body(self):
        return self.body

