from stacks import Stack

OPERATORS = set(["+", "-", "*", "/", "^"])
PRIORITY = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
NUMBERS = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

def in2post(expr):
    new_stack = Stack()
    output = ""
    for char in expr:
        if char in NUMBERS:
            output += char
        elif char == "(":
            new_stack.push(char)
        elif char == ")":
            while new_stack.size() > 0 and new_stack.top() != "(": #checks for unpaired parenthesis
                output += new_stack.pop() #adds everything from the stack to the output
            new_stack.pop() #gets rid of the parenthesis because we don't need it
        else:
            while new_stack.size() > 0 and new_stack.top() != '('\
                and PRIORITY[char] <= PRIORITY[new_stack.top()]:
                output += new_stack.pop()
            new_stack.push(char)
        return output




with open('data.txt', 'r') as fin:
    lines = fin.readlines()
    for line in lines:
        print(f"Infix: {line}")
        print(f"Postfix: {in2post(line)}")


