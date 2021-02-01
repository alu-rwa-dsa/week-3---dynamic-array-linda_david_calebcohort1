from timeit import Timer
from memory_profiler import profile


class Array:
# The beginning of Qn1
    # (a)The length of the array
    @profile
    def length(self, values):
        print("***QUESTION 1***")
        print("THE LENGTH OF THE ARRAY IS: " , len(values))

    # (b)The index of a chosen position
    @profile
    def index(self, values):
        print("THE NUMBER AT INDEX 2 IS: " , values[2])

    # (c) Replacing the value
    @profile
    def replace(self, values):
        values[1] = 23
        print("THE REPLACED VALUE IS: " , values[1])
        print("")

if __name__=='__main__':
    t = Timer("Array", "from __main__ import Array")
    print("This is the Runtime for this program: " , t.timeit())




