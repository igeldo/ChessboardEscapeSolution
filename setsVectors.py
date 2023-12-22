from typing import Set
import numpy as np
class SetsVectors:

    def __init__(self, coins, **kwargs):
        super().__init__(**kwargs)
        # generation of quantities for averaging to find the coin to be flipped
        self._setGesamt = set(range(64))
        self._set0  = set(range(32))
        self._set1  = set(range(0,16)) | set(range(32,48))
        self._set2  = set(range(0, 8)) | set(range(16,24)) | set(range(32,40)) | set(range(48,56))
        self._set3  = set(range(0, 4)) | set(range(8, 12)) | set(range(16,20)) | set(range(24,28)) | set(range(32,36)) | set(range(40,44)) | set(range(48,52)) | set(range(56,60))
        self._set4  = {0,1,4,5,8,9,12,13,16,17,20,21,24,25,28,29,32,33,36,37,40,41,44,45,48,49,52,53,56,57,60,61}
        self._set5  = {0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62}
        self._bits = self.genActVal(coins)

    def genActVal(self,coins):
        # generation of binary vectors for the quantities
        vect0 = [coins[i] for i in self._set0]
        vect1 = [coins[i] for i in self._set1]
        vect2 = [coins[i] for i in self._set2]
        vect3 = [coins[i] for i in self._set3]
        vect4 = [coins[i] for i in self._set4]
        vect5 = [coins[i] for i in self._set5]
        # generation of the bit value (false = even number of trues - true = odd number of trues in vector)
        bit0 = bool(vect0.count(True) % 2 != 0)
        bit1 = bool(vect1.count(True) % 2 != 0)
        bit2 = bool(vect2.count(True) % 2 != 0)
        bit3 = bool(vect3.count(True) % 2 != 0)
        bit4 = bool(vect4.count(True) % 2 != 0)
        bit5 = bool(vect5.count(True) % 2 != 0)
        # provide the bit value from the 6 individual bits
        return([bit5, bit4, bit3, bit2, bit1, bit0])

    def getSetGesamt(self) -> Set:
        return(self._setGesamt)
    def getSet0(self) -> Set:
        return(self._set0)
    def getSet1(self) -> Set:
        return(self._set1)
    def getSet2(self) -> Set:
        return(self._set2)
    def getSet3(self) -> Set:
        return(self._set3)
    def getSet4(self) -> Set:
        return(self._set4)
    def getSet5(self) -> Set:
        return(self._set5)
    def getbits(self) -> bool:
        return(self._bits)