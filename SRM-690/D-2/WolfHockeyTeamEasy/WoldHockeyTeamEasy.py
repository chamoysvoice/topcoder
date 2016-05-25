from itertools import permutations
import unittest

# correct result, but super slow, permutation is exponential // maybe some math will cheer this up?
class WolfHockeyTeamEasy:
    @staticmethod
    def count(n, k):
        if k > n * 2 - 2: # impossible to find "nice" photos
            return 0
        different = []
        wolves = [x for x in xrange(n*2)]
        for combination in permutations(wolves): #generator :D
            if max(combination[0:n]) < k or max(combination[n:2*n]) < k:
                continue
            current_photo = []
            for i in xrange(n):
                current_photo.append(max(combination[i], combination[n + i]))
            current_photo.append(max(combination[0:n]))
            current_photo.append(max(combination[n:2*n]))
            if current_photo not in different:
                different.append(current_photo)
        return len(different) % 1000000007 #topcoder asks it

class TestWolfHockeyTeamEasy(unittest.TestCase):
    def test_one(self):
        self.assertEqual(1104, WolfHockeyTeamEasy.count(4, 5))
    """ #Ultra SLOW, bad idea to use permutations :v
        def test_two(self):
            self.assertEqual(803057135, WolfHockeyTeamEasy.count(100, 120))
    """
    def test_three(self):
        self.assertEqual(0, WolfHockeyTeamEasy.count(234, 467))


if __name__ == "__main__":
    unittest.main()
