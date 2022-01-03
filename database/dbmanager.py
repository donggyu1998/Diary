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
        
    def insert(self, uid, data):
        self._db.insert(uid, data)
        
    def update(self, uid, title, content):
        self._db.update(uid, title, content)
        
    def delete(self, uid):
        self._db.delete(uid)
        
    def find(self, data):
        self._db.find(data)
        
    def login(self, user_id, user_pw):
        self._db.login(user_id, user_pw)
    
    def register(self, user_id, user_pw):
        self._db.register(user_id, user_pw)