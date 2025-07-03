#Let's Cook Rice! This script acts like micro_wave
import time
print("---------------")
print('''
        Welcome to Micro mate V.1.1, your personalised smart kitchen micro-wave

        INSTRUCTIONS
        1.Plug in Micro mate
        2.Enter username
        3.Put the food to be heated
        4.Set duration for heating
        ''')
allusers = {}
username = input("Enter your name to continue:\n >>> ")
allusers["name"] = username
print("Welcome, ", username, "!")
print("Open the micro-wave")
print("Put the rice")
print("Set your cooking time")
heating_duration = float(input("Enter time: \n")) #You can use int in place of float to have your input be integers only
allusers["duration"] = heating_duration
charge_for_heating = heating_duration * 1000
allusers["amount"] = charge_for_heating
print(allusers)
print("Your rice will be ready in {} min(s) {}".format(heating_duration, username))
print(f"You will be charged ₦{charge_for_heating} for heating")
time.sleep(heating_duration * 60)
print("Your food is ready!")

