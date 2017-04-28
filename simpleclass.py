#!/usr/bin/python
#Filename:simpleclass.py

class Person:
    '''Represents a person.'''
    population=0
    
    def __init__(self, name):
        self.name = name
        Person.population += 1
    def __del__(self):
        Person.population -= 1
        if Persion.population == 0:
            print("the last one")
    def sayHi(self):
        print("how are you?",self.name)
    def howMany(self):
        print("we have %d persons here." % Person.population)

swaroop = Person('Swaroop')
swaroop.sayHi()
swaroop.howMany()

kalam = Person('Abdul Kalam')
kalam.sayHi()
kalam.howMany()

swaroop.sayHi()
swaroop.howMany()
