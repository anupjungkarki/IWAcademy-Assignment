# Write a Python class to find validity of a string of parentheses, '(', ')','{', '}', '[' and ']. These brackets must
# be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.
class validity:
    def is_valid_parenthesis(self, str):
        stack, char = [], {"(": ")", "{": "}", "[": "]"}
        for parenthesis in str:
            if parenthesis in char:
                stack.append(parenthesis)
            elif len(stack) == 0 or char[stack.pop()] != parenthesis:
                return False
        return len(stack) == 0


print(validity().is_valid_parenthesis("(){}[]"))
print(validity().is_valid_parenthesis("()[{)}"))
print(validity().is_valid_parenthesis("()"))
