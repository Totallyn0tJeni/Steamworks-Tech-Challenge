year = int(input("What is the year? "))
month = int(input("what is the month? "))
day = int(input("What day is it? "))
location = input("Where are you?! ")
month2 = 0
  
#Adding the year, month, day & location variables to our code and making sure the values are in the correct ranges

if month == 1:
  month2 = "January"
if month == 2:
  month2 = "Febuary"
if month == 3:
  month2 = "March"
if month == 4:
  month2 = "April"
if month == 5:
  month2 = "May"
if month == 6:
  month2 = "June"
if month == 7:
  month2 = "July"
if month == 8:
  month2 = "August"
if month == 9:
  month2 = "September"
if month == 10:
  month2 = "October"
if month == 11:
  month2 = "November"
if month == 12:
  month2 = "December"
#Chaging the numbers to the coressponding months


if month > 12 or day > 31:
  print("Invalid date")
else:
  print("You will arrive at" , location, "on", month2, day, year)

#If the values are in the correct range then it will print out the date and location where we will arive at. 

