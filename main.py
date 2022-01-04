
import os
import time
import datetime
from database.dbmanager import DBManager
from database.model.diary import Diary
from pagestate import PageState

def page_login():
    print ("************ MENU LOGIN ************")
    print ("1) Login")
    print ("2) Register")
    print ("************************************")
    selected = int(input("Select : "))
    
    if selected == 1:
        id = input("ID : ")
        pw = input("PW : ")
        ret = dbmanager.login(id, pw)

        if ret is None:
            input ("Error : Pls Check ID/PW... ( If you want to retry, press enter. )")

        return ret
    
    elif selected == 2:
        id = input("ID : ")
        pw = input("PW : ")
        
        ret = dbmanager.register(id, pw)
        
        if ret is None:
            input ("Error : Pls Check ID/PW... ( If you want to retry, press enter. )")
            
        return ret
    
def page_diary(user):
    
    print ("[ UserInfo : {}] ".format(user._id))
    print ("************ Menu Diary ************")
    print ("1) Create new diary")
    print ("2) Find diary")
    print ("3) Delete diary")
    print ("4) Update diary")
    print ("------------------------------------")
    print ("9) Logout")
    print ("************************************")
    selected = int(input(" Select : "))

    ret = True

    if selected == 1:
        print (" * Create New Diary * ")
        
        title = input(" - Title : ")
        content = input(" - Content : ")

        diary = Diary()
        diary.setTitle(title)
        diary.setContent(content)
        user.setDiary(diary)
        
        dbmanager.insertDiary(user._uid, diary)

        print (" Info : Successed create new diary ! ")

    elif selected == 2:
        print (" * Find Diary * ")
        diaries = user.getDiary()
        
        if len(diaries) == 0:
            print ("Info : Diary is empty. ")
            
        else:
            for i in range(len(diaries)):
                diary = diaries[i]
                print (" {}) Title : {} | Create_at : {} {}".format(i, diary.title, diary.create_at, diary._uid))
            
            selected = int(input(" Select : "))
                       
            if selected < len(diaries):
                diary = diaries[selected]
                diary.printInfo()
            
            else:
                print ("Error : Index out of range exception. ")

        input ("Press enter key to continue...")

    elif selected == 3:
        print (" * Delete Diary * ")
        diaries = user.getDiary()

        if len(diaries) == 0:
            print ("Info : Diary is empty. ")
            
        else:
            for i in range(len(diaries)):
                diary = diaries[i]
                print ("{}) Title : {} | Create_at : {}".format(i, diary.title, diary.create_at))

            selected = int(input(" Select : "))

            if selected < len(diaries):
                diary = diaries[selected]
                diaries.pop(selected)
                dbmanager.deleteDiary(user._uid, diary._uid)
                
            else:
                print ("Error : Index out of range exception. ")

        input ("Press enter key to continue...")

    elif selected == 4:
        print (" * Update Diary * ")
        diaries = user.diary
        
        if len(diaries) == 0:
            print ("Info : Diary is empty.")
        
        else:
            for i in range(len(diaries)):
                diary =  diaries[i]
                print ("{}) Title : {} | Create_at : {}".format(i, diary.title, diary.create_at))
                
            selected = int(input(" Select : "))
            
            if selected < len(diaries):
                diary = diaries[selected]
                
                title = input(" - Title : ")
                content = input(" - Content : ")
                
                diary_items = diaries[selected]
                diary_uid = diary_items.getUid()
                
                diary_items.setTitle(title)
                diary_items.setContent(content)
                diary_items.setLastModified(datetime.datetime.now().isoformat())
                
                dbmanager.updateDiary(user._uid, diary_uid, diary_items.getTitle(), diary_items.getContent(), diary_items.getLastModified())    
                
            else:
                
                print ("Error : Index out of range exception.")

        input ("Press enter key to continue...")
        
    elif selected == 9:
        print ("LOGOUT ... ")
        user = None
        ret = False

    else:
        print ("Pls select valid item...")

    return ret


def print_menu():

    global cur_page
    global user

    # os.system('cls') # clear terminal

    if cur_page == PageState.PAGE_LOGIN:
        user = page_login()
        
        if user is not None:
            cur_page = PageState.PAGE_DIARY

    elif cur_page == PageState.PAGE_DIARY:
        ret = page_diary(user)
        
        if ret is False:
            cur_page = PageState.PAGE_LOGIN        

    time.sleep(0.5)

user = None
cur_page = PageState.PAGE_LOGIN

if __name__ == '__main__':

    dbmanager = DBManager.getInstance()
    
    while True:
        print_menu()

