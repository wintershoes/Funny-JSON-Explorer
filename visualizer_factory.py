# visualizer_factory.py
from abc import ABC, abstractmethod

class DisplayStyle(ABC):
    @abstractmethod
    def display(self, node, icon_factory):
        pass

class TreeDisplayStyle(DisplayStyle):
    def display(self, node, icon_factory):
        output = []
        self._recursive_display(node, icon_factory, output, "", is_tail=True)
        return "\n".join(output)

    def _recursive_display(self, node, icon_factory, output, indent, is_tail):
        node_icon = icon_factory.get_icon(is_leaf=node.is_leaf())
        line = f"{indent}{'└─ ' if is_tail else '├─ '}{node_icon} {node.key if not node.is_leaf() else f'{node.key}: {node.value}'}"
        output.append(line)
        if not node.is_leaf():
            new_indent = indent + ("   " if is_tail else "│  ")
            children_count = len(node.children)
            for index, child in enumerate(node.children):
                self._recursive_display(child, icon_factory, output, new_indent, index == children_count - 1)

class RectangleDisplayStyle(DisplayStyle):
    def display(self, node, icon_factory):
        output = []
        self._recursive_display(node, icon_factory, output, "", True)
        max_length = max(len(line) for line in output)
        for i in range(len(output)):
            line = output[i]
            line = line[:-2] + "─" * (max_length - len(line)) + line[-2:]
            output[i] = line
        return "\n".join(output)

    def _recursive_display(self, node, icon_factory, output, prefix, is_root):
        node_icon = icon_factory.get_icon(is_leaf=node.is_leaf())
        if is_root:
            output.append(f"┌─ {node_icon}{node.key} ───────────────────────────────┐")
        else:
            output.append(f"{prefix}├─ {node_icon}{node.key} ───────────────────────────┤")
        if not node.is_leaf():
            child_prefix = prefix + "│ "
            for child in node.children:
                self._recursive_display(child, icon_factory, output, child_prefix, False)
        if is_root:
            output.append(f"└───────────────────────────────────────────────┘")

