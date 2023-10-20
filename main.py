import random, os, time
while True:
  value = random.randint(1, 9)
  track = 0
  while True:
    num = int(input("Guess the Number from 1 to 9!"))
    if num > value:
      print("Too high")
      track += 1
      if track >= 5:
        time.sleep(0.5)
        os.system('clear')
        time.sleep(0.2)
        while True:
          print('YOU FAILED!')
          time.sleep(1)
      continue
    elif num < value:
      print("Too low")
      track += 1
      if track >= 5:
        time.sleep(1.2)
        while True:
          print('YOU FAILED!')
          time.sleep(0.1)
          os.system('clear')
          time.sleep(0.05)
      continue
    else:
      print("You got it!")
      print(f"You took {track} tries to find the number!")
      break