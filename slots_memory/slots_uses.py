#in Python every class can have instance attributes. By default Python uses a dict
#  to store an object’s instance attributes. This is really helpful as it allows
# setting arbitrary new attributes at runtime.

#However, for small classes with known attributes it might be a bottleneck.
#  The dict wastes a lot of RAM. Python can’t just allocate a static amount of memory at object
# creation to store all the attributes. Therefore it sucks a lot of RAM if you create a lot of objects
#  (I am talking in thousands and millions). Still there is a way to circumvent this issue.
# It involves the usage of __slots__ to tell Python not to use a dict, and
# only allocate space for a fixed set of attributes. Here is an example with and without __slots__:
import pdb
class test_without_slots(object):
    def __init__(self,*args):
        self.id = args[0]
        self.first_name = args[1]
        self.last_name = args[2]
        self.year_of_joing = args[3]

    def __str__(self):
        return str(self.id)

    def details(self):
        return id , self.first_name + ' ' + self.last_name


class test_with_slots(object):

    __slots__ = ['id','first_name','last_name','year_of_joing']

    def __init__(self,*args):
        self.id = args[0]
        self.first_name = args[1]
        self.last_name = args[2]
        self.year_of_joing = args[3]

    def __str__(self):
        return str(self.id)

    def details(self):
        return id, self.first_name + ' ' + self.last_name

if __name__ == "__main__":
    obj_with_out_slots = test_without_slots(1,'suraj','singh','2010')
    obj_with_slots = test_with_slots(1,'suraj','singh','2010')
    print(obj_with_out_slots)
    print(obj_with_slots)

