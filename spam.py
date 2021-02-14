import pyautogui
import time

msg = input("Enter the message: ")
n = input("How many times ?: ")

print("Start in ")

count = 5
while(count != 0):
	print(count)
	time.sleep(1)
	count -= 1

print("Let's Go!!")

for i in range(0, int(n)):
	pyautogui.typewrite(msg + "\n")
	time.sleep(0.5)
