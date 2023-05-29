import unittest
from unittesting.Test_Generator import Test_Generator
from unittesting.Test_sortAlgo import Test_sortAlgo



class Run_tests(unittest.TestCase):
    
    def display_tests(self):
            print("Choisissez un test à exécuter :")
            print("0. Test_All")
            print("1. Test_Generator")
            print("2. Test_sortAlgo")

            choice = input("Entrez le numéro du test choisi : ")
            if choice == "0":
                self.run_test(Test_Generator)
                self.run_test(Test_sortAlgo)
            elif choice == "1":
                self.run_test(Test_Generator)
            elif choice == "2":
                self.run_test(Test_sortAlgo)
            else:
                print("Choix invalide")

    def run_test(self, test_class):
        suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)
    
    

    




        
