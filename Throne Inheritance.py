class Node:
    def __init__(self, name=""):
        self.name = name
        self.children = []

    def addChild(self, childName):
        self.children.append(childName)

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.people = {}
        self.dead = set()
        self.king = kingName
        king = Node(name=kingName)
        self.people[kingName] = king

    def birth(self, parentName: str, childName: str) -> None:
        parent = self.people[parentName]
        child = Node(name=childName)
        self.people[childName] = child
        parent.addChild(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        return self.getOrder(self.king, [])

    def getOrder(self, name, arr):
        if name not in self.dead:
            arr.append(name)
        person = self.people[name]
        for childName in person.children:
            self.getOrder(childName, arr)
        return arr

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
