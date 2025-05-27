class person():
    def __init__(self,n,id):
        self.n=n 
        self.id=id
    def display(self):
        print(self.n)
        print(self.id)

class emp(person):
    def __init__(self,n,id,sal,post):
        self.sal=sal
        self.post=post
        person.__init__(self,n,id)

obj=emp("Nihitha",1234,670000,"Manager")
obj.display()