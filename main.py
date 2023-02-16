# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next,i+1))
            
           
            # Process opening bracket, write your code here
            
          
        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
             return i+1
            opening_brackets_stack.pop()
            if not opening_brackets_stack:
                return "Success"
    return 1
            
    
            


def main():
    text = inputs()
    if "I" in text:
        text = inputs()
    inputs =["[]","{}[]","[{}]","{","{[}","foo(bar[i);",]
    for input in inputs:
         mismatch = find_mismatch(input)
         print("%-11s %s" %(input,mismatch))
        
    # Printing answer, write your code here


if __name__ == "__main__":
     main()
