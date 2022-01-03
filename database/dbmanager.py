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
        
    def insert_diary(self, uid, diary):
        self._db.insert_diary(uid, diary)
    
    def get_all_diaries(self, uid, user):
        self._db.get_all_diaries(uid, user)
        
    def update(self, uid, title, content):
        self._db.update(uid, title, content)
        
    def delete(self, uid):
        self._db.delete(uid)
        
    def login(self, user_id, user_pw):
        return self._db.login(user_id, user_pw)
    
    def register(self, user_id, user_pw):
        self._db.register(user_id, user_pw)