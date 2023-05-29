from model.importLib.importAll import *
import unittest


class Test_sortAlgo(unittest.TestCase):

    def setUp_list(self):
        tabTest = [4,5,6,8,7,2,5,4,1,3,2,5,6,9,8,7,2,3,5,4,9,9,9,1,4,5,7,2]
        for i in range(len(tabTest)):
            tabTest[i] = FloatCompare(float(tabTest[i]))
        tabTest = MonitoredList(tabTest)
        return tabTest

    def test_Bubblesort(self):
        test = BubbleSort(self.setUp_list())
        #sort_test
        self.assertListEqual(test.sort(), sorted(test.sort()))
    
    def test_CountingSort(self):
        test = CountingSort(self.setUp_list())
        #sort_test
        self.assertListEqual(test.sort(), sorted(test.sort()))

    def test_SelectionSort(self):
        test = SelectionSort(self.setUp_list())
        #sort_test
        self.assertListEqual(test.sort(), sorted(test.sort()))
    
    def test_InsertionSort(self):
        test = InsertionSort(self.setUp_list())
        #sort_test
        self.assertListEqual(test.sort(), sorted(test.sort()))
    
    def test_QuickSort(self):
        test = QuickSort(self.setUp_list())
        #sort_test
        self.assertListEqual(test.sort(), sorted(test.sort()))

    def test_MergeSort(self):
        test = MergeSort(self.setUp_list())
        #sort_test
        self.assertListEqual(test.sort(), sorted(test.sort()))

    def test_HeapSort(self):
        test = HeapSort(self.setUp_list())
        #sort_test
        self.assertListEqual(test.sort(), sorted(test.sort()))

    def test_ShellSort(self):
        test = ShellSort(self.setUp_list())
        #sort_test
        self.assertListEqual(test.sort(), sorted(test.sort()))
    
    def test_GnomeSort(self):
        test = GnomeSort(self.setUp_list())
        #sort_test
        self.assertListEqual(test.sort(), sorted(test.sort()))

    def test_PancakeSort(self):
        test = PancakeSort(self.setUp_list())
        #sort_test
        self.assertListEqual(test.sort(), sorted(test.sort()))

    def test_CombSort(self):
        test = CombSort(self.setUp_list())
        #sort_test
        self.assertListEqual(test.sort(), sorted(test.sort()))

    
    
    
    
        