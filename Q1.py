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
What are python variables? And assignment statement?
Ans:variable:variables are nothing but reversed memory locations to store values. This means that when you created a variable you reverse some space in memory
Python variables (A-Z, 0-9,_)
Variable names are case sensitive (age, Age,AGE) are 3 different variables
Assignment statement:name=expression. The purpose of python's assignment statement is to associate names with values in your program. It is the only statement that does not starting with a keyword. An assignment statement is a line containing at least one single equal sign(=) that is not inside parentheses.
