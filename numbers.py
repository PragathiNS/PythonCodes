# median
def median(lst):
    sorted_list = sorted(lst)
    if len(sorted_list) % 2 != 0:
        #odd number of elements
        index = len(sorted_list)//2 
        return sorted_list[index]
    elif len(sorted_list) % 2 == 0:
        #even no. of elements
        index_1 = len(sorted_list)/2 - 1
        index_2 = len(sorted_list)/2
        mean = (sorted_list[index_1] + sorted_list[index_2])/2.0
        return mean
   
print median([2, 4, 5, 9])


# Factorial
def factorial(x):
    total = 1
    while x>0:
        total *= x
        x-=1
    return total
    
 factorial(9)
 
# is_prime
def is_prime(x):
  if x < 2:
      return False
  else:
      for n in range(2, x-1):
          if x % n == 0:
              return False
      return True

        
# is_int
def is_int(x):
    absoluteCount = abs(x)
    typeCount =type(x)
    roundCount = round(absoluteCount)
    if typeCount and absoluteCount - roundCount == 0:
        return True
    else:
        return False
 
# Statistics
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print grade

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  print total
  return total
    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  print average
  return average

def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for score in scores:
    variance += (average - score) ** 2
  variance = variance / len(scores)
  print variance
  return variance

def grades_std_deviation(variance):
  return variance ** 0.5

variance = grades_variance(grades)
print print_grades(grades)
print grades_std_deviation(variance)
