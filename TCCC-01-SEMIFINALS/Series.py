class Series:
    def increasingLength(self, series):
        if len(series) < 2:
            return (len(series))
        longest = 1
        buffer = 1
        for x in range(1, len(series)):
            prev = series[x - 1]
            if prev < series[x]:
                buffer += 1
            else:
                if buffer > longest:
                    longest = buffer
                buffer = 1
        return longest

s = Series()
print s.increasingLength([-4, 5, -2, 0, 4, 5, 9, 9])
print s.increasingLength([1, 0])