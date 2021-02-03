import random

def guess(x):
        random_no = random.randint(1, x)
        times =0
        guess = 0
        while guess != random_no:
            guess = int(input(f"please input a no{x}:"))
            if guess>random_no:
                print("sorry no too high")
            elif guess<random_no:
                print("sorrry no too low" )
            times+=1
        print(f"hurray you made it to {random_no}!!in {times} times")

guess(10)



