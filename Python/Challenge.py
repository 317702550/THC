Python 3.7.3 (default, Mar 27 2019, 13:36:35) 
[GCC 9.0.1 20190227 (Red Hat 9.0.1-0.8)] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> L1=["M","E","E",71]
>>> for l in L1:
	L1.count(l)

	
1
2
2
1
>>> for l in L1:
	L1.count(l)
print("Hay %g M's, %g, E's, %g"%(l1,l2,l3))
SyntaxError: invalid syntax
>>> for l in L1:
	L1.count(l)
print("Hay %g M's, %g, E's, %g"%(l,l,l))
SyntaxError: invalid syntax
>>> for l in L1:
	L1.count(l)
print("Hay %g M's, %g, E's, %g"%(L1[0],L1[1],L1[2]))
SyntaxError: invalid syntax
>>> for l in L1:
	L1.count(l)
print("Hay %g M's, %g, E's, %g 27's"%(L1[0],L1[1],L1[2]))
SyntaxError: invalid syntax
>>> for l in L1:
	L1.count(l)

1
2
2
1
>>> print("Hay %g M's, %g, E's, %g 27's"%(L1[0],L1[1],L1[2]))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print("Hay %g M's, %g, E's, %g 27's"%(L1[0],L1[1],L1[2]))
TypeError: must be real number, not str
>>> print("Hay %g M's, %g, E's, %g 27's"%(L1[0],L1[1],L1[2]))
