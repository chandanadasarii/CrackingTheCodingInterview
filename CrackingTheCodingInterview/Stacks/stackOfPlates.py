class stackOfPlates():
 
    values = list(list())

    def __init__(self, capacity):
        self.capacity = capacity

    def push(self, data):
        if len(self.values) == 0 or len(self.values[-1]) == self.capacity:
            self.values.append([data])
        else:
            self.values[-1].append(data)


    def peek(self):
        return self.values[-1][-1]


    def pop(self):
        if len(self.values[-1]) == 0:
            self.values.pop()
        return self.values[-1].pop()
        

sp = stackOfPlates(3)
sp.push(2)
sp.push(4)
sp.push(7)
sp.push(1)
print(sp.values)
sp.pop()
print(sp.values)
sp.pop()
print(sp.values)