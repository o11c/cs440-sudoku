import node

def search3x3(self, rootNode):
    stack = []
    stack.append(rootNode)

    while stack != []:
        node = stack.pop()
        if node.depth == node.state.nn:
            return node
        move = action(node)
        if move != []:
            for n in move:
                stack.append(n)
    return None

def action(node):
    return []
