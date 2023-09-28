def add (first, second):
    return first+second


def minus (first, second):
    return first-second



def mult (first, second):
    return first*second



def div (first, second):
    if second == 0:
        raise ValueError("Cannot divided by Zero")
    return first/second


def tree(node):
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        operator, left_operand, right_operand = node
        if operator == '+':
            return add (tree(left_operand), tree(right_operand))
        elif operator == '-':
            return minus (tree(left_operand), tree(right_operand))
        elif operator == '*':
            return mult (tree(left_operand), tree(right_operand))
        elif operator == '/':
            return div (tree(left_operand), tree(right_operand))
    else:
        raise ValueError("Invalid expression tree node")

expression_tree = ('*', ('+', 2, 3), ('-', 5, 1))

result = tree(expression_tree)

print("Hasil Evaluasi Pohon Ekspresi:", result)

