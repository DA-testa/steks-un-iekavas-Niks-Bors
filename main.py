# python3
# 
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

        if i == len(text)-1 and len(opening_brackets_stack)==0:
            return "Success"
    return 1


    
            
    
            


def main():
    type = input()
    if type =='F':
        fileName = input()
        file = open(fileName, "r")
        print(find_mismatch(file))
    if type =='I':
        text = input()
        print(find_mismatch(text))
        
    # Printing answer, write your code here


if __name__ == "__main__":
     main()
