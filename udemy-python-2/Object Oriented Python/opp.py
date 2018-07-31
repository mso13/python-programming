class Kettle(object):

	def __init__(self, make, price):
		self.make = make
		self.price = price
		self.on = False

	def show_info(self):
		print('->Make: ' + self.make + '\n->Price: $', self.price)

	def switch_on(self):
		self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.show_info()

print(kenwood.on)
kenwood.switch_on()
print(kenwood.on)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))