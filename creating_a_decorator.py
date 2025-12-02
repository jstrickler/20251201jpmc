from functools import wraps
from datetime import datetime

def timestamp(f):

    @wraps(f)
    def _wrapper(*args, **kwargs):
        print(datetime.now().ctime())  # log time
        return f(*args, **kwargs)

    return _wrapper

@timestamp
def spam():
    print("SPAM SPAM SPAM")
    return 42

@timestamp
def ham(repeat_count):
    print("HAM" * repeat_count)

# spam = timestamp(spam)
# ham = timestamp(ham)

s = spam()
print(f"{s = }")

ham(3)
ham(10)
print(f"{spam.__name__ = }")
print(f"{ham.__name__ = }")
