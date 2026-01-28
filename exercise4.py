
class Dog:
  def __init__(self, legs_length, arms, tail, eyes, fur):
    self.legs_length = legs_length
    self.arms = arms
    self.tail = tail
    self.eyes = eyes
    self.fur = fur

    def characteristics(self):
    	doggy = Dog(4.0, None, 'long', 2, 'furry')

print(type(doggy.legs_length))
print(doggy.legs_length)
print(doggy.arms)
print(bool(doggy.arms))
print(doggy.tail)
print(type(doggy.tail))
print(doggy.eyes)
print(type(doggy.eyes))
print(doggy.fur)
print(bool(doggy.fur))


