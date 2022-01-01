class User:

    def __init__(self): 
        
        self._id = None
        self.password = None
        
    def setId(self, user_id):
        self._id = user_id
        
    def setPassword(self, password):
        self.password = password
        
    def getId(self):
        return self._id
    
    def getPassword(self):
        return self.password
 