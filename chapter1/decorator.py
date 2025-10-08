def hello():
    print("hello")
def deco(fn):
    def deco_hello():
        print("*" * 20)
        fn()
        print("*" * 20)
    return deco_hello
@deco
def hello2():
    print("hello 2")
hello()
deco_hello = deco(hello)
deco_hello()
hello = deco(hello)
hello()
hello2()