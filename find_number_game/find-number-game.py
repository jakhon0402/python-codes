import random 
import time

print("Keling son topish o'yini o'ynaymiz !!!")

def game1():
    ### EN: In this part of the game, the computer thinks of number from 1 to 10. And you will find.
    ### UZ: O'yinning ushbu qismida kompyuter 1 dan 10 gacha son o'ylaydi. Siz esa topasiz.
    compnumber = random.randint(1,10)   # Kompyuter o'ylagan son
    s=1  # Dastlabki urinish
    mynumber = int(input("1 dan 10 gacha son o'yladim. Ushbu sonni topa olasizmi? \n"))  # Siz kiritayotgan son
     # 
    while True : 
        if compnumber > mynumber : # Kompyuter o'ylagan son siz o'ylagan sondan katta bo'lgan holat
            mynumber = int(input("Men o'ylagan son ushbu sondan katta. Boshqa son kiriting :")) 
        elif compnumber < mynumber : # Kompyuter o'ylagan son siz o'ylagan sondan kichik bo'lgan holat
            mynumber = int(input("Men o'ylagan son ushbu sondan kichkina. Boshqa son kiriting :"))
        elif compnumber == mynumber : break # ompyuter o'ylagan son topilgan holat
        s+=1  # Urinishlarning ortib borishi
    
    print(f"Tabriklayman Topdingiz!!! Siz {s} ta urunishda topdingiz.") 
    return s # Ushbu funksiya urinishlar sonini qaytaradi.

def game2():
    ### EN: In this part of the game you think of numbers from 1 to 10. And the computer finds.
    ### UZ: O'yinning ushbu qismida siz 1 dan 10 gacha son o'ylaysiz. Kompyuter esa topadi.

    print("Endi sizni galingiz. Siz 1 dan 10 gacha son o'ylang (10 sekund ichida) men esa topishga harakat qilaman.\n")
    time.sleep(10)
    begin = 1 
    end = 10
    compnumber = random.randint(begin,end) # Kompyuter o'ylagan son
    s=1 # Dastlabki urinish
    while True:
        check = input(f"Men {compnumber} soni deb o'yladim. Siz o'ylagan son {compnumber} dan katta bo'lsa (+), kichik bo'lsa (-), tog'ri bo'lsa (t)") # Kompyuter o'ylagan sonni tekshirish qismi
        if check == "-" :  # siz o'ylagan son kichik bo'lgan holat
            end = compnumber-1
            compnumber = random.randint(begin,compnumber-1)
            
        elif check == "+" : # siz o'ylagan son katta bo'lgan holat
            begin = compnumber+1
            compnumber = random.randint(compnumber+1,end)
            
        elif check == "t" : break # siz o'ylagan son to'g'ri bo'lgan holat
        s+=1  # Urinishlarning ortib borishi
    print(f"Urra!!! Men {s} ta urunishda topdim")
    return s # Ushbu funksiya urinishlar sonini qaytaradi.
    
# START GAME
while True:
    # O'yinning 1-qismi
    myscore = game1() 
    # O'yinning 2-qismi
    compscore = game2()
    # Urinishlar soniga qarab yutganligini aniqlanadi. Urinishlar soni kichikligi yutganligini anglatadi.
    if myscore < compscore :
        print(f"Siz yutdingiz!!! {myscore}:{compscore}")
    elif myscore > compscore :
        print(f"Siz yutqizdingiz!!! {myscore}:{compscore}  ( Hafa bo'lmang. )")
    elif myscore == compscore :
        print(f"Durrang!!! {myscore}:{compscore}")

    endgame = int(input("Yana o'ynaymizmi? HA(1) YO'Q(0)"))
    if endgame == 0 : break



