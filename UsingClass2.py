class Rider():
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return self.name
    def __add__(self, other):
        return self.name+" "+other.name

class Horse():
    def __init__(self,name,rid):
        self.name=name
        self.rider=rid

rd=Rider("Mike")
print(rd)
hr=Horse("Agat",rd)
print("Horse {} has rider {}".format(hr.name,hr.rider.name))

print(rd+hr)



