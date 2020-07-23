Saw some post around Python Variable, let me try to explain what is variable when it comes to python

when it comes to python,I wont say variable as a reserved memory location rather it is an reference to a memory location which hold the value ... now if you want to do practical round it then just type below in 
a=20
b=20
id(a)
id(b)
Both will have same mem reference 
now if you delete a
del a
still b refer to same memory reference 

which tell variable are nothing but a reference to a memory location
