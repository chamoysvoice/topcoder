class Area:
    def __init__(self):
        self.coords = list()
        self.figures = list()
        self.lastKnown = 0
        self.visited = [[0 for x in range(21)] for y in range(21)]

    def totalEnclosed(self, x, y, path):
        self.coords.append([x, y])
        currentPos = 0
        area = 0
        for direction in path:

            if direction == 'L':
                x -= 1
            elif direction == 'R':
                x += 1
            elif direction == 'U':
                y -= 1
            elif direction == 'D':
                y += 1
            else:
                return 0
            if x < -10 or x > 10 or y < -10 or y > 10:
                return 0

            currentPos += 1
            if [x, y] in self.coords:
                self.figures.append(list(self.coords[self.lastKnown:]))
                self.lastKnown = currentPos

            self.coords.append([x, y])

        for figure in self.figures:
            max_x = -10
            max_y = -10
            min_x = 10
            min_y = 10
            for coords in figure:
                if coords[0] < min_x:
                    min_x = coords[0]
                if coords[0] > max_x:
                    max_x = coords[0]

                if coords[1] < min_y:
                    min_y = coords[1]
                if coords[1] > max_y:
                    max_y = coords[1]

            area += (max_y - min_y) * (max_x - min_x)

        return area


area = Area()
print area.totalEnclosed(0, 0, "RRUULLDDDDL")
# TODO fix other cases
