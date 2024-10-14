"""Name: Dustin Barnes
Course: 2420-001
Project 4 Stacks
File: main.py
The following code was written by me. """

from stack import Stack

def balance(expr):
    """Used to make sure an expression is balanced in terms of
    parenthesis."""
    balance_stack = Stack()
    for char in expr:
        if balance_stack.is_empty():
            if char == "(":
                balance_stack.push(char)
            if char == ")":
                return False
        else:
            if char == "(":
                balance_stack.push(char)
            if char == ")":
                if balance_stack.pop() != "(":
                    return False
    return balance_stack.is_empty()

def in2post(expr): #pylint: disable=R0912
    """Takes an infix math equation and converts it to postfix."""
    if not balance(expr):
        raise SyntaxError("the provided expression is not balanced")
    in2post_stack = Stack()
    operator_list = ["/", "*", "+", "-"]
    parenthesis_list = ["(", ")"]
    operator_priority_dict = {"/":2, "*":2, "+":1, "-":1}
    operand_list = []
    post_expr = ""
    for number in range(10):
        operand_list.append(str(number))
    for char in expr:
        if char != " ":
            if char not in operator_list and char not in operand_list and char not in parenthesis_list: #pylint: disable=C0301
                raise ValueError("the expression has invalid characters")
            if char == "(":
                in2post_stack.push(char)
            elif char in operand_list:
                post_expr += (char + " ")
            elif char in operator_list:
                while not in2post_stack.is_empty() and in2post_stack.peek() != "(" and operator_priority_dict[in2post_stack.peek()] >= operator_priority_dict[char]: #pylint: disable=C0301
                    post_expr += (in2post_stack.pop() + " ")
                in2post_stack.push(char)
            else:
                post_expr += (in2post_stack.pop() + " ")
                while in2post_stack.peek() != "(" and not in2post_stack.is_empty():
                    post_expr += (in2post_stack.pop() + " ")
                in2post_stack.pop()
    for char in range(in2post_stack.size()):
        if in2post_stack.peek() == "(":
            in2post_stack.pop()
        else:
            post_expr += (in2post_stack.pop() + " ")
    return post_expr

def eval_postfix(expr):
    """Takes in a postfix equation and evaluates it. Then returns the result as a float."""
    eval_stack = Stack()
    operator_list = ["/", "*", "+", "-"]
    operand_list = []
    for number in range(10):
        operand_list.append(str(number))
    for char in expr:
        if char != " ":
            if char not in operator_list and char not in operand_list:
                raise ValueError("the expression contains invalid characters")
            if char in operand_list:
                eval_stack.push(char)
            else:
                if eval_stack.size() < 2:
                    raise SyntaxError("this is an invalid post-fix expression")
                second_number = float(eval_stack.pop())
                first_number = float(eval_stack.pop())
                if char == "+":
                    eval_number = first_number + second_number
                    eval_stack.push(eval_number)
                if char == "-":
                    eval_number = first_number - second_number
                    eval_stack.push(eval_number)
                if char == "/":
                    eval_number = first_number / second_number
                    eval_stack.push(eval_number)
                if char == "*":
                    eval_number = first_number * second_number
                    eval_stack.push(eval_number)
    return float(eval_stack.pop())

def main():
    """Main function, takes data input from a file, converts the
    infix equations to postfix, evaluates the postfix equations,
    and prints out the results."""
    raw_file = open("data.txt", "r")
    raw_file_data = raw_file.read()
    infix_list = raw_file_data.split('\n')
    if infix_list[-1] == '':
        infix_list.pop()
    for expr in infix_list:
        post = in2post(expr)
        print("infix: " + expr)
        print("postfix: " + post)
        print("answer: " + str(eval_postfix(post)))
        print("\n")

if __name__ == "__main__":
    main()
