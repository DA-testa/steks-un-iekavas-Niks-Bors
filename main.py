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
            
        print(opening_brackets_stack)   
        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
             return i+1

            opening_brackets_stack.pop()
            if opening_brackets_stack:
                return opening_brackets_stack[0].position
                
            return "Success"
            
            
            # Process closing bracket, write your code here
            


    def main():
        text = input()
        mismatch = find_mismatch(text)
        if len(opening_brackets_stack)==0:
                print("Success")

        else:
         print(opening_brackets_stack[-1].postion)
        return 0
    # Printing answer, write your code here


    if __name__ == "__main__":
     main()
