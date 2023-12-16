class Store:
    def __init__(self):
        self.data = {}

    def set(self, key, value):
        keys = key.split('.')
        curr = self.data
        for i in range(len(keys) - 1):
            if keys[i] not in curr:
                curr[keys[i]] = {}
            curr = curr[keys[i]]
        curr[keys[-1]] = value

    def get(self, key):
        keys = key.split('.')
        curr = self.data
        for k in keys:
            if k not in curr:
                return None
            curr = curr[k]
        return curr

    def update(self, key, new_value):
        keys = key.split('.')
        curr = self.data
        for k in keys[:-1]:
            if k not in curr:
                return
            curr = curr[k]
        curr[keys[-1]] = new_value

    def delete(self, key):
        keys = key.split('.')
        curr = self.data
        for k in keys[:-1]:
            if k not in curr:
                return
            curr = curr[k]
        curr.pop(keys[-1], None)
