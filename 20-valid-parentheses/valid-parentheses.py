class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Dictionary to map closing brackets to their corresponding opening brackets
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:
                # Pop the top of the stack if it's not empty, otherwise use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the mapping doesn't match, it's invalid
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all brackets matched; otherwise, it's invalid
        return not stack
