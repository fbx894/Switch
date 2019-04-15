"""
Simple Example:
from switch import *
def Case1():
  print("Case 1 Selected")
def Case2():
  print("Case 2 Selected")
def default():
  print("Default selected")
x = int(input())
code = switch(
  key = x, case = [1,2],
  command = [Case1,Case2],
  default = default
)
code.run()
"""
__author__ = "Victor G. Rodrigues"
__email__ = "victorgrodriguesm7@gmail.com"
__version__ = "0.1"
__all__ = ['switch']
class switch():
    def __init__(self, key, case = [],command = [], default = '' ):
        if (hasattr(default, '__call__') == False): raise Exception("Default need be a fuction")
        self.key = key; self.case = case; self.command = command; self.default = default
    def run(self):
        #Simple Key Verification Comparing with Cases
        for i,case in enumerate(self.case):
          if self.key == case: # Run command
            self.command[i]()
            break
        else: #Run Default
            try:
                self.default()
            except Exception as error:
                print("Error: Default need be Fuction")
    #Getters and Setters created, will hardly be used, but are already implemented if necessary
    #Setters:
    def set_key(self, newValue, again):
      self.key = newValue
      if again: self.run() #Run again
    def set_case(self,newValue,i):
      try:
          self.case[i] = newValue
      except:
          self.case.append(newValue)
    def set_command(self,newValue,i):
      try: self.command[i] = newValue
      except: self.command.append(newValue)
    #Getters:
    def get_key(self): return self.key
    def get_case(self): return self.case
    def get_command(self): return self.command
