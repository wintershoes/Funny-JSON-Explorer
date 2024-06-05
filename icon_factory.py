#icon_factory.py
class IconFactory:
    def __init__(self, family):
        self.family = family

    def get_icon(self, is_leaf=False):
        if self.family == 'poker-face':
            return '♢' if not is_leaf else '♤'
        return '○' if not is_leaf else '●'