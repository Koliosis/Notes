#code for a stack ADT
class Stack():
    def __init__(self):
        self.lyst = []


    def __str__(self):
        return str(self.lyst)


    def push(self, num):
        self.lyst.append(num)

    
    def pop(self):
        if len(self.lyst) == 0:
            raise SyntaxError
        value = self.lyst[-1]
        del self.lyst[-1]
        return value


    def top(self):
        return self.lyst[-1]


    def size(self):
        return len(self.lyst)
    
    
    def empty(self):
        if len(self.lyst) == 0:
            return True


    def clear(self):
        self.lyst = []


#create function that take the infix expression and change it to postfix
def in2post(expression):
    stack_list = Stack()
    OPERATORS = set(['+', '-', '*', '/', '(', ')', '^'])
    PRIORITY = {'+':1, '-':1, '*':2, '/':2, '^':3}
    NUMBERS = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    """
    :param expression:
    :return:
    """
    if type(expression) is not str:
        raise ValueError
    expression = expression.replace(" ", "")
    output = ''
    for char in expression:
        if char not in OPERATORS:
            output += char
        elif char == '(':
            stack_list.push('(')
        elif char == ')':
            while stack_list.size() > 0 and stack_list.top() != '(':
                output += stack_list.pop()
            stack_list.pop()
        else:
            while stack_list.size() > 0 and stack_list.top() != '('\
                    and PRIORITY[char] <= PRIORITY[stack_list.top()]:
                output += stack_list.pop()
            stack_list.push(char)
    while stack_list.size() > 0:
        output += stack_list.pop()
    return output