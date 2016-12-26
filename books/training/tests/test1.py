#	ex1 ::::::::::::::::::::::::::::::::::::::::::::::::::

class Ex1:
	z = 'lsk'
	def x(self, value):
		self.data = value
	def y(self):
		print(self.data)

# ekz = Ex1()
# ekz.x('xxx')
# print(ekz.data) # xxx
# ekz.y()			# xxx

# ekz.data = '---'
# ekz.newatr = 'www'
# print(ekz.data) # ---
# print(ekz.newatr) # www

# print(Ex1.z) 	# 'lsk'

#	ex2 ::::::::::::::::::::::::::::::::::::::::::::::::::

class Ex2(Ex1):
	def y(self):
		print('New value: {}'.format(self.data))

# qqq = Ex2()
# qqq.x('zzz')
# print(qqq.data) # zzz
# qqq.y() 	# New value: zzz

#	ex3 ::::::::::::::::::::::::::::::::::::::::::::::::::

class Ex3(Ex2):
	def __init__(self, value):
		self.data = value
	def __add__(self, other):
		return Ex3(self.data + other)
	def __str__(self):
		return '[Ex3: {}]'.format(self.data)
	def test(self, other):
		self.data *= other

# a = Ex3('abc')
# a.y() 	# New value: abc
# print(a) # [Ex3: abc]

# b = '-ghy-'
# c = a + b	# Новый __add__: создается новый экземпляр
# c.y() 	# New value: abc-ghy-
# print(c) # [Ex3: abc-ghy-]

# a.test(2)
# print(a) # [Ex3: abcabc]
# c.test(3)
# print(c) # [Ex3: abc-ghy-abc-ghy-abc-ghy-]

#	ex4 ::::::::::::::::::::::::::::::::::::::::::::::::::

class Ex4:
	# self.var = 'kdsj'
	atr = 'test'
	def __init__(self, value):
		self.atr = value
	def display(self):
		print(self.atr, Ex4.atr)

# x = Ex4(1)
# y = Ex4(2)

# x.display()	# 1 test
# y.display()	# 2 test

# print(Ex4.var)	# NameError: name 'self' is not defined


#	ex5 ::::::::::::::::::::::::::::::::::::::::::::::::::

class Ex5_1:
	def display():
		print('center')

class Ex5_2(Ex5_1):
	def display():
		print('start')
		Ex5_1.display()
		print('stop')

# Ex5_2.display() # start
# 				# center
# 				# stop

#	ex6 ::::::::::::::::::::::::::::::::::::::::::::::::::

class Super:
	def method(self):
		print('in Super.method')
	def delegate(self):
		self.action()

class Inheriton(Super): pass

class Replacer(Super):
	def method(self):
		print('in Replacer.method')

class Extender(Super):
	def method(self):
		print('starting Extender.method')
		Super.method(self)
		print('ending Extender.method')

class Provider(Super):
	def action(self):
		print('in Provider.action')

if __name__ == '__main__':
	for klass in (Inheriton, Replacer, Extender):
		print('\n' + klass.__name__ + '...')
		klass().method()
	print('\nProvider...')
	x = Provider()
	x.delegate()