'''Question - 1
Task to make the first letter of every words as capital'''
def solve(s):
    return ' '.join(word.capitalize() for word in s.split(' '))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()


'''Question - 2
Calculate the averages of items present inside a python set '''
def average(array):
    my_set = set(array)
    avg = sum(my_set)/len(my_set)
    return (avg)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


'''Question - 3
Task to wrap the string into a paragraph of given width .'''
import textwrap
def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


'''Question - 4
pattern printing with the help of alphabets'''
def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    lines = []
    for i in range(size):
        s = '-'.join(alpha[size-1:i:-1] + alpha[i:size])
        lines.append((s).center(4*size - 3, '-'))
    print('\n'.join(lines[:0:-1] + lines))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


'''Question - 5
Split a string into equal parts of length and Convert each parts by removing any subsequent occurrences of non-distinct'''
def merge_the_tools(string, k):
    n = len(string)
    for i in range(0, n, k):
        segment = string[i:i+k]
        seen = set()
        result = []
        for char in segment:
            if char not in seen:
                seen.add(char)
                result.append(char)
        print(''.join(result))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


'''Question - 6
calculate the total earned amount'''
from collections import defaultdict
def compute_earnings():
    num_shoes = int(input())
    shoe_sizes = list(map(int, input().split()))
    num_customers = int(input())
    inventory = defaultdict(int)
    for size in shoe_sizes:
        inventory[size] += 1
    total_earnings = 0
    for _ in range(num_customers):
        size, price = map(int, input().split())
        if inventory.get(size, 0) > 0:
            total_earnings += price
            inventory[size] -= 1
    print(total_earnings)

if __name__ == "__main__":
    compute_earnings()


'''Question - 7
implementing exception handling'''
for i in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(int(a//b))
    except Exception as e:
        print("Error Code:",e)


'''Question - 8
regex based problem statement'''
import re
def is_valid_regex(s):
    try:
        re.compile(s)
        return True
    except re.error:
        return False

if __name__ == "__main__":
    import sys
    input_lines = sys.stdin.read().splitlines()
    T = int(input_lines[0])
    for i in range(1, T + 1):
        s = input_lines[i].strip()
        print(is_valid_regex(s))


'''Question - 9
py-set-discard-remove-pop : task based on discard(),remove() & pop()'''
n = int(input())
s = set(map(int, input().split()))
num_commands = int(input())

for _ in range(num_commands):
    command = input().split()
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        s.remove(int(command[1]))
    elif command[0] == 'discard':
        s.discard(int(command[1]))

print(sum(s))
