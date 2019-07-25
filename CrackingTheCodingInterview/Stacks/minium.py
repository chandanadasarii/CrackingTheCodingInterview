class minStack:
    __values = list()
    __minval = list()

    def push(self, data):
        self.__values.append(data)
        minval = self.getmin()
        if minval and data < minval:
            self.__push_min(data)
    
    def __push_min(self, data):
        self.__minval.append(data)

    def peek(self):
        return self.__values[-1]

    def __pop_min(self):
        return self.__minval.pop()

    def pop(self):
        val = self.__values.pop()
        if val == self.getmin():
            self.__pop_min()
    
    def getmin(self):
        if len(self.__minval) == 0:
            return None
        return self.__minval[-1]


ms = minStack()
ms.push(10)
ms.push(20)
ms.push(30)
ms.push(5)