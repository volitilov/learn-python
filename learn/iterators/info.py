#	iterators ::::::::::::::::::::::::::::::::::::::::::::::::::::::

#	объект считается итерируемым, либо если он физически является 
#	последовательностью, либо если он является объектом, который 
#	воспроизводит по одному результату за раз в контексте инструментов 
#	выполнения итераций, таких как цикл for. В некотором смысле в 
#	категорию итерируемых объектов входят как физические 
#	последовательности, так и  последовательности виртуальные, которые 
#	вычисляются по требованию.

#	....................................
f = open('test.py')

f.readline()
f.__next__()
next(f)
iter(f)		# True

#	....................................
t = [1, 2, 3]

iter(t)		# False

#	....................................
D = {'a': 1, 'b': 2, 'c': 3}

iter(D)		# False
next(iter(D))
for key in D: ...