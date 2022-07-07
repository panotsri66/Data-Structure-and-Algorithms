class A:
    __slots__= 'key','value'
    def __init__(self,k,v):
        self.key=k
        self.value=v

c=A(1,2)
'''class Base(object): 
    __slots__ = ()
class Child(Base):
    __slots__ = ('a',)
class SlottedWithDict(Child): 
    __slots__ = ('__dict__', 'b')

swd = SlottedWithDict()
swd.a = 'a'
swd.b = 'b'
swd.c = 'c' '''