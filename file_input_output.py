my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "w")

for i in my_list:
  my_file.write(str(i) + "\n")
  
my_file.close()

my_file = open("output.txt", "r")

print my_file.read()
"""1
4
9
16
25
36
49
64
81
100"""

my_file.close()

my_file = open("text.txt", "r")

print my_file.readline()
# I'm the first line of the file!

print my_file.readline()
# I'm the second line.

print my_file.readline()
# Third line here, boss.

my_file.close()

# __enter__() and __exit__(). The details aren't important, but what is important is that when a file object's __exit__() method is invoked, it automatically closes the file. 
# How do we invoke this method? With with and as.

with open("text.txt", "w") as my_file:
  my_file.write("Hello")
  
if not my_file.closed:
  my_file.close()
print my_file.closed
