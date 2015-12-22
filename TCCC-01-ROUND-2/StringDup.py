class StringDup:
    def getMax(self, dupString):
        if len(dupString) == 0:
            return ''
        freq = dict()
        for ltr in dupString:
            if ltr in freq.keys():
                freq[ltr] += 1
            else:
                freq[ltr] = 1
        maxVal = 0
        maxLtr = ''
        for ltr in freq:
            if freq[ltr] > maxVal:
                maxLtr = ltr
                maxVal = freq[ltr]
        return maxLtr

#Test Cases
s = StringDup()
print s.getMax("aaiicccnn"), s.getMax("aabbccdd"), s.getMax("ab2sbf2dj2skl")