class BaseClass:
    def base_func(self):
        print('base class function')

class DerivedClass(BaseClass):
    def derived_func(self):
        print('Derived class function')

obj = DerivedClass()
obj.base_func()
obj.derived_func()

###########################
