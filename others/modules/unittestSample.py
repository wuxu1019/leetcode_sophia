import unittest

def IsPolin(string):
    i, j = 0, len(string)-1
    while j > i:
        if string[i] != string[j]:
            return False
        i, j = i+1, j-1
    return True


class TestCompareMethods(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(IsPolin('aba'), True)

    def test_2(self):
        self.assertEqual(IsPolin('ab'), False)

    def test_3(self):
        self.assertEqual(IsPolin(''), True)

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'Hello world'
        self.assertEqual(s.split(), ['Hello', 'world'])



if __name__ == '__main__':
    #     # Three ways to run tests
    # # first way, run all tests using uinttest.main()
    unittest.main()
#
#     # second way
#    suits = unittest.TestLoader().loadTestsFromTestCase(TestCompareMethods)
#    unittest.TextTestRunner(verbosity=2).run(suits)

#     # third way
#     polintestsuit = unittest.TestSuite()
#     polintestsuit.addTest(TestCompareMethods("test_1"))
#     polintestsuit.addTest(TestCompareMethods("test_2"))
#     polintestsuit.addTest(TestCompareMethods("test_3"))
#
#     runtest = unittest.TextTestRunner()
#     runtest.run(polintestsuit)
