# python3
import re
def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
#     command=input()
#     if 'I' in command:
        p=input()
        line=input()

#     if 'F' in command:
#         file=input()
#         name="tests/"+file
#         with open(name,"r") as file:
#                 p=name.readline().rstrip()
#                 line=name.readline().rstrip()
    
    return (p, line)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(p,line):
    # this function should find the occurances using Rabin Karp alghoritm 
    # and return an iterable variable
    occurrences = []
    pattern_len = len(p)
    text_len = len(line)
    pattern_hash = hash(p)
    
    for i in range(text_len - pattern_len + 1):
        
        if hash(line[i:i+pattern_len]) == pattern_hash:
           
            if line[i:i+pattern_len] == p:
                occurrences.append(i)
    
    return occurrences

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

