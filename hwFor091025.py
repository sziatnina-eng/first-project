class Animal:
  def __init__(self, name, size):
    self.name = name
    self._size = size

  def get_size(self):
    return self._size

  def set_size(self, size):
    self._size = size

class Mouse(Animal):
  def __init__(self, name, size, tail):
    super().__init__(name, size)
    self._tail = tail


  def get_tail(self):
    return self._tail

  def set_tail(self, tail):
    self._tail = tail

mouse = Mouse('Cat', 8, "short")

print(mouse.name)
print(mouse.get_size())
print(mouse.get_tail())

mouse.set_size(12)
mouse.set_tail("long")

print("Updated Size:", mouse.get_size())
print("Updated Tail:", mouse.get_tail())

