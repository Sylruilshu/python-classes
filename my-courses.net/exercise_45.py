
class Computation:

    def __init__(self):
        self.number = 1

    def factorial(self, number):
        x = 1

        for i in range(1, number + 1):
            x = x * i
        return x

    def sum(self, number):
        y = 0

        for i in range(1, number + 1):
            y += i
        return y

    def test_prime(self, number):
        pass


comp = Computation()

print(comp.factorial(3))
