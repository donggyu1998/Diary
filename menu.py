import datetime
from database.dbmanager import DBManager
from database.model.diary import Diary

def menuPageLogin():
    print ("************ MENU Login ************")
    print ("1) Login")
    print ("2) Register")
    print ("************************************")
    selected = int(input("Select : "))
    
    if selected == 1:
        return menuLogin()

    elif selected == 2:
        return menuRegister()
    
def menuLogin():
    dbmanager = DBManager.getInstance()
        
    id = input("ID : ")
    pw = input("PW : ")
    
    ret = dbmanager.login(id, pw)
    
    if ret is None:
        input ("Error : Pls Check ID/PW... ( If you want to retry, press enter. )")

    return ret

def menuRegister():
    dbmanager = DBManager.getInstance()
    
    id = input("ID : ")
    pw = input("PW : ")
    
    ret = dbmanager.register(id, pw)
    
    if ret is False:
        
        input ("Error : Pls Check ID/PW... ( If you want to retry, press enter. )")
        
    return ret

def menuPageDiary(user):
    
    print ("[ UserInfo : {}] ".format(user._id))
    print ("************ Menu List ************")
    print ("1) Create new diary")
    print ("2) Find diary")
    print ("3) Delete diary")
    print ("4) Update diary")
    print ("------------------------------------")
    print ("9) Logout")
    print ("************************************")
    selected = int(input("Select : "))

    ret = True
    
    if selected == 1:
        createDiary(user)
    
    elif selected == 2:
        findDiary(user)
        
    elif selected == 3:
        deleteDiary(user)

    elif selected == 4:
        updateDiary(user)
        
    elif selected == 9:
        user = None
        return logout()

    else:
        print ("Pls select valid item...")

    return ret

def createDiary(user):
    
    print (" * Create New Diary * ")
    
    title = input(" - Title : ")
    content = input(" - Content : ")
    
    diary = Diary()
    diary.setTitle(title)
    diary.setContent(content)
    user.setDiary(diary)
    
    dbmanager = DBManager.getInstance()    
    dbmanager.insertDiary(user, diary)
    
    print (" Info : Successed create new diary ! ")
        
def findDiary(user):
    
    print (" * Find Diary * ")
    
    diaries = user.getDiary()
    
    if len(diaries) == 0:
        print ("Info : Diary is empty. ")
        
    else:
        for i in range(len(diaries)):
            diary = diaries[i]
            print (" {}) Title : {} | Create_at : {} ".format(i, diary.title, diary.create_at))
        
        selected = int(input("Select : "))
                   
        if selected < len(diaries):
            diary = diaries[selected]
            diary.printInfo()
        
        else:
            print ("Error : Index out of range exception. ")
            
    input ("Press enter key to continue...")
        
def deleteDiary(user):
    
    print (" * Delete Diary * ")
    
    diaries = user.getDiary()
    
    if len(diaries) == 0:
        print ("Info : Diary is empty. ")
        
    else:
        for i in range(len(diaries)):
            diary = diaries[i]
            print ("{}) Title : {} | Create_at : {}".format(i, diary.title, diary.create_at))
            
        selected = int(input("Select : "))
        
        if selected < len(diaries):
            diary = diaries[selected]
            diaries.pop(selected)

            dbmanager = DBManager.getInstance()
            dbmanager.deleteDiary(user, diary._uid)
            
        else:
            print ("Error : Index out of range exception. ")
            
    input ("Press enter key to continue...")
    
def updateDiary(user):
    
    print (" * Update Diary * ")
    
    diaries = user.getDiary()
    
    if len(diaries) == 0:
        print ("Info : Diary is empty.")
    
    else:
        for i in range(len(diaries)):
            diary =  diaries[i]
            print ("{}) Title : {} | Create_at : {}".format(i, diary.title, diary.create_at))
            
        selected = int(input("Select : "))
        
        if selected < len(diaries):
            diary = diaries[selected]
            
            title = input(" - Title : ")
            content = input(" - Content : ")
            
            diary = diaries[selected]
            diary_uid = diary.getUid()
            
            diary.setTitle(title)
            diary.setContent(content)
            diary.setLastModified(datetime.datetime.now().isoformat())
            
            dbmanager = DBManager.getInstance()
            dbmanager.updateDiary(user, diary_uid, diary.getTitle(), diary.getContent(), diary.getLastModified())    
            
        else:
            print ("Error : Index out of range exception.")
            
    input ("Press enter key to continue...")
    
def logout():
    print ("LOGOUT ... ")
    
    ret = False
    return ret