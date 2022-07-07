class P:
    def __init__(self) -> None:
        self.data=["a"]
    def isEmpty(self):
        return len(self.data)==0
A=P()
print(A.isEmpty())
while not P.isEmpty :
    A.data.pop()
print(A.data)