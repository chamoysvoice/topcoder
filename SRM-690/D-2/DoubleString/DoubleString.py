import unittest


class DoubleString:
    def __init__(self):
        pass

    @staticmethod
    def check(string):
        """
        Oneliner to solve the problem.
        :param string:
        :return: "square" or "not square"
        """
        return "\"square\"" if len(string) % 2 == 0 \
                               and string[:len(string)/2] == string[len(string)/2:len(string)] else "\"not square\""


class TestDoubleString(unittest.TestCase):
    def test_one(self):
        self.assertEqual("\"square\"", DoubleString.check("MAZAIMAZAI"), "MAZAIMAZAI -> square")

    def test_two(self):
        self.assertEqual("\"not square\"", DoubleString.check("MAMAZAIZAI"), "MAMAZAIZAI -> not square")

    def test_three(self):
        self.assertEqual("\"not square\"", DoubleString.check("IOI"), "IOI -> not square")

    def test_four(self):
        self.assertEqual("\"square\"", DoubleString.check("AA"), "AA -> square")

    def test_five(self):
        self.assertEqual("\"not square\"", DoubleString.check("ABCCBA"), "ABCCBA -> not square")

    def test_six(self):
        self.assertEqual("\"not square\"", DoubleString.check("Y"), "Y -> not square")

if __name__ == "__main__":
    unittest.main()
