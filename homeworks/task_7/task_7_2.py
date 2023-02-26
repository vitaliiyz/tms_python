from collections import deque


class HistoryDict:
    def __init__(self, user_dict: dict):
        self._user_dict = user_dict
        self._history = deque(maxlen=10)

    @property
    def user_dict(self):
        return self._user_dict

    @property
    def history(self):
        return self._history

    def set_value(self, key, value):
        self.user_dict[key] = value
        self.history.append(key)

    def get_history(self):
        print(list(self.history))


d = HistoryDict({"foo": 42})
d.set_value("bar", 43)
d.get_history()
