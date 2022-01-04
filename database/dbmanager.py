from database.firebase.database import Database

class DBManager:
    
    __instance = None
    
    @classmethod
    def getInstance(cls):
        
        if cls.__instance == None:
            cls.__instance = DBManager()
            
        return cls.__instance
    
    def __init__(self):
        self._db = Database()
        self._db.connect()
        
    def insertDiary(self, user, diary):
        ret = self._db.insertDiary(user, diary)
        return ret
    
    def deleteDiary(self, user, diary_uid):
        ret = self._db.deleteDiary(user, diary_uid)
        return ret
    
    def updateDiary(self, user, diary_uid, title, content, last_modified):
        ret = self._db.updateDiary(user, diary_uid, title, content, last_modified)
        return ret
    
    def login(self, id, pw):
        ret = self._db.login(id, pw)
        return ret
    
    def register(self, id, pw):
        ret = self._db.register(id, pw)
        return ret