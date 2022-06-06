## Animal is-a object look at the extra credit
class Animal(object):
    pass

## Dog has a relationship with Animal class
class Dog(Animal):

    def __init__(self, name):
        ## dog has a name
        self.name = name
    