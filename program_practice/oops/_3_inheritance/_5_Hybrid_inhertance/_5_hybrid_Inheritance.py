class A:
    def a(self):
        print("A Class")

class B(A):
    def b(self):
        print("B Class")


class C(A):
    def c(self):
        print("C Class")

class D(B):
    def d(self):
        print("D Class")

class E(B):
    def e(self):
        print("E Class")

class F(C):
    def f(self):
        print("F Class")

class G(E,F):
    def g(self):
        print("G Class")



a_obj =A()
a_obj.a()
print()


b_obj =B()
b_obj.b()
b_obj.a()
print()

c_obj=C()
c_obj.c()
c_obj.a()
print()

d_obj =D()
d_obj.d()
d_obj.b()
d_obj.a()
print()

e_obj = E()
e_obj.e()
e_obj.b()
e_obj.a()
print()

f_obj =F()
f_obj.f()
f_obj.c()
f_obj.a()
print()

g_obj = G()
g_obj.a()
g_obj.b()
g_obj.c()
g_obj.e()
g_obj.f()
g_obj.g()
print()




