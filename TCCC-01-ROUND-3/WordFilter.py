class WordFilter:
    def strip(self, pattern, buffer):
        pattern = str(pattern)
        buffer = str(buffer)
        if len(pattern) > len(buffer):
            return buffer
        while True:
            found = False
            if len(pattern) > len(buffer):
                break
            for k in xrange(len(buffer) - len(pattern) + 1):
                if buffer[k:len(pattern) + k].lower() == pattern.lower():
                    buffer = buffer[:k] + buffer[len(pattern) + k:]
                    found = True
            if not found:
                break
        return buffer


#Test cases
wf = WordFilter()
print wf.strip("string", "ccccSTRIstringNG ssssssssss")
print wf.strip("string", "ccccstrinstringgsssssssssss")
print wf.strip("string", "ccccstring stringssssssssss")