#Diary project in python

#Idea and coded by Rounak

import os
import sys
import datetime

set_pass = "abrakadabra" #preset password

#function specially made for protecting your diary
def password_match(a):
    if(a==set_pass):
        print("Your entered password is right\n")
        print("You may procede")
    else:
        print("The entered password is wrong")
        exit(1)

#New event function to add new event into ypur diary
def new_event():
    print("Enter the password")
    a=input()
    password_match(a)
        
    print("You have entered the diary")
    myfilename =input("Enter the name you want to save this day as")
    f_object=open((myfilename),"w+")
    #Funtion to import the system date into the code
    #Wherer current_dt is an object 
    current_dt = datetime.datetime.now()
    f_object.write(str(current_dt))
    f_object.write("\n")
    print("Start writing the event")
    event ="""    """ #This is a multi-line string and thats why three quotation marks are used 
    event=input()
    f_object.write(event)
    f2_object=open("Diary_list1.txt","a+")
    f2_object.write(myfilename)
    f2_object.write("\n")
    f_object.close()
    f2_object.close()

   
def read_event():
    print("Lets check out your contents")
    f2_object=open("Diary_list1.txt","r")
    content=f2_object.read()
    print(content)
    print("Enter the 'event name' you want to open")
    ev_name=input()
    f3_object=open((ev_name),"r+")
    content2=f3_object.read()
    print(content2)


def edit_event():
    print("Enter the password")
    a=input()
    password_match(a)
    
    print("check for the event you want to edit or delete\n")
    f2_object=open("Diary_list1.txt","r")
    content=f2_object.read()
    print(content)
    print("Enter the 'event name' you want to edit")
    ev_name=input()
    f4_object=open((ev_name),"a+")
    print("add if anything you want to add\n")
    event2=""" """
    event2=input()
    f4_object.write("\n")
    f4_object.write(event2)
    
    
def main_func():
    print("\t\tWelcome to your Diary\n")

    print("\t\tPress '1' for writing new event\n")
    print("\t\tPress '2' for checking out past events\n")
    print("\t\tPress '3' for editing past events\n")

    x=int(input())

    if(x==1):
        new_event()
        print("\t\tPress '4' to go back\n")
        print("\t\tPress '5' to exit\n")
        y=int(input())
        if(y==4):
            main_func()
        elif(y==5):
            exit(0)
        
    elif(x==2):
        read_event()
        print("\t\tPress '4' to go back\n")
        print("\t\tPress '5' to exit\n")
        y=int(input())
        if(y==4):
            main_func()
        elif(y==5):
            exit(0)
        
    elif(x==3):
        edit_event()
        print("\t\tPress '4' to go back\n")
        print("\t\tPress '5' to exit\n")
        y=int(input())
        if(y==4):
            main_func()
        elif(y==5):
            exit(0)
        
main_func()
            
