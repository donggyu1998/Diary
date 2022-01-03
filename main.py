
import os
import time
from database.dbmanager import DBManager
from database.model.diary import Diary
from enum import Enum


class PageState(Enum):
    PAGE_LOGIN = 0
    PAGE_DIARY = 1

def page_login():

    print ("************ MENU LOGIN ************")
    id = input("ID : ")
    pw = input("PW : ")
    print ("************************************")

    ret = dbmanager.login(id, pw)

    if ret is None:
        input ("Please Check ID/PW... ( if you want to retry, press enter. )")

    return ret

def page_diary(user):
    print ("[ UserInfo : {}] ".format(user._id))
    print ("************ MENU DIARY ************")
    print ("1) Create new diary")
    print ("2) Find diary")
    print ("3) Delete diary")
    print ("------------------------------------")
    print ("9) Logout")
    print ("************************************")
    selected = int(input("select : "))

    ret = True

    if selected == 1:
        print (" * Create new diary * ")
        
        title = input(" - title : ")
        content = input(" - content : ")

        diary = Diary()
        diary.setTitle(title)
        diary.setContent(content)
        dbmanager.insert_diary(user._uid, diary)

        print (" Successed Create New Diary ! ")

    elif selected == 2:
        print (" * Find diary * ")

        diaries = dbmanager.find_all_diaries(user._uid, user)
        diaries = []
        
        if len(diaries) == 0:
            print (" Diary is Empty ")
            
        else:
            for i in range(len(diaries)):
                diary = diaries[i]
                print ("{}) {} _ {}", i, diary.title, diary.created_at)

            selected = int(input("selected : "))

            if selected < len(diaries):
                diary = diaries[selected]
                diary.printInfo()
                
            else:
                print ("~ index out of range exception ~")

        input ("Press enter key to continue...")

    elif selected == 3:
        print (" * Delete diary * ")

        diaries = dbmanager.get_all_diaries(user)
        diaries = []

        if len(diaries) == 0:
            print ("Diary is empty")
        else:
            for i in range(len(diaries)):
                diary = diaries[i]
                print ("{}) {} _ {}", i, diary.title, diary.created_at)

            selected = int(input("selected : "))

            if selected < len(diaries):
                diary = diaries[selected]
                # delete diary
            else:
                print ("~ index out of range exception ~")

        input ("Press enter key to continue...")

    elif selected == 9:
        print ("LOGOUT ... ")
        user = None
        ret = False

    else:
        print ("Plz select valid item...")

    return ret


def print_menu():

    global cur_page
    global user

    #os.system('cls') # clear terminal

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

