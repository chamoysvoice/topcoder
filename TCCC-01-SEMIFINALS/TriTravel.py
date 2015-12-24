class TriTravel:
    def bestWayDown(self, triangle):
        currentPosition = 0
        total = triangle[0]
        level = 1
        while self.calculateSize(level) < len(triangle):
            start = self.calculateSize(level)
            if triangle[start + currentPosition] < triangle[start + currentPosition + 1]:
                total += triangle[start + currentPosition + 1]
                currentPosition += 1
            else:
                total += triangle[start + currentPosition]
            level += 1
        return total

    def calculateSize(self, level):
        return sum(x for x in xrange(level + 1))

tt = TriTravel()
print tt.bestWayDown([1,6,7,4,-1,6,5,8,9,0])
print tt.bestWayDown([5, 4, 1, 2, 8, -1])