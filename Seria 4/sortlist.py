class SortedList(list):
    def __init__(self,lista,sorttype=False):
        self.sorttype=sorttype
        lista.sort(reverse=self.sorttype)
        super().__init__(lista)
    def _sort(self):
        self.sort(reverse=self.sorttype)
        return self
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self._sort
    def append(self, *value):
        super().append(value)
        self._sort
    def extend(self, value):
        super().extend(value)
        self._sort
    def pop(self,*lit):
        super().pop(*lit)
        self._sort
import sys
args = sys.argv[1:]
for a,i in enumerate(args):
    args[a] = float(i)
i = SortedList(args)
print(i)
i = SortedList(args,True)
print(i)
