class Stack_palindrome:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def top(self):
        return self.data[len(self.data) - 1]

    def pop(self):
        return self.data.pop()
    
    def print_stack(self):
        print (self.data)

    def __str__(self):
        return str(self.data)

def isPalindrome(s):
    obj = Stack_palindrome()
    
    for i in s:
        obj.push(i)

    obj.print_stack()

    for i in s:
        print (i)
        if obj.pop() == s:
            palindrome = True
        else:
            palindrome = False

    return palindrome

print (isPalindrome("madam"))
