# Import Necessary Packages
from abc import ABC, abstractmethod
# Create Base Class
class Animal(ABC):
    
    # Abstract Method
    # Should be implemented by all sub-classes
    def move(self):
        pass

# Sub Classes
class Human(Animal):
    
    def move(self):
        print("I can walk and run")
        
class Snake(Animal):
    
    def move(self):
        print("I can crawl")
        
class Dog(Animal):
    
    def move(self):
        print("I can bark and run")
        
class Lion(Animal):
    
    def move(self):
        print("I can roar")
    
# Driver Code
R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()
