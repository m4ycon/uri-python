# John wants to set up a panel 
# containing different numbers of LEDs. He does not have many leds, 
# he is not sure if he will be able to mount the desired number. 
# Considering the configuration of the LEDs of the numbers below, 
# make an algorithm that helps John to discover 
# the number of LEDs needed to set the value.

# Input
# The input contains an integer N, (1 ≤ N ≤ 2000) 
# corresponding to the number of test cases, followed by N lines, 
# each line containing a number (1 ≤ V ≤ 10100) 
# corresponding to the value that John wants to set with the leds.

# Output
# For each test case, print one line containing the number of LEDs 
# that John needs to set the desired value, followed by the word "leds".

# 3
# 115380
# --> 27 leds
# 2819311
# --> 29 leds
# 23456
# --> 25 leds

numOfLines = int(input())

for x in range(numOfLines):
    nums = str(input())
    leds = 0
    for num in nums:
        num = int(num)
        if (num == 1):
            leds += 2
        elif (num == 7):
            leds += 3
        elif (num == 4):
            leds += 4
        elif (num == 2 or num == 3 or num == 5):
            leds += 5
        elif (num == 6 or num == 9 or num == 0):
            leds += 6
        elif (num == 8):
            leds += 7
    print(str(leds) + ' leds')
