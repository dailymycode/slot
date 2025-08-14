import random 
import time

fruits = ["🍎", "🍌", "🍒", "🍇"]

def spin_slot();

result = ["", "", ""]

for i in range(10):

    for j in range(3):
        result[j] = random.choice(fruits)
        print(" | ".join(result), end="\r")
        time.sleep(0.5)

        print(" | ".join(result))


        if result[0] == result[1] == result[2]:
            print("🎉 You wonn..")

        else:
            print("you lost, try ):")    

 spin_slot()


 