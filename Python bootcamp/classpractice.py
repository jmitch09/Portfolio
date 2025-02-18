class Sample():

        param3 = 'hi'

        def __init__(self,param1,param2):
                self.param1 = param1
                self.param2 = param2

def main():
        my_sample = Sample('hello','world')
        print(my_sample.param1)
        print(my_sample.param2)
        print(my_sample.param3)

if __name__ == "__main__":
        main()