# Import Necerssary Modules
from abc import ABC, abstractmethod

# Create Base Class
class AbsClass(ABC):
    
    # Function to print a value
    def print(self,x):
        print("Passed Value: ", x)
        
    # Abstract Method
    @abstractmethod
    def task(self):
        print("We are inside Absclass task")
        
    # Create Sub CLass
class test_class(AbsClass):
    def task(self):
        print("We are inside test_class task")

# Object of test_class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)
