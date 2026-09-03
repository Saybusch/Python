class CiagArytmetyczny():
    def __init__(self, pierwszy, difference):
        self.pierwszy = pierwszy
        self.difference = difference
    def kolejne_wyrazy(self, ileWyrazow):
        return [self.pierwszy + x*self.difference for x in range(ileWyrazow)]
ciag = CiagArytmetyczny(2, 3)
print(ciag.kolejne_wyrazy(10))