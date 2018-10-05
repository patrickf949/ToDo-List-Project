
class Mammals:

	def __init__(self):
		pass

	def introduce_mammal(self):
		print("And they are all mammals")


class Dog(Mammals):
	#defines dog

	population=0#class variable that stores number of dogs
	def __init__(self, name, age):
		"""
		Get dog information
		params: dog name, and age
		returns: n/a
		"""
		self.name = name
		self.age = age
		self.hungry=True
		Dog.population+=1#increase dog population every time an instance of this class is initialised
	
	def introduce_dog(self):
		"""
		Tell the world about the said dog
		params: n/a
		returns: n/a
		"""
		print("{0} is {1} years old".format(self.name,self.age))
	
	def announce_num_of_dogs(self):
		"""
		Tell the world how many dogs i have
		params: n/a
		return: n/a
		"""
		print("I have {0} dogs".format(Dog.population))

	def eat(self):
		"""
		feeds dog
		params: n/a
		returns: n/a
		"""
		self.hungry=False
		Dog.population-=1
		if Dog.population==0:
			print("All my dogs are hungry")

class Pet():
	
	def __init__(self, name, age):
		"""
		Get pet information
		params: dog name, and age
		returns: n/a
		"""
		Dog.__init__(self,name,age)
		Pet.announce_num_of_Pets(self)

	def announce_num_of_Pets(self):
		"""
		Tell number of pets
		params:n/a
		returns:n/a
		"""
		Dog.announce_num_of_dogs(self)

	def announce_pet(self):
		Dog.introduce_dog(self)

	def feed(self):
		"""
		feeds pet
		params: n/a
		returns:n/a
		"""
		Dog.eat(self)
		

#def main():
	#start application
T= Pet("Tom",6)
F= Pet("Fletcher",7)
L=Pet("Larry",9)



petlist=[T,L,F]
for i in petlist:
	i.announce_pet()
	i.feed()
	print(Dog.population)

if Dog.population==0:
	#if all dogs have been fed
	print("My dogs are not hungry")
else:
	#if any dog is still hungry
	print("My dogs are hungry")

# if __name__ == '__main__':
# 	main()
	