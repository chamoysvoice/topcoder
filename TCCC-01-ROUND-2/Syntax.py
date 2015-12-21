class Syntax:
    def match(self, syntaxCheck):
        if len(syntaxCheck) == 0:
            return True
        opening = ['(', '[', '{']
        closing = [')', ']', '}']
        rSyntaxCheck = syntaxCheck
        while len(rSyntaxCheck) > 1:
            print rSyntaxCheck
            valid = False
            remainingOpen = False
            remainingClosed = False
            for x in xrange(len(rSyntaxCheck)):
                if not valid:
                    if rSyntaxCheck[x] in opening:
                        remainingOpen = True
                    if rSyntaxCheck[x] in closing and remainingOpen:
                        remainingClosed = True
                        for y in xrange(x):
                            if rSyntaxCheck[x - y - 1] in opening:
                                if opening.index(rSyntaxCheck[x - y - 1]) == closing.index(rSyntaxCheck[x]):
                                    valid = True
                                    rSyntaxCheck = rSyntaxCheck[:x - y - 1] + rSyntaxCheck[x + 1:]
                                else:
                                    return False
                            if valid:
                                break
                        if not valid:
                            return False
                    elif rSyntaxCheck[x] in closing and not remainingOpen:
                        return False
            if remainingOpen and not remainingClosed:
                return False
        return True

#Test Cases
s = Syntax()
print s.match("x(y(z{test})abc)"), s.match("()"), s.match("([)]"), s.match("[[]](()){{{}}}"), s.match("abc(def(ghi)")