class Fibonacci:
    def __init__(self,max):
        self.max = max

    def __iter__(self):
        self.x, self.y = 1, 1
        return self

    def __next__(self):
        fib = 1
        if fib > self.max:
            raise StopIteration
        self.x, self.y = self.y, self.x + self.y
        return fib

fib = Fibonacci(100)
for i in  fib:
    print(i,end=' ')



