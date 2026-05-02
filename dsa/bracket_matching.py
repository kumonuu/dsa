from stacks import Stack

open_brackets = ["(","{","[","<"]
closed_brackets = [")","}","]",">"]
stack = Stack()

def bracket_match(string):
    for character in string:
        if character in open_brackets:
            stack.push(character)
        if character in closed_brackets:
            closed_index = closed_brackets.index(character)
            if open_brackets[closed_index] == stack.top():
                stack.pop()
            else:
                return False
    if len(stack.my_list) > 0:
        return False
    return True

string = "()(}"
print(bracket_match(string))