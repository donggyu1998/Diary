import datetime 
from database.dbmanager import DBManager
from database.model.user import User

class Diary:
    
    def __init__(self):
        
        self.title = None
        self.content = None
        self.last_modified = None
        self.create_at = datetime.datetime.now().isoformat()
    
    def setTitle(self, data):
        self.title = data
    
    def setContent(self, data):
        self.content = data
    
    def setLastModified(self, data):
        self.last_modified = data
        
    def insert(self, uid, title, content):
        
        diary = Diary()
        diary.setTitle(title)        
        diary.setContent(content)
        diary.setLastModified("None")
        
        dbmanager = DBManager.getInstance()
        dbmanager.insert(uid, diary)
        
    def find():
        pass

    def delete(self, uid):

        dbmanager = DBManager.getInstance()
        dbmanager.delete(uid)
    
    def update(self, uid, title, content):
        dbmanager = DBManager.getInstance()
        dbmanager.update(uid, title, content)