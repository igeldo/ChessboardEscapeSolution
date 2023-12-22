
import numpy as np
from setsVectors import SetsVectors

class CoinPuzzle:

    def __init__(self, rows, columns, key, **kwargs):
        super().__init__(**kwargs)
        self._rows= rows
        self._columns=columns
        self._key = key
        self._coinsFloat = (np.random.rand(rows,columns))
        self._coinsBin = self._coinsFloat >= 0.5
        self._coinsFlat = self._coinsBin.flatten()
        self._sets = SetsVectors(self._coinsFlat)

    def keycode(self):
        return bin(self._key)

    def correction(self,actualVal,targetVal):
        aVal = int(actualVal, 2)
        tVal = int(targetVal, 2)
        return bin(aVal ^ tVal)[2:]  # xor-Operator # [2:] deletes prefix '0b'


    def calculate(self):
        actualVal = self._sets.getbits()
        actualVal = int("".join("1" if value else "0" for value in actualVal), 2)
        actualVal = bin(actualVal) #  [2:] deletes prefix '0b'
        targetVal = bin(self._key)
        todo = [bit == '1' for bit in self.correction(actualVal,targetVal)]
        # filling up to 6 values with False for missing MSB
        while len(todo) < 6:
            todo.insert(0, False)
        completeSet = self._sets.getSetGesamt()
        target = completeSet
        # Case differentiation for each bit
        #print(f"todo {todo}")
        if todo[-1]:
            target = target & self._sets.getSet0()
        else:
            target = target & (completeSet - self._sets.getSet0())
        #print(f"set= {target}")
        if todo[-2]:
            target = target & self._sets.getSet1()
        else:
            target = target & (completeSet - self._sets.getSet1())
        #print(f"set= {target}")
        if todo[-3]:
            target = target & self._sets.getSet2()
        else:
            target = target & (completeSet - self._sets.getSet2())
        #print(f"set= {target}")
        if todo[-4]:
            target = target & self._sets.getSet3()
        else:
            target = target & (completeSet - self._sets.getSet3())
        #print(f"set= {target}")
        if todo[-5]:
            target = target & self._sets.getSet4()
        else:
            target = target & (completeSet - self._sets.getSet4())
        #print(f"set= {target}")
        if todo[-6]:
            target = target & self._sets.getSet5()
        else:
            target = target & (completeSet - self._sets.getSet5())
        #print(f"set= {target}")
        return(bin(target.pop()))  # convert a list with an int element into an integer and then into a binary number

    def print(self):
        print(f"key: {self._key} , {self.keycode()}")
        #print(self._coinsBin)
        #print(self._coinsFlat)
        #print(self._sets.getSetGesamt())
        #print(self._sets.getSet0())
        #print(self._sets.getSet1())
        #print(self._sets.getSet2())
        #print(self._sets.getSet3())
        #print(self._sets.getSet4())
        #print(self._sets.getSet5())
        aVal = self._sets.getbits() [2:]  #deletes prefix '0b'
        aVal = int("".join("1" if value else "0" for value in aVal), 2)
        aVal = bin(aVal) [2:]
        tVal = self.keycode() [2:]
        #print(aVal,tVal)
        corr = self.correction(aVal, tVal)
        flip = self.calculate() [2:] # deletes prefix '0b'
        print(f"code: {aVal.rjust(6, '0')} , {int(aVal,2)}")
        print(f"key : {tVal.rjust(6, '0')} , {int(tVal,2)}")
        print(f"corr: {corr.rjust(6, '0')}")
        print(f"flip: {flip.rjust(6, '0')} , {int(flip,2)}")
        self.test(int(flip,2))

    def test(self,flip):
        self._coinsFlat [flip] = not (self._coinsFlat [flip])
        self._sets2 = SetsVectors(self._coinsFlat)
        newVal = self._sets2.getbits()
        newVal = int("".join("1" if value else "0" for value in newVal), 2)
        newVal = bin(newVal)  [2:] # deletes prefix '0b'
        print(f"test: {newVal.rjust(6, '0')} , {int(newVal,2)}")
