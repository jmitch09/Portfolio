def num_vowels(text):
        num = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        for char in text.lower():
                if char in vowels:
                        num += 1

        return num       

def factorial(fact):
        if fact < 0:
                pass # rasie error
        if fact == 1 or fact == 0:
                return 1

        return fact * factorial(fact - 1)

def BS(arr, num, left=0, right=None):
        if right == None:
                right = len(arr) - 1
        if left > right:
                return -1
        
        k = (left + right) // 2

        if arr[k] == num:
                return k
        elif arr[k] < num:
                return BS(arr, num, k + 1 , right)
        elif arr[k] > num:
                return BS(arr, num, left, k - 1)
        
        # More effiecient to be all done in a loop

def min_cost(cost):
        dp = [0] * (len(cost) + 1)
        for i in range(2, len(dp)):
                dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[-1]



def main():
        pass

if __name__ == "__main__":
        main()