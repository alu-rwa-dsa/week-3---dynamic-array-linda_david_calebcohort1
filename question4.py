from timeit import Timer
from memory_profiler import profile

# Fourth Question
class Dictionary:
    #(a) Add items to the Dictionary
    @profile
    def addition(self, dict):
        print("***QUESTION 4***")
        dict["gender"] = "male"
        print("THE LIST AFTER ADDING gender: " , dict)

    #(b) Remove items from Dictionary
    @profile
    def remove(self, dict):
        dict.pop("name")
        print("THE LIST AFTER REMOVING THE AGE: ", dict)

    #(c) Modify item in the dictionary
    @profile
    def modify(self, dict):
        dict["age"] = 85
        print("THE LIST AFTER CHANGING age: " , dict)

    #(d) Lookup method
    @profile
    def lookup(self, dict):
        lookup_value = "male"
        thevalue = []
        for key, value in dict.items():
            if (value == lookup_value):
                thevalue.append(key)
        print("THE WAS FOUND, THE KEY IS:" , thevalue)

if __name__=='__main__':
    t = Timer("Associate", "from __main__ import Associate")
    print("This is the Runtime for this program: " , t.timeit())