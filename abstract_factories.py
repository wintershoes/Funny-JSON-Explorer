# abstract_factories.py
from abc import ABC, abstractmethod
from icon_factory import IconFactory
from visualizer_factory import DisplayStyle, TreeDisplayStyle, RectangleDisplayStyle

class AbstractFactory(ABC):
    @abstractmethod
    def create_icon_factory(self, family):
        pass

    @abstractmethod
    def create_visualizer(self, style):
        pass

class FactoryProducer(AbstractFactory):
    def create_icon_factory(self, family):
        return IconFactory(family)

    def create_visualizer(self, style):
        if style == 'tree':
            return TreeDisplayStyle()
        elif style == 'rectangle':
            return RectangleDisplayStyle()
        else:
            raise ValueError("Unknown visualization style")
