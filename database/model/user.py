import datetime
class User:

    USER_STATE_NOT_CONNECT = 1
    USER_STATE_CONNECT = 2
    
    def __init__(self): 
        self._id = None
        self.password = None
        self.diary = []
        self.state = User.USER_STATE_NOT_CONNECT
        self.create_at = datetime.datetime.now().isoformat()
        
    def setId(self, user_id):
        self._id = user_id
        
    def setPassword(self, password):
        self.password = password
        
    def setState(self, state):
        self.state = state
    
    def setDiary(self, data):
        self.diary.append(data)
        
    def getId(self):
        return self._id
    
    def getPassword(self):
        return self.password
    
    def getState(self):
        return self.state
    
    def getDiary(self):
        return self.diary
    
    def applyJson(self, data):
        pass