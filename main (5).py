#Leap year

"""
 year % 4==0&
 year% 100!  =0/
 year%400=0

 """
def isLeapyear(year):
  if(year% 4==0):
    return True
  else:
    return False

year=2017
if isLeapyear(year):
  print('{} is a lesp                     year.'.format) 
else:
  print(' {} is not a leap                  year.'.format (year))     