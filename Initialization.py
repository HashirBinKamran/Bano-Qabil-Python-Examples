class Python:
    def __init__(self,name,company):
        self.name = name
        self.company = company
    def show(self):
        print("Hello My Name is " +self.name+ " and I " + " work in " +self.company+ " . ")

obj = Python("Ghufran", "Bano Qabil")
obj.show()