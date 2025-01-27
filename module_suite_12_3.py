import module_12_3
import unittest

testRT = unittest.TestSuite()
testRT.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_3.RunnerTest))
testRT.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(testRT)