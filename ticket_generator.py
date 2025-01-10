#Name: Kaylie Yuen
#Date: 12/12/2024

#Initialize
import turtle
t = turtle.Turtle()

#Functions

#Draws an admission ticket with a label and customer information inside. This function uses a turtle to draw a ticket with the name of the customer and the price paid for the ticket.
#(string: name) represents the customers name that appears inside the ticket
#(integer: price) represents the price the customer paid that appears inside the ticket
#(string: dayofweek) represents the day of the week that the ticket was purchased
#(integer: y_location) y_location represents the vertical loction of the ticket
def draw_ticket(name, price, dayofweek, y_location):
    t.goto(-50, y_location)
    t.write("Ticket", font=("Arial", 15), align="right")
    t.pendown()
    for i in range(2):
        t.forward(500)
        t.left(90)
        t.forward(250)
        t.left(90)
    t.penup()
    t.goto(50, y_location +215)
    t.write("Admit One", font=("Arial", 15), align="right")
    t.goto(440, y_location +215)
    t.write(dayofweek, font=("Arial", 15), align="right")
    t.goto(225, y_location +135)
    t.write(name, font=("Arial", 15), align="right")
    t.goto(225, y_location +15)
    t.write(price, font=("Arial", 15), align="right")


#Main
#1. Introduction (Welcome to the Six Flags Ticket Generator!)

print("\n Welcome to the Griffin Museum of Science and Industry! If you'd like to plan a visit, please fill out this ticket form. \n" )

#2. Collect all of the pertinent information
# Name, Age, Day of Week, Coupon code
name = input("Enter your first and last name: ")
age = int(input("Enter your age: "))
day = input ("What day of the week are you visiting? ")
coupon_yn = input("Do you have a coupon code? (Yes/No) ")

#3. Algorithm for setting the price goes here

if age <= 3:
    price = 0
elif age >= 4 and age <= 17 and day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    price = 50 #half off for students during weekdays
else:
    price = 100
    
if coupon_yn == "Yes":
    coupon = input("Enter your coupon code: ")
    if coupon == "FREEFRIDAY" and age >= 4 and age <= 17 and day == "Friday":
        price = 0
    elif coupon == "SUNDAY10" and age >= 4 and age <=17 and day == "Sunday":
        price = price - 10 
    else:
        print("Sorry! That coupon is invalid.")
elif coupon_yn == "No":
    print("No coupon code entered. \n")

print("Generating ticket...")


#4. Generate ticket

draw_ticket(name, price, day, 0)




