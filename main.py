
import os
import time
import menu.menulist as menulist
import menu.menuselect as menuselect
from database.dbmanager import DBManager
from pagestate import PageState

def page_login():

    menulist.previewMenuLoginList()
    selected = int(input("Select : "))
    
    if selected == 1:
        return menuselect.login()
        
    elif selected == 2:
        return menuselect.register()
    
def page_diary(user):

    menulist.previewMenuDiaryList(user)
    selected = int(input("Select : "))

    ret = True
    
    if selected == 1:
        menuselect.createDiary(user)

    elif selected == 2:
        menuselect.findDiary(user)
        
    elif selected == 3:
        menuselect.deleteDiary(user)

    elif selected == 4:
        menuselect.updateDiary(user)
        
    elif selected == 9:
        user = None
        return menuselect.logout(user)

    else:
        print ("Pls select valid item...")

    return ret
    
def main():

    global cur_page
    global user
    cur_page = PageState.PAGE_LOGIN
    user = None
    
    while True:
        os.system('cls')
        
        if cur_page == PageState.PAGE_LOGIN:
            ret = page_login()
            
            if not ((ret is None) or 
                    (ret is True) or 
                    (ret is False)):
                
                user = ret
                cur_page = PageState.PAGE_DIARY
            
        elif cur_page == PageState.PAGE_DIARY:
            ret = page_diary(user)
            
            if ret is False:
                cur_page = PageState.PAGE_LOGIN
                      
        time.sleep(0.5)

if __name__ == '__main__':

    dbmanager = DBManager.getInstance()
    main()


        