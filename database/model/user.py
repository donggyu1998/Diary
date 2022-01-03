import datetime

from database.model.diary import Diary
class User:
    
    def __init__(self): # 유니크한 변수 : _ 가 앞에 붙음.
        self._uid = None
        self._id = None
        self.password = None
        self.diary = []
        self.create_at = datetime.datetime.now().isoformat()
        
    def setId(self, user_id):
        self._id = user_id
        
    def setPassword(self, password):
        self.password = password
        
    def setDiary(self, data):
        self.diary.append(data)
    
    def setUid(self, uid):
        self._uid = uid
        
    def getId(self):
        return self._id
    
    def getPassword(self):
        return self.password
    
    def getDiary(self):
        return self.diary
    
    def getUid(self):
        return self._uid
    
    def applyJson(self, data):
        self._id = data.get('_id', None)
        self.password = data.get('password', None)
        
        self.diary = []
        
        dic_diary = data.get('diary', {})
        diary = Diary()
        
        for data in list(dic_diary.values()):
        
            diary.applyJson(data)
            self.diary.append(diary)

        self.create_at = data.get('create_at', None)