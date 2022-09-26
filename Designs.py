def rangoli():
    try:
        n = int(input("Enter a number from 1-26: "))
        l = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
        m = 1
        j = (n * 2 - 1) + (n * 2 - 2)
        k = 1
        lis = []
        for i in range(n):
            string = ""
            for i in reversed(range(m, n + 1)):
                string = string + l[i] + "-"
            for i in range(m + 1, n + 1):
                string = string + l[i] + "-"
            m += 1
            result = (string[:-1].center(j, "-"))
            lis.append(result)
        for i in reversed(lis):
            print(i)

        for i in lis:
            if i == lis[0]:
                pass
            else:
                print(i)
        return "Alphabetical rangoli is Awsome"
    except IndexError:
        print("There are only 26 alphabets. So you have to enter a number in range 1-26")
        input("Press Enter for restart the programme")
        print(rangoli())
        return ""

def door_mat():
    try:
        print("Enter 2 space separte value. Make sure that num2 is triple of num1")
        n, m = map(int, input().split())
        inp = ".|."
        md = inp.center(21, "-")
        for i in range(1, int(n / 2) + 1):
            p = i * 2 - 1
            inp = (".|." * p).center(m, "-")
            print(inp)
        print("welcome".center(m, '-'))
        for i in reversed(range(1, int(n / 2) + 1)):
            p = i * 2 - 1
            inp = (".|." * p).center(m, "-")
            print(inp)
    except:
        print("You have to Enter the height and width separeted with space.\nFor example, If the mat height=7 and width =21 then you have to enter the value as 7 21 ")
        input("Press Enter for restart the programme")
        print(door_mat())
        return ""
    if m != n*3:
        print("Your mat width is not equal to triple of height. Mat may be not created properly")
    else:
        return "Door mat created sucsessfully"

def dual_style():
    try:
        num = int(input())
        l = []
        for i in range(num, 0, -2):
            result = ("@" * (num - i + 1)).center(num)
            l.append(result)

        for i in range(3, num + 1, 2):
            result = ("@" * (num - i + 1)).center(num)

        string = ""
        for i in l:
            string = i + i
            print(string)
        for i in reversed(l):
            if i == l[-1]:
                pass
            else:
                string = i + i
                print(string)
    except ValueError:
        print("Entered input is not an Intiger")
        input(">>Press enter for restart the progranne")
        print(dual_style())
        return ""

    return "Style created sucsessfully"

def line_design():
    try:
        n = int(input("Enter any number: "))
        for i in range(n):
            string = ""
            string = string + (" # " * i) + (" @ ") + " # " * (n - i - 1)
            print(string)
    except ValueError:
        print("Entered input is not an Intiger")
        input(">>Press enter for restart the progranne")
        print(line_design())
        return ""
    return "Simple programe for replace the main digonal charecters"

def multi_tringle_design():
    try:
        print("This programme can performe properly with odd numbers")
        num = int(input("Enter a odd number:"))

        for i in range(0, num, 2):
            result = ("@" * (num - i)).center(num)
            print(result)
        for i in range(num - 1, 0, -2):
            result = ("@" * (num - i + 2)).center(num)
            print(result)
    except ValueError:
        print("Entered input is not an Intiger")
        input(">>Press enter for restart the progranne")
        print(multi_tringle_design())
        return ""
    if num % 2 == 0:
        return "You are enterd a even numnber. So the design didn't create properly"
    else:
        return "Multitringle created sucsessfully"

while True:
    try:
        print("\nThis programme can performe some designs listed below")
        inp = int(input(" 1: Alphabetical rangoli\n 2: Door mat\n 3: Dual style\n 4: line design\n 5: Multi Tringle Design\n 6:Exit programme\nEmter the design number: "))
        if inp == 1:
            print(rangoli())
            input("press Enter for Main Menu>")
        elif inp == 2:
            print(door_mat())
            input("press Enter for Main Menu>")
        elif inp == 3:
            print(dual_style())
            input("press Enter for Main Menu>")
        elif inp == 4:
            print(line_design())
            input("press Enter for Main Menu>")
        elif inp == 5:
            print(multi_tringle_design())
            input("press Enter for Main Menu>")
        elif inp == 6:
            print(">>>Programme closed sucsessfully")
            break
        else:
            print(">>>Wrong Selaction")
    except ValueError:
        print(">>>Your Input is not a number, Check and try again...")