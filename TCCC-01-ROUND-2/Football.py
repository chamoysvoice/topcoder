class Football:
    def __init__(self):
        self.pastAnswers = dict()
        self.pastAnswers[2] = [[2]]
        self.pastAnswers[3] = [[3]]
        self.pastAnswers[7] = [[7], [2,2,3]]

    def fetchCombinations(self, n):
        if n == 0:
            return [[]]
        if self.pastAnswers.has_key(n):
            return self.pastAnswers[n]
        combinations = []
        scores = [2, 3 ,7]
        for score in scores:
            if n - score >= 0:
                prev = self.fetchCombinations(n - score)
                for comb in prev:
                    t = comb[:]
                    t.append(score)
                    t.sort()
                    if t not in combinations:
                        combinations.append(t)
        self.pastAnswers[n] = combinations
        return combinations

# Test cases
f = Football()
print 1, f.fetchCombinations(1)
print 4, f.fetchCombinations(4)
print 9, f.fetchCombinations(9)
print 11,f.fetchCombinations(11)

