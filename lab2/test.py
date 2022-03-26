import unittest
from insertion import insertion_sort
from merge import merge_sort

class sortingTestCase(unittest.TestCase):
    A = [20,50,10,15,40]
    B = [10,20,50,40,15]
    C = [50,40,20,15,10]
    sortedA = [10,15,20,40,50]
    def test_insertion(self):
        insertion_sort(self.A)
        insertion_sort(self.B)
        insertion_sort(self.C)
        self.assertListEqual(self.A,self.sortedA)
        self.assertListEqual(self.B,self.sortedA)
        self.assertListEqual(self.C,self.sortedA)
    
    def test_merge(self):
        merge_sort(self.A,0,4)
        merge_sort(self.B,0,4)
        merge_sort(self.C,0,4)
        self.assertListEqual(self.A,self.sortedA)
        self.assertListEqual(self.B,self.sortedA)
        self.assertListEqual(self.C,self.sortedA)

if __name__ == '__main__':
    unittest.main()