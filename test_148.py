class Judge:
    def __init__(self,a,b):
        self.a=a
        self.b=b


    def judge(self):
        return self.a is self.b


aaa=Judge("apple","big")
bbb=Judge("big","big")

print(aaa.judge())
print(bbb.judge())




def test(a,b):
    ans=a is b
    return ans

print(test("am","am"))
print(test("am","be"))
