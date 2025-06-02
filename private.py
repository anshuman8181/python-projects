class myclass:
    __privateVar = 27

    def  __privMeth(self):
        print("I am inside myclass")

    def hello(self):
        print("Private Variable value:",myclass.__privateVar)


foo = myclass()
foo.hello()
foo.__privMeth

