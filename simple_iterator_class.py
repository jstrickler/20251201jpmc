class ABC:
    # responds to iter()
    def __iter__(self):
        return self
    
    # responds to next()
    def __next__(self):
        return 10
    

abc = ABC()
i = iter(abc)
print(f"{i = }")
value = next(i)
print(f"{value = }")


