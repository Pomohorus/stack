from ex1 import Stack

def balance(example):
    left = 0
    right = 0
    index_1 = 0
    if Stack(example).isempty() is True:
        if Stack(example).size() % 2 == 0:
            for item in example:
                if item == '(':
                    left += 1
                elif item == '[':
                    left += 1
                elif item == '{':
                    left += 1
                else:
                    right += 1
            if right == left:
                while index_1 < len(example):
                    if example[index_1] == '(' and example[index_1 + 1] == ')' :
                        example.pop(index_1)
                        example.pop(index_1)
                        index_1 = 0
                    elif example[index_1] == '[' and example[index_1 + 1] == ']':
                        example.pop(index_1)
                        example.pop(index_1)
                        index_1 = 0
                    elif example[index_1] == '{' and example[index_1 + 1] == '}':
                        example.pop(index_1)
                        example.pop(index_1)
                        index_1 = 0
                    else:
                        index_1 += 1
                if len(example) == 0:
                    return 'Сбалансированно'
                else:
                    return 'Несбалансированно'
            else:
                return 'Несбалансированно'
        else:
            return 'Несбалансированно'
    else:
        return 'Входной список пуст'

example = '(((([{}]))))'
example = list(example)
total = balance(example)
print(total)