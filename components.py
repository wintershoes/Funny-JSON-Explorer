#components.py
class JsonComponent:
    def draw(self, icon_factory, style):
        raise NotImplementedError("Must implement draw method.")

class Composite(JsonComponent):
    def __init__(self, key):
        self.key = key
        self.children = []

    def add(self, component):
        self.children.append(component)

    def draw(self, icon_factory, style):
        return style.display(self, icon_factory)

    def is_leaf(self):
        return False  # Composite is never a leaf

class Leaf(JsonComponent):
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def draw(self, icon_factory, style):
        return style.display(self, icon_factory)

    def is_leaf(self):
        return True  # Leaf is always a leaf
