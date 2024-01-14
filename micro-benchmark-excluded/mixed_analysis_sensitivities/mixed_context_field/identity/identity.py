# A class Identity is defined that can store different types of values in a member variable value.
# The constructor takes an initial value as a parameter, and the get_value method returns the current value of the value member variable.
# This is field-sensitive , allowing the value member variable to store different types of values in different contexts.


class Identity:
    def __init__(self, x):
        self.value = x

    def get_value(self):
        return self.value


class ValueStore:
    def __init__(self, a):
        self.a = a


op1 = ValueStore(5)
op2 = ValueStore("Hello")

id1 = Identity(op1.a)
id2 = Identity(op2.a)

result1 = id1.get_value()
result2 = id2.get_value()
