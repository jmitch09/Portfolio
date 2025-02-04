import math

def main():
        pHW()
        print(1/2)
        print(math.floor(1/2))
        x = [1, 2]
        y = [3, 4]
        z = x + y
        print(z)
        #i = 0
        # while i < 5:
        #         if i == 5:
        #                 break
        #         print(i)
        #         i += 1
        # else:
        #         print(i) 
        nl = ["hi", "how", "are", "you"]
        ''.join(nl)
        if 345 in {'key':345}.values():
                print('yes')
                mylist = [x*y for x, y in [(2,1),(4,2),(6,3)]]
                print(mylist)
        
        x= 1
        print("x is {}".format(x))
        


def pHW():
        print("Hello World")       

if __name__ == "__main__":
        main()