from model.generator.Generator import Generator
import unittest
import numpy


class Test_Generator(unittest.TestCase):

    def test_createIntegerValuesList(self):
        test = Generator()
        print()
        #type_test
        self.assertIsInstance(test.createIntegerValuesList(3, 20, 44), list)
        #len_test
        self.assertEqual(len(test.createIntegerValuesList(3, 20, 44)), 44)
        for value in test.createIntegerValuesList(3, 20, 44):
            #type_value_test
            self.assertIsInstance(value, numpy.int64)
            #less_value_test
            self.assertLessEqual(value, 20)
            #greater_value_test
            self.assertGreaterEqual(value, 3)
    
    def test_createIntegerValuesListRange(self):
        test = Generator()
        #type_test
        self.assertIsInstance(test.createIntegerValuesListRange(3, 20), list)
        #len_test
        self.assertEqual(len(test.createIntegerValuesListRange(3, 20)),(20-3)+1 )
        for value in test.createIntegerValuesListRange(3, 20):
            #type_value_test
            self.assertIsInstance(value, int)
            #less_value_test
            self.assertLessEqual(value, 20)
            #greater_value_test
            self.assertGreaterEqual(value, 3)

    def test_createFloatValuesListEntropy(self):
        test = Generator()
        #type_test
        self.assertIsInstance(test.createFloatValuesListEntropy(3, 44), list)
        #len_test
        self.assertEqual(len(test.createFloatValuesListEntropy(3, 44)), 44 )
        for value in test.createFloatValuesListEntropy(3, 20):
            #type_value_test
            self.assertIsInstance(value, float)


        

    

