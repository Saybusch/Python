class CiagGeometryczny():
    def __init__(self, pierwszy, iloraz):
        self.pierwszy = pierwszy
        self.iloraz = iloraz
    def kolejne_wyrazy(self, ileWyrazow):
        return [self.pierwszy * self.iloraz**x for x in range(ileWyrazow)]