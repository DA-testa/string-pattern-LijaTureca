# python3


def read_input():
    # this function needs to acquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (for input from file)

    input_type = input().strip().upper()

    if input_type == 'I':
        p = input().strip()
        line = input().strip()

    elif input_type == 'F':
#         file = input()
        name="tests/06"
        with open(name,"r") as file:
            p = file.readline().strip()
            line = file.readline().strip()


    return p, line

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))
    
def get_hash(p: str) -> int:
    global B,Q 
    pattern_len = len(p)
    result=0
    for i in range(pattern_len):
        result=(B*result+ord(p[i])) % Q 
    return result

def get_occurrences(p,line):
    # this function should find the occurances using Rabin Karp alghoritm 
    # and return an iterable variable
    occurrences = []
    pattern_len = len(p)
    text_len = len(line)
    
    m=1
    for i in range(1,pattern_len):
        m=(m*B)%Q 
    pattern_hash=get_hash(p)
    line_hash=get_hash(line[:pattern_len])
    
    for i in range(text_len - pattern_len + 1):
        
        if line_hash == pattern_hash:
           
            if line[i:i+pattern_len] == p:
                occurrences.append(i)
        if i < text_len - pattern_len:
            line_hash = (B * (line_hash - m * ord(line[i])) + ord(line[i+pattern_len])) % Q
    
    
    
    return occurrences

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

