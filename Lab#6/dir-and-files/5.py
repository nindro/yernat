#5. Write a Python program to write a list to a file.
lst = ["apple", "banana", "cherry"]
f = open("demo.txt", "x")
for i in lst:
    f.write(i + "\n")
f.close()
#RESULTS:
#Creates a demo.txt file containing:
#apple
#banana
#cherry