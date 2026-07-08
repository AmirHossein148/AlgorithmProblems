class editor:
    def __init__(self, string):
        self.string = list(string)
        self.sign = 0
        self.maxsize = len(string)

    def next(self):
        if self.sign == self.maxsize - 1:
            return
        self.sign += 1

    def prev(self):
        if self.sign == 0:
            return
        self.sign -= 1

    def add(self, val):
        self.string.insert(self.sign, val)
        self.sign += 1


n = int(input())
Word = editor('')
for i in range(n):
    inp = list(input().split())
    if inp[0] == 'insert':
        Word.add(inp[1])
    elif inp[0] == '+':
        Word.next()
    else:
        Word.prev()

print(*Word.string, sep='')

