class A:
    def _init_(self, a, b, c):
        self.__a = a  
        self._b = b   
        self.c = c    
    
    def display(self):
        print("Class A:")
        print("a =", self.__a)
        print("b =", self._b)
        print("c =", self.c)

class B(A):  #inheriting class A
    def display(self):
        print("Class B:")
        try:
            print("a =", self.__a)  
        except AttributeError:
            print("Cannot access private member a of class A")
        print("b =", self._b)
        print("c =", self.c)


a = A(10,20,30)
b = B(40,50,60)
a.display()
b.display()