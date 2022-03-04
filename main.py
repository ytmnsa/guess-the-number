import random
x = random.randint(1,10)
ans = int(input("Guess the number from 1 to 10 :"))
test = "hi"
print("_____________")
if x == ans:
  print("""Correct!
Me: """+str(x)
+"""
You: """+str(ans))
elif x != ans:
  print("""Wrong!
Me: """+str(x)
+"""
You: """+str(ans))
