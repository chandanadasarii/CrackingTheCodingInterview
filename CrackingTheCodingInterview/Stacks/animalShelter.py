import time

class AnimalShelter:
    dogs = list()
    cats = list()

    def enqueue(self, animal, type):
        if type == 'dog':
            self.dogs.append((time.time(), animal))
        elif type == 'cat':
            self.cats.append((time.time(), animal))
        else:
            raise Exception("Invalid Animal type!!")

    
    def dequeueAny(self):

        if len(self.cats) == 0 and len(self.dogs) == 0:
            return None
        elif len(self.dogs) == 0 and len(self.cats) != 0:
            return self.cats.pop(0)[1] 
        elif len(self.dogs) != 0 and len(self.cats) == 0:
            return self.dogs.pop(0)[1]
        else:
            if self.dogs[0][0] > self.cats[0][0]:
                return self.cats.pop(0)[1]
            else:
                return self.dogs.pop(0)[1]

    def dequeueDog(self):
        if len(self.dogs):
            return self.dogs.pop(0)[1]
        else:
            return None

    def dequeueCat(self):
        if len(self.cats):
            return self.cats.pop(0)[1]
        else:
            return None 


as1 = AnimalShelter()
as1.enqueue('a', 'dog')
as1.enqueue('b', 'dog') 
