from question1 import Array
from timeit import Timer
from memory_profiler import profile

#The beginning of Qn2
class SubArray(Array):
    @profile
    def add(self, values):
        print("***QUESTION 2***")
        values.append(34)
        print("WE HAVE ADDED 34 IN THE ARRAY: " , values)

    @profile
    def delete(self, values):
        values.remove(9)
        print("9 WAS REMOVED FROM THE ARRAY. THE NEW ARRAY IS: " , values)
        print("")

# Third Question
    #Check if a value is in an array
    @profile
    def check(self, values):
        print("***QUESTION 3***")
        if 5 in values:
            contains = True
            print(contains)
        else:
            print("none")

    #Reversing an array
    @profile
    def reverse(self,values):
        print("THE REVERSE IS: ")
        for i in reversed(values):
            print(i)

    # Adding an item to a specific location
    @profile
    def insertion(self, values):
        values.insert(3, 76)
        print(values)
        print("")

if __name__=='__main__':
    t = Timer("SubArray", "from __main__ import SubArray")
    print("This is the Runtime for this program: " , t.timeit())
