import unittest
from kadene import maxSubArraySum, maxSubArraySumSpaceImproved


class Test(unittest.TestCase):

    def assert_both_methods(self, l, sol):
        self.assertEqual(sol, maxSubArraySum(l))
        self.assertEqual(sol, maxSubArraySumSpaceImproved(l))

    def testEmptyList(self):
        l = []
        self.assertRaises(Exception, maxSubArraySum, l)
        self.assertRaises(Exception, maxSubArraySum, l)

    def testOneElementList(self):
        l = [5]
        self.assert_both_methods(l, 5)

    def testOneNegativElementList(self):
        l = [-5]
        self.assert_both_methods(l, -5)

    def testSkippableNegativeNumbers(self):
        l = [-10, 5, -10]
        self.assert_both_methods(l, 5)

    def testMultiplePositiveNumbers(self):
        l = [5, 10, 15, 10, 5]
        self.assert_both_methods(l, 45)

    def testMultipleNegativeNumbers(self):
        l = [-5, -10, -15, -10, -5]
        self.assert_both_methods(l, -5)

    def testLargerExample1(self):
        l = [300, -10, 5, -10, 200, -5, -5, -5, 200]
        self.assert_both_methods(l, 670)

    def testLargerExample2(self):
        l = [300, -10, 5, -10, -1000, 200, -5, -5, -5, 200]
        self.assert_both_methods(l, 385)

if __name__ == "__main__":
    unittest.main()