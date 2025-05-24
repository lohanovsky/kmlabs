class BinaryTree:
    def min(self):
        return self.root.min()
    
    def max(self):
        return self.root.max()
    
    def lcr(self):
        return self.root.lcr()
    
    def __len__(self):
        return len(self.root)
    
    def __contains__(self,value):
        return value in self.root
    
    def __init__(self):
        """Метод __Init__ используется при инициализации (то есть создании) элемента класса BinaryTree. Создаётся корень класса EmptyNode"""
        BinaryNode.numberOfNodes = 0
        self.root = EmptyNode()

    def __repr__(self):
        """Метод __repr__ описывает строковое представление объекта. Он возвращает представление корня, который может быть класса BinaryNode или ЕmptyNode"""
        return repr(self.root)

    def insert(self,value):
        """Метод insert дерева присваивает корень новому элементу BinaryTree""" 
        self.root = self.root.insert(value)

class BinaryNode:
    numberOfNodes = 0
    def __len__(self):
        return self.numberOfNodes
    
    def min(self):
        if isinstance(self.left,EmptyNode):
            return self.value
        else:
            return self.left.min()
    
    def max(self):
        if isinstance(self.right,EmptyNode):
            return self.value
        else:
            return self.right.max()
    
    def lcr(self):
        result = self.left.lcr() + [self.value] + self.right.lcr()
        return result

    def __contains__(self,value):
        if value == self.value:
            return True
        elif value < self.value:
            return value in self.left
        else:
            return value in self.right
    
    def __init__(self,left,value,right):
        """Метод __init__ инициализирует узел дерева"""
        BinaryNode.numberOfNodes += 1
        self.left = left
        self.value = value
        self.right = right
    
    def __repr__(self):
        """Метод __repr__ возвращает строковое представление узла"""
        return f'({self.left},{self.value},{self.right})'
    
    def insert(self,value):
       """Метод insert узла дерева добавляет новый узел по правилу, что если новое значение меньше чем текущее,
       то новый узел записывается слева от текущего, и наоборот если равно либо больше. Таким образом, все элементы дерева
       меньше изначального (корневого) находятся от него слева, и наоборот для больших"""
       if value < self.value:
           self.left = self.left.insert(value)
       else:
           self.right = self.right.insert(value)
       return self
    
class EmptyNode:
    def min(self):
        return None
    
    def max(self):
        return None
    
    def lcr(self):
        return []
    def __len__(self):
        return 0
    
    def __contains__(self,_):
        return False
    
    def __repr__(self):
        """Метод __repr__ для пустого узла возвращает '*'"""
        return '*'
        
    def insert(self,value):
        """Метод insert для пустого узла возвращает новый узел BinaryNode"""
        return BinaryNode(self,value,self)