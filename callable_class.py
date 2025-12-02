class Hi:
    def __call__(self):
        print("Hi, Mom!")

h = Hi()
h()  # call the instance, not a method
