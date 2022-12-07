# from anytree import Node, RenderTree

# udo = Node("/")
# marc = Node("Marc", parent=udo)
# lian = Node("Lian", parent=marc)
# dan = Node("Dan", parent=udo)
# jet = Node("Jet", parent=dan)
# jan = Node("Jan", parent=dan)
# joe = Node("Joe", parent=dan)

# print(udo)
# Node('/Udo')
# print(joe)
# Node('/Udo/Dan/Joe')

# for pre, fill, node in RenderTree(udo):
#     print("%s%s" % (pre, node.name))\

# from collections import defaultdict
# infinite_defaultdict = lambda: defaultdict(infinite_defaultdict)
# d = infinite_defaultdict() 
# d['x']['y']['z'] = 10
# print(d['x'])

class NestedDict(dict):
    def __getitem__(self, key):
        if key in self:
            return self.get(key)
        return self.setdefault(key, NestedDict())

    def __add__(self, other):
        return other

    def __sub__(self, other):
        return other

test = NestedDict()
test
{}
test['a']['b'] = 1
test
{'a': {'b': 1}}
test['a']['b'] += 1
test
{'a': {'b': 2}}
test['b']['a'] += 1
test
{'a': {'b': 2}, 'b': {'a': 1}}

print(test)