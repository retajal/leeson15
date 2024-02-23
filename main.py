#lesson 15 case 
#example 1
#ask how many phones yhey have

n = int(input("how many phones do you have ?"))
match n :#look in n شيك
    case 0 :
        print("why do you have no phones ?")
    case 1 :
        print("that is normal")
    case 2 :
        print("this good")
    case 3 :
        print("3 phones ???")
    case 4 :
        print("omg 4 !")

#example 2
#make function tell you what to do at traffic light
def whattodo(colour) :
    match colour :
        case "red" :
            return "stop"
        case "yellow" :
            return "dont start walking but countniou "
        case "green" :
            return "walk"
#ask them the coulour
x = input("what is the coulour :")
x = x.lower()
print(whattodo(x))

d = int(input("give me a day "))
match d :# we shouls writ match wheb we use the case
    case 0 :
        print("sun")
    case 1 :
        print("mon")
    case 2 :
        print("tue")
    case 3 :
        print("wed")
    case 4 :
        print("thur")
    case 5 :
        print("fri")
    case 6 :
        print("sat")
    case 7 :
        print("sun")
# we can also writ it in function

#example 3
print("hat is the past tense of to sim ")
print(" your choice are : swimed , swimming , swimmer ,swam ")
answer = input("what is the past tense of to sim ")
match answer :
    case "swimed" :
        print("worng")
    case "swimming" :
        print("worng")
    case "swimmer " :
        print("worng")
    case " swam" :
        print("yes")
