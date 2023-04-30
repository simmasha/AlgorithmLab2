class Tree:
    def __init__(self, Array: list, count):
        self.Array = Array
        if count % 2 == 0:
            self.size = len(Array) * 2
        else:
            if count == 1:
                self.size = 1
            else:
                self.size = len(Array) * 2 + 1
        self.build(0, len(Array))
        self.head = Array[-1]

    def build(self, start, end):
        if len(self.Array) < self.size:
            for i in range(start, end, 2):
                if self.Array[i].left is None and self.Array[i].right is None:
                    if i < end - 1:
                        node = Node(i, i + 1, 0, self.Array[i], self.Array[i + 1])
                    else:
                        node = Node(i, i, 0, self.Array[i], None)
                else:
                    if i < end - 1:
                        if self.Array[i + 1].right is not None:
                            node = Node(self.Array[i].left.leftcoverage, self.Array[i + 1].right.rightcoverage, 0,
                                        self.Array[i], self.Array[i + 1])
                        else:
                            node = Node(self.Array[i].left.leftcoverage, self.Array[i + 1].left.rightcoverage, 0,
                                        self.Array[i], self.Array[i + 1])
                    else:
                        node = Node(self.Array[i].left.leftcoverage, self.Array[i].left.leftcoverage, 0,
                                    self.Array[i], None)
                self.Array.append(node)
            self.build(end, len(self.Array))
        return


class Node:
    def __init__(self, lcoverage, rcoverage, modificator, left=None, right=None):
        self.leftcoverage = lcoverage
        self.rightcoverage = rcoverage
        self.modificator = modificator
        self.left = left
        self.right = right


def Operation(node, operator: int, left: int, right: int):
    if node.leftcoverage >= left and node.rightcoverage <= right:  # полное покрытие
        newNode = Node(node.leftcoverage, node.rightcoverage, node.modificator, node.left, node.right)
        newNode.modificator += operator
        # return node
    elif node.rightcoverage < left or node.leftcoverage > right:  # нет покрытия
        return node
    else:  # частичное покрытие
        newNode = Node(node.leftcoverage, node.rightcoverage, node.modificator, node.left, node.right)
        newNode.left = Operation(newNode.left, operator, left, right)
        newNode.right = Operation(newNode.right, operator, left, right)
    return newNode


def Result(node, leaf, res=0):
    res += node.modificator
    if leaf == node.leftcoverage == node.rightcoverage:
        return res
    if node.left is not None:
        if node.left.leftcoverage <= leaf <= node.left.rightcoverage:
            res = Result(node.left, leaf, res)
    if node.right is not None:
        if node.right.leftcoverage <= leaf <= node.right.rightcoverage:
            res = Result(node.right, leaf, res)
    return res


# def printTree(node):
#     print(node.modificator)
#     if node.left is not None: printTree(node.left)
#     if node.right is not None: printTree(node.right)

def solution(Rectangles, Points):
    operations = []
    for rectangle in Rectangles:
        operations.append([rectangle.x1, rectangle.y1, rectangle.x2, rectangle.y2, 1])
        operations.append([rectangle.x2, rectangle.y2, rectangle.x1, rectangle.y1, -1])
    operations.sort(key=lambda x: x[0])
    # print(recPoints)

    # operations = []
    # for x in recPoints:
    #     if x[4] == 'start':
    #         arr = [x[1], x[3] - 1, 1]
    #     else:
    #         arr = [x[3], x[1] - 1, -1]
    #     operations.append(arr)

    trees = []
    t = []
    for i in range(len(Rectangles) * 2 - 1):
        node = Node(i, i, 0)
        t.append(node)
    tree = Tree(t, len(Rectangles))

    X = {}
    for op in operations:
        if op[4] == 1:
            tree.head = Operation(tree.head, op[4], op[1], op[3]-1)
        else:
            tree.head = Operation(tree.head, op[4], op[3], op[1]-1)
        X[op[0]] = tree.head
        trees.append(tree.head)
        # printTree(tree.head)
        # print("\n")

    for point in Points:
        if point.y >= len(operations)-1: print('0', end = " ")
        elif point.x == -1 or point.y == -1: print('0', end = " ")
        else: print(Result(X[point.x], point.y), end=" ")
