import unittest

def IsPolin(string):
    i, j = 0, len(string)-1
    while j > i:
        if string[i] != string[j]:
            return False
        i, j = i+1, j-1
    return True


class TestCompareMethods(unittest.TestCase):

    def test_1(self):
        self.assertEqual(IsPolin('aba'), True)

    def test_2(self):
        self.assertEqual(IsPolin('ab'), False)

    def test_3(self):
        self.assertEqual(IsPolin(''), True)

if __name__ == '__main__':
    #unittest.main()
    suits = unittest.TestLoader().loadTestsFromTestCase(TestCompareMethods)
    unittest.TextTestRunner(verbosity=2).run(suits)