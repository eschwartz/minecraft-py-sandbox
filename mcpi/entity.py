class Entity:
    """Minecraft PI entity description. Can be sent to Minecraft.setEntity/s"""

    def __init__(self, id, data=0):
        self.id = id
        self.data = data

    def __cmp__(self, rhs):
        return hash(self) - hash(rhs)

    def __eq__(self, rhs):
        return self.id == rhs.id and self.data == rhs.data

    def __hash__(self):
        return (self.id << 8) + self.data

    def withData(self, data):
        return Entity(self.id, data)

    def __iter__(self):
        """Allows a Block to be sent whenever id [and data] is needed"""
        return iter((self.id, self.data))

    def __repr__(self):
        return "Entity(%d, %d)" % (self.id, self.data)


SHEEP = Entity(91)
PARROT = Entity(105)
LLAMA = Entity(103)
