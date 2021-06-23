"""
Parens: Implement an algorithm to print all valid (e.g., properly opened and closed)
combinations of n pairs of parentheses.
EXAMPLE
Input: 3
Output: ((())), (()()), (())(), ()(()), ()()()
"""


def validParenthesesHelper(parentheses: str) -> []:
    openParentheses = "("
    parenthesesLookup = {"(": ")", ")": "("}
    if len(parentheses) == 1:
        return [parentheses]
    else:
        first = parentheses[:1]
        stack = validParenthesesHelper(parentheses[1:])
        if stack:
            top = stack.pop()
            if first is openParentheses and parenthesesLookup[first] == top:
                return stack
            else:
                stack.append(top)
                stack.append(first)
                return stack


def validParentheses(parentheses: str) -> bool:
    return False if validParenthesesHelper(parentheses) else True


if __name__ == '__main__':
    testParentheses = "(()))"
    print(validParentheses(testParentheses))
