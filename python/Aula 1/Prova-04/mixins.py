import json

class AuthMixin:
    def is_authenticated(self):
        return self.header.get('token', '') == '0x24'

class JSONMixin:
    @property
    def as_json(self):
        if not self.header.get('Content-Type', '').lower() == 'application/json':
            raise ValueError('unexpected content type')
        return json.loads(self.body)
    
class Request(AuthMixin, JSONMixin):
    def __init__(self, header, body):
        self.header = header
        self.body = body

    def process(self):
        if not self.is_authenticated():
            return 'invalid user'
        return self.as_json


if __name__ == '__main__':
    print(Request({'token': '0x24', 'Content-Type': 'application/json'}, '[0, 1, 2, 3, 5]').process())
    print(Request({'token': 'xxxx', 'Content-Type': 'application/json'}, '[6, 7, 8, 9, 5]').process())