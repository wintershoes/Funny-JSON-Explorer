# main.py
import sys
import json
from structure_builder import StructureBuilder
from abstract_factories import FactoryProducer

def main():
    json_file = 'example.json'
    style = 'tree'  
    icon_family = 'default'  

    if '-f' in sys.argv:
        json_file = sys.argv[sys.argv.index('-f') + 1]
    if '-s' in sys.argv:
        style = sys.argv[sys.argv.index('-s') + 1]
    if '-i' in sys.argv:
        icon_family = sys.argv[sys.argv.index('-i') + 1]

    with open(json_file, 'r') as file:
        data = json.load(file)

    factory = FactoryProducer()
    icons = factory.create_icon_factory(icon_family)
    visualizer = factory.create_visualizer(style)

    builder = StructureBuilder()
    root = builder.build(data)

    print(visualizer.display(root, icons))

if __name__ == '__main__':
    main()
