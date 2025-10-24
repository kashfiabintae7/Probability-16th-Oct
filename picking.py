import random

red = int(input("Enter number of Red balls: "))
blue = int(input("Enter number of Blue balls: "))
green = int(input("Enter number of Green balls: "))

balls = ["Red"] * red + ["Blue"] * blue + ["Green"] * green
print("\nBalls in the box:", balls)

picked_ball = random.choice(balls)
print("\nPicked ball:", picked_ball)

total_balls = len(balls)
picked_count = balls.count(picked_ball)
print("Probability of picking a", picked_ball, "ball =", (picked_count/total_balls))
