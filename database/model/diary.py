import datetime 

class Diary:
    
    def __init__(self): # 유니크한 변수 : _ 가 앞에 붙음.
        self._uid = None
        self.title = None
        self.content = None 
        self.last_modified = None
        self.create_at = datetime.datetime.now().isoformat()
    
    def setUid(self, uid):
        self._uid = uid 
        
    def setTitle(self, data):
        self.title = data
    
    def setContent(self, data):
        self.content = data
    
    def setLastModified(self, data):
        self.last_modified = data
    
    def getUid(self):
        return self._uid
    
    def getTitle(self):
        return self.title
    
    def getContent(self):
        return self.content
    
    def getLastModified(self):
        return self.last_modified
    
    def printInfo(self):
        print ("************ Diary Info ************")
        print("Title : {title}\nContent : {content}\nLast_modified : {last_modified}\nCreate_at : {create_at}".format(
            title=self.title, content=self.content, last_modified=self.last_modified, create_at=self.create_at))     
        print ("************************************")   
        
    def applyJson(self, data):
        self.title = data.get('title', None)
        self.content = data.get('content', None)
        self.last_modified = data.get('last_modified', None)
        self.create_at = data.get('create_at', None)