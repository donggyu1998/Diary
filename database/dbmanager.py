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
        
    def insertDiary(self, user_uid, diary):
        ret = self._db.insertDiary(user_uid, diary)
        return ret
    
    def deleteDiary(self, user_uid, diary_uid):
        ret = self._db.deleteDiary(user_uid, diary_uid)
        return ret
    
    def updateDiary(self, user_uid, diary_uid, title, content, last_modified):
        ret = self._db.updateDiary(user_uid, diary_uid, title, content, last_modified)
        return ret
    
    def login(self, user_id, user_pw):
        ret = self._db.login(user_id, user_pw)
        return ret
    
    def register(self, user_id, user_pw):
        ret = self._db.register(user_id, user_pw)
        return ret