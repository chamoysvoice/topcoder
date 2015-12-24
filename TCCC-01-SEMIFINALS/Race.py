class Race:
    def closestCheckPoint(self, runner1, runner2, runner3):
        if len(runner1) != len(runner2) or len(runner1) != len(runner3):
            return -1 #as error
        minDiff = 30000 # max value given
        raceRound = 0
        for x in xrange(len(runner1)):
            diff = abs(runner1[x] - runner2[x]) + abs(runner2[x] - runner3[x]) + abs(runner1[x] - runner3[x])
            if(diff <= minDiff):
                minDiff = diff
                raceRound = x
        return raceRound

#Test cases
r = Race()
runner1 = [10,40,90]
runner2 = [12,37,87]
runner3 = [15,32,88]
print r.closestCheckPoint(runner1, runner2, runner3)

runner1 = [3,4,5,8]
runner2 = [3,4,6,8]
runner3 = [3,5,7,8]
print r.closestCheckPoint(runner1, runner2, runner3)
