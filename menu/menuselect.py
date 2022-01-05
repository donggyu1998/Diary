import datetime
from database.dbmanager import DBManager
from database.model.diary import Diary

def login():
    
    dbmanager = DBManager.getInstance()
        
    id = input("ID : ")
    pw = input("PW : ")
    
    ret = dbmanager.login(id, pw)
    
    if ret is None:
        input ("Error : Pls Check ID/PW... ( If you want to retry, press enter. )")

    return ret

def register():
    
    dbmanager = DBManager.getInstance()
    
    id = input("ID : ")
    pw = input("PW : ")
    
    ret = dbmanager.register(id, pw)
    
    if ret is False:
        input ("Error : Pls Check ID/PW... ( If you want to retry, press enter. )")
        
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
    diaries = user.diary
    
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
            
            diary_items = diaries[selected]
            diary_uid = diary_items.getUid()
            
            diary_items.setTitle(title)
            diary_items.setContent(content)
            diary_items.setLastModified(datetime.datetime.now().isoformat())
            
            dbmanager = DBManager.getInstance()
            dbmanager.updateDiary(user, diary_uid, diary_items.getTitle(), diary_items.getContent(), diary_items.getLastModified())    
            
        else:
            print ("Error : Index out of range exception.")
            
    input ("Press enter key to continue...")
    
def logout(user):
    print ("LOGOUT ... ")
    ret = False
    return ret
