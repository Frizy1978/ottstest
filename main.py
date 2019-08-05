from graph import Node, Tree, sanitize_id
import uuid

class CharVh(Node):
    def __init__(self, name, value, key = None, dictvh = None):
        super(CharVh, self).__init__(name, identifier=None, expanded=True)
        self.name = name
        self.value = value
        self.key = key
        self.dic = dictvh
    def displaychar(self):
        print("%s: %s -> *уточнение: %s" % (self.name, self.value, self.dic[self.key]))

class AttrVh(Tree):
    def __init__(self, name, identifier=None, id_parent=None):
        super(AttrVh, self).__init__()
        self.name = name
        self.id = (str(uuid.uuid1()) if identifier is None else sanitize_id(str(identifier)))
        self.id_parent = id_parent

if __name__ == "__main__":
    notevh = {"КЛЮЧ 1":"Уточнение 1", "КЛЮЧ 2":"Уточнение 2", "КЛЮЧ 3":"Уточнение 3"}
    print(notevh)
    print("="*40)
    charvh = CharVh("Тип топлива"," бензин", "КЛЮЧ 2", notevh)
    charvh.displaychar()
    notevh.update({"КЛЮЧ 2":"Уточнение 2+++++++++++++++++++"})
    print(type(charvh.dic))
    print("="*40)
    print(notevh)
    charvh.displaychar()
    print(">"*80)
    atr = AttrVh("Количество мест для сидения")
    atr.create_node("первый ряд", "1 row")



