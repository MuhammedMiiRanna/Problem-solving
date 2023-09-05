# Define a custom exception class
class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Vector:
    # TODO Finish the Vector class.
    @classmethod
    def check(cls, V1, V2):
        if len(V1.vector) != len(V2.vector):
            raise CustomException("Length is different between the two vectors...")

    def __init__(self, vector):
        self.__vector = vector

    @property
    def vector(self):
        return self.__vector

    def add(self, vector):
        Vector.check(self, vector)
        return Vector([v1 + v2 for v1, v2 in zip(self.vector, vector.vector)])

    def subtract(self, vector):
        Vector.check(self, vector)
        return Vector([v1 - v2 for v1, v2 in zip(self.vector, vector.vector)])

    def dot(self, vector):
        Vector.check(self, vector)
        return sum([v1 * v2 for v1, v2 in zip(self.vector, vector.vector)])

    def norm(self):
        return sum([v**2 for v in self.vector]) ** (1 / 2)

    def __eq__(self, vector) -> bool:
        for v1, v2 in zip(self.vector, vector.vector):
            if v1 != v2:
                return False
        return True

    def equals(self, vector):
        return self == vector

    def __str__(self) -> str:
        return "(" + ",".join([str(v) for v in self.vector]) + ")"


a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

print(str(a))

# a.add(b)  # should return a new Vector([4, 6, 8])
# a.subtract(b)  # should return a new Vector([-2, -2, -2])
# a.dot(b)  # should return 1*3 + 2*4 + 3*5 = 26
# a.norm()  # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
# # a.add(c)  # raises an exception
