class QueueWithStacks():
    stackm = list()
    stacka = list()

    def enqueue(self, data):
        if len(self.stackm) == 0 and len(self.stacka) != 0:
            for i in range(len(self.stacka)):
                self.stackm.append(self.stacka.pop())
        self.stackm.append(data)

    def dequeue(self):
        if len(self.stacka) == 0:
            if len(self.stackm) == 0:
                return None
            for i in range(len(self.stackm)):
                self.stacka.append(self.stackm.pop())

        return self.stacka.pop()


q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
q.enqueue(4)
print(q.stackm)
