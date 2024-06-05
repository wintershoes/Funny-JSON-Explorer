from components import Composite, Leaf

class StructureBuilder:
    def __init__(self):
        self.root = None

    def build(self, data, key="root"):
        if isinstance(data, dict):
            node = Composite(key)
            for k, v in data.items():
                child = self.build(v, k)
                node.add(child)
        elif isinstance(data, list):
            node = Composite(key)
            for i, item in enumerate(data):
                child = self.build(item, f"index-{i}")
                node.add(child)
        else:
            node = Leaf(key, data)
        return node