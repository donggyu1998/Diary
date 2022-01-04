import datetime

from database.model.diary import Diary
class User:
    
    def __init__(self): # 유니크한 변수 : _ 가 앞에 붙음.
        self._uid = None
        self._id = None
        self.password = None
        self.diary = []
        self.create_at = datetime.datetime.now().isoformat()
        
    def setUid(self, uid):
        self._uid = uid
        
    def setId(self, user_id):
        self._id = user_id
        
    def setPassword(self, password):
        self.password = password
        
    def setDiary(self, data):
        self.diary.append(data)
    
    def getId(self):
        return self._id
    
    def getPassword(self):
        return self.password
    
    def getDiary(self):
        return self.diary
    
    def getUid(self):
        return self._uid
    
    def refreshDiary(self, snapshot):

        if len(snapshot) > 0:

            self.diary = []

            for key, data in snapshot.items():

                diary = Diary()
                diary.setUid(key)
                diary.applyJson(data)
                self.diary.append(diary)
                                
    def applyJson(self, data):
        
        self._id = data.get('_id', None)
        self.password = data.get('password', None)

        dic_diary = data.get('diary', {})
        self.diary = []
        
        if len(dic_diary) > 0:

            for key, data in dic_diary.items():

                diary = Diary()
                diary.setUid(key)
                diary.applyJson(data)
                self.diary.append(diary)
            
        self.create_at = data.get('create_at', None)