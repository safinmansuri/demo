class employee:
    def __init__(self,name,number,salary,post,address):
        self.name= name
        self.number=number
        self.salary=salary
        self.post=post
        self.address=address

    def getsalary(self):
        print(self.salary)
    def getaddress(self):
        print(self.address)

safin = employee("safin",9173046686,25000,"HR","205 bage masira 2 amber tower")
print(safin.name)
print(safin.post)
print(safin.number)
print(safin.address)
safin.getsalary()
print(safin.salary)
safin.getaddress()