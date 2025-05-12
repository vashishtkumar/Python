class A:
    A="hi I am A"

class B:
    B="hi I am B"

class C(A,B):
    C="hi I am C"


obj1=C()

print(obj1.C)
print(obj1.B)
print(obj1.A)