"""
WARMUP
"""
# Lesser of Two Evens
def lesser_of_two_evens(a, b):
        if a % 2 == 0 and b % 2 == 0:
                return min(a, b)
        else:
                return max(a, b)
        
# Animal Crackers
def animal_crackers(text):
        arr = text.split()
        if arr[0][0] == arr[1][0]:
                return True
        else:
                return False

# Makes Twenty
def makes_twenty(a, b):
        if a == 20 or b == 20 or sum((a, b)) == 20:
                return True
        else:
                return False
        
"""
LEVEL 1
"""
# Old Macdonald
def old_macdonald(name):
        s = ''
        for i in range(len(name)):
                if i == 0 or i == 3:
                        s = s + name[i].upper()
                else:
                        s = s + name[i]
        
        return s

# Master Yoda
def master_yoda(text):
        arr = text.split()
        arr.reverse()
        ans = ' '.join(arr)

        return ans

# Almost There
def almost_there(n):
        if n >= 90 and n <= 110:
                return True
        elif n >= 190 and n <= 210:
                return True
        else:
                return False

"""
LEVEL 2
"""
# Find 33
def has_33(nums):
        three = False
        for num in nums:
                if num == 3:
                        if three == True:
                                return True
                        else:
                                three = True
                else:
                        three = False

        return False

# Paper Doll
def paper_doll(text):
        s = ''
        for char in text:
                s = s + char * 3

        return s

# BlackJack
def blackjack(a, b, c):
        x = a + b + c
        ans = None
        if x <= 21:
                ans = x
        else:
                if a == 11 or b == 11 or c == 11:
                        x = x - 10
                        if x <= 21:
                                ans = x
                        else:
                            ans = 'BUST'
                else:
                        ans = 'BUST'

        return ans

# Summer 69
def summer_69(arr):
        six = False
        s = 0
        for num in arr:
                if num == 6:
                        six = True
                elif six:
                        if num == 9:
                                six = False
                else:
                        s = s + num

        return s

"""
CHALLENGE
"""
# Spy Game
def spy_game(nums):
        oh = False
        OH = False
        for num in nums:
                if num == 7:
                        if oh and OH:
                                return True
                elif num == 0:
                        if oh:
                                OH = True
                        else:
                                oh = True
        
        return False

# Count Primes
def count_primes(num):
        ans = 0
        for i in range(2, num+1):
                if is_prime(i):
                        ans += 1
        
        return ans

def is_prime(num):
        for i in range(2, num):
                if num % i == 0:
                        if num == 2:
                                return True
                        else:
                                return False
                
        return True




"""
TESTS
"""
def main():
        # Warmup
        print("\n\nwarmup")
        print(lesser_of_two_evens(2, 4))
        print(lesser_of_two_evens(2, 5))
        print(animal_crackers('Level Llama'))
        print(animal_crackers('Crazy Kangaroo'))
        print(makes_twenty(20, 10))
        print(makes_twenty(12, 8))
        print(makes_twenty(2, 3))
        
        # Level 1
        print("\n\nLevel 1")
        print(old_macdonald('macdonald'))
        print(master_yoda('I am home'))
        print(master_yoda('We are ready'))
        print(almost_there(104))
        print(almost_there(150))
        print(almost_there(209))

        # Level 2
        print("\n\nLevel 2")
        print(has_33([1, 3, 3]))
        print(has_33([1, 3, 1, 3]))
        print(has_33([3, 1, 3]))
        print(paper_doll("hello"))
        print(paper_doll("mississippi"))
        print(blackjack(5,6,7))
        print(blackjack(9,9,9))
        print(blackjack(9,9,11))
        print(summer_69([1, 3, 5]))
        print(summer_69([4, 5, 6, 7, 8, 9]))
        print(summer_69([2, 1, 6, 9, 11]))

        # Challenge
        print("\n\nChallenge")
        print(spy_game([1, 2, 4, 0, 0, 7, 5]))
        print(spy_game([1, 0, 2, 4, 0, 5, 7]))
        print(spy_game([1, 7, 2, 0, 4, 5, 0]))
        print(count_primes(100))

if __name__ == "__main__":
        main()