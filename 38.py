class User:
    def __init__(self):
        self._name = None

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


class Employee(User):
    def set_name(self, name):
        if len(name) > 0:
            self._name = name
