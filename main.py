#Authors:  David Mbugua
#          Caleb Mugisha
#          Pacifique Linda IKIREZI

# Calling the classes
from question1 import Array
from question2_3 import SubArray
from question4 import Associate

# Importing everything from the array module
from array import *

# Declaring the array we used in **Qn1,2,3
values = array('i' , [2, 7, 9, 10, 5])

# Declaring the dictionary **Qn4
dict = {"name": "Kamali", "age": 45}

# Calling methods of the First question
question1 = Array()
question1.length(values)
question1.index(values)
question1.replace(values)

# Calling methods of the First question
question2 = SubArray()
question2.add(values)
question2.delete(values)

# Calling methods of the First question
question3 = SubArray()
question3.check(values)
question3.reverse(values)
question3.insertion(values)

# Calling methods of the First question
question4 = Dictionary()
question4.addition(dict)
question4.remove(dict)
question4.modify(dict)
question4.lookup(dict)

