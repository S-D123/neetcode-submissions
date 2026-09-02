class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [None] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        for i in range(len(self.arr)):
            if self.arr[i] == None: 
                self.arr[i] = n
                return
        
        self.resize()
        self.arr[len(self.arr)//2] = n
        return

    def popback(self) -> int:
        for i in range(len(self.arr)):
            if self.arr[i] == None: 
                val = self.arr[i-1]
                self.arr[i-1] = None
                return val

        last = len(self.arr)-1
        k = self.arr[last]
        self.arr[last] = None
        return k

    def resize(self) -> None:
        pass
        self.arr += [None] * len(self.arr)

    def getSize(self) -> int:
        for i in range(len(self.arr)):
            if self.arr[i] == None:
                return i

        return len(self.arr)
    
    def getCapacity(self) -> int:
        return len(self.arr)
