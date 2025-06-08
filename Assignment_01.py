'''Task
Question - 1
The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.'''

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    addition = a+b
    subtract = a-b
    product = a*b
    print(addition)
    print(subtract)
    print(product)





'''Question - 2
Given an integer,n, print the following values for each integer i from 1 to n :

Decimal
Octal
Hexadecimal (capitalized)
Binary
Function Description

Complete the print_formatted function in the editor below.

print_formatted has the following parameters:

int number: the maximum value to print
Prints

The four values must be printed on a single line in the order specified above for each i from 1 to number. Each value should be space-padded to match the width of the binary value of number and the values should be separated by a single space.
'''

def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]
        
        print(decimal.rjust(width), octal.rjust(width), hexadecimal.rjust(width), binary.rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)





'''Question - 3
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.'''
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()  
    average = sum(student_marks[query_name]) / len(student_marks[query_name])
    print("{0:.2f}".format(average))





'''Question - 4
Task
Given an integer,n, and n  space-separated integers as input, create a tuple,t, of those n integers. Then compute and print the result of hash(t) .

Note: hash() is one of the functons in the __builtins__ module, so it need not be imported.'''
if __name__ == '__main__':
  n = int(raw_input())
  integer_list = map(int, raw_input().split())
  t=tuple(integer_list)
  print(hash(t))
  



'''Question - 5
The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python.

To read more about the functions in this module, check out their documentation here.

You are given a list of N lowercase English letters. For a given integer K, you can select any K indices (assume 1-based indexing) with a uniform probability from the list.

Find the probability that at least one of the K indices selected will contain the letter: 'a'.
'''
import itertools

def probability_contains_a(N, letters, k):
    count_a = letters.count('a')
    total_combinations = len(list(itertools.combinations(letters, k)))
    if count_a == 0:
        return 0.0
    
    non_a_letters = [c for c in letters if c != 'a']
    non_a_combinations = len(list(itertools.combinations(non_a_letters, k)))
    if non_a_combinations == 0:
        return 1.0
    prob_no_a = non_a_combinations / total_combinations
    prob_at_least_one_a = 1 - prob_no_a
    return prob_at_least_one_a

N = int(input())
letters = input().split()
k = int(input())

result = probability_contains_a(N, letters, k)
print("{0:.3f}".format(result))





'''Question - 6
Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.'''
def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    return leap

year = int(input())
print(is_leap(year))






'''Question - 7
The Minion Game'''
def minion_game(string):
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    n = len(string)
    
    for i in range(n):
        if string[i] in vowels:
            kevin_score += (n - i)
        else:
            stuart_score += (n - i)
    
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)






'''Question - 8
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .

You are given a string S . Suppose a character 'c' occurs consecutively X times in the string. Replace these consecutive occurrences of the character 'c' with (X,c) in the string.

For a better understanding of the problem, check the explanation.'''
from itertools import groupby

def compress_string(s):
    groups = groupby(s)
    result = [(len(list(group)), int(char)) for char, group in groups]
    return result

if __name__ == '__main__':
    s = input().strip()
    compressed = compress_string(s)
    print(' '.join(f'({count}, {char})' for count, char in compressed))