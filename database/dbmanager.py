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
        
    def insert(self):
        self._db.insert()
        
    def update(self):
        self._db.update()
        
    def delete(self):
        self._db.delete()
        
    def find(self, data):
        self._db.find(data)
        
    def login(self, user_id, user_pw):
        self._db.login(user_id, user_pw)
    
    def register(self, user_id, user_pw):
        self._db.register(user_id, user_pw)