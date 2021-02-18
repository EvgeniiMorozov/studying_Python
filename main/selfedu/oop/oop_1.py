
# class A:
#     pass


# a = A()
# print(a)  # <__main__.A object at 0x000001E5022AA0A0>

# a.property1 = 'Property 1'
# a.property2 = 'Property 2'
# print(a.property1)  # Property 1


# class A:
#     property1 = 'Property 1'
#     property2 = 'Property 2'
#
#     def say_hi(self, name='guest'):
#         return 'Hi, ' + name
#
#
# a = A()
# print(a.property1)  # Property 1
# print(a.say_hi('John'))  # Hi, John
# print(a.say_hi())  # Hi, guest


class A:
    property1 = 'Property 1'
    property2 = 'Property 2'
    name = 'guest'

    def say_hi(self, name=''):
        if name:
            return 'Hi, ' + name
        else:
            return 'Hello, ' + self.name


a = A()
print(a.say_hi('John'))  # Hi, John
print(a.say_hi())  # Hello, guest




