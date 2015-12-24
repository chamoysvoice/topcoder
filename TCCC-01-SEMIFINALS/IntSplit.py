class IntSplit:
    def maxSplit(self, tosplit, target):
        if tosplit < target:
            return tosplit
        stringSplit = str(tosplit)
        splits = [0 for x in range(len(stringSplit) - 1)]
        total = 0
        binarySplitField = 0
        while binarySplitField < 2 ** (len(stringSplit) - 1) - 1:
            option = []
            binarySplitField += 1
            for x in range(0, len(stringSplit) - 1):
                splits[x] = (binarySplitField >> (len(stringSplit) - x - 2)) % 2 == 1
            start = 0
            for x in xrange(len(splits)):
                if splits[x]:
                    option.append(int(stringSplit[start: x + 1]))
                    start = x + 1
            option.append(int(stringSplit[start:]))
            if not sum(option) > target:
                if sum(option) > total:
                    total = sum(option)
        return total

iS = IntSplit()
print iS.maxSplit(19967, 1000)
print iS.maxSplit(19967, 100)
print iS.maxSplit(22215, 225)