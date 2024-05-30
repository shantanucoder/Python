class Vector2D:
    def __init__(self, i, j) -> None:
        self.i = i 
        self.j = j

    def printVector(self):
        print(f"{self.i}i + {self.j}j")
        
class Vector3D(Vector2D):
    def __init__(self, i, j , k):
        super().__init__(i, j)
        self.k = k

    def printVector(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")


V2 = Vector2D(1, 5)
V3 = Vector3D(11, 5, 9)

V2.printVector()
V3.printVector()
