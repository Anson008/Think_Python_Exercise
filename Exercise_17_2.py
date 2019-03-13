class Kangeroo:
    def __init__(self, name, contents=None):
        self.name = name
        if contents is None:
            contents = []
        self.pouch_contents = contents

    def __str__(self):
        t = [self.name + " has pouch contents:"]
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        self.pouch_contents.append(item)


kanga = Kangeroo("hanga")
kanga.put_in_pouch("apple")
print(kanga)

roo = Kangeroo("roo")
roo.put_in_pouch("peach")
print(roo)

kanga.put_in_pouch(roo)
print(kanga)
