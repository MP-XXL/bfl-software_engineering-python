#Let's Cook Rice! This script acts like micro_wave
import time
print("---------------")
user_name = input("Enter your name")
print("Open the micro-wave")
print("Put the rice")
print("Set your cooking time")
duration = int(input("Enter time: \n")) #You can use float in place of int to have your input be a floating point number
print("Your rice will be ready in {} mins, {}".format(duration, user_name))
time.sleep(duration * 60)
print("Your food is ready!")


