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
            # pievieno stekam atverošo iekavu, un pozīciju
            
           
            # Process opening bracket, write your code here
            
          
        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i+1
                # pārbauda vai stekā ir atbilstoša aizverošā iekava atverošai iekavai, un vai tas ir tukšs

            opening_brackets_stack.pop() # ja sakrīt iekavas, tad tiek izņemts no steka
        if i == len(text)-1 and len(opening_brackets_stack)==0:
            # ja teksta rindā visas iekavas sakrīt, tad izprintē success

            return "Success"
     
        
    

def main():

    text = input()
    if "I" in text:
        text = input()
        ms = find_mismatch(text)
        print(ms)
        
    # Printing answer, write your code here


if __name__ == "__main__":
     main()

     


