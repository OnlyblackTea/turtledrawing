class stack:

    def __init__(self):
        self.__list = []

    def empty(self):
        return self.__list == []

    def insert(self, item):
        self.__list.append(item)

    def pop(self):
        if self.empty():
            return
        else:
            return self.__list.pop()

    def top(self):
        if self.empty():
            return
        else:
            return self.__list[-1]
