import math
import string

def vol(rad):
        return 4 / 3 * math.pi * pow(rad, 3)

def ran_check(num, low, high):
        if num > low and num < high:
                return True
        else:
                return False
        
def up_low(s):
        upper = 0
        lower = 0
        for char in s:
                if char.isupper():
                        upper += 1
                elif char.islower():
                        lower += 1
        
        print("Original String: " + s)
        print(f"No. of Upper case characters: {upper}")
        print("No. of Lower case characters: {}".format(lower))

def unique_list(lst):
        nl = set([])
        for num in lst:
                if num not in nl:
                        nl.add(num)
        return list(nl)

def multiply(numbers):
        ans = 1
        for num in numbers:
                if len(numbers) == 0:
                        return 0
                else:
                        ans = ans * num

        return ans

def palindrome(s):
        s = s.replace(' ','')
        ns = s[::-1]
        if ns == s:
                return True
        else:
                return False
        
def ispangram(str1, alphabet=string.ascii_lowercase):
        aset = set(alphabet)
        str1 = str1.replace(' ','')
        str1 = set(str1.lower())
        if str1 == aset:
                return True
        else:
                return False
        

        
def main():
        print(vol(2))
        print(ran_check(5,2,7))
        print(ran_check(1,2,7))
        up_low("Hello Mr. Rogers, how are you this fine Tuesday?")
        print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))
        print(multiply([1,2,3,-4]))
        print(palindrome('helleh'))
        print(palindrome('heller'))
        print(palindrome('hell eh'))
        print(ispangram("The quick brown fox jumps over the lazy dog"))
        print(ispangram("The, quick brown fox jumps over the lazy dog"))

if __name__ == "__main__":
        main()