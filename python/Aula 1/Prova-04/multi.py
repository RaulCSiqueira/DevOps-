class A:
    def run(self):
        print('a')

class B(A):
    def run(self):
        print('b')
        
class C(A):
    def run(self):
        print('c')

class D(C, B): ...

if __name__ == '__main__':
    D().run()
    print('as method', D.mro())
    print('attribute', D.__mro__)