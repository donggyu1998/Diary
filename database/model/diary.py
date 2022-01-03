import datetime 

class Diary:
    
    def __init__(self):
        # model class 는 set get data에 대한 정보만 
        self.title = None
        self.content = None 
        self.last_modified = None
        self.create_at = datetime.datetime.now().isoformat()
    
    def setTitle(self, data):
        self.title = data
    
    def setContent(self, data):
        self.content = data
    
    def setLastModified(self, data):
        self.last_modified = data
    
    def getTitle(self):
        return self.title
    
    def getContent(self):
        return self.content
    
    def getLastModified(self):
        return self.last_modified
    
    def printInfo(self):
        print("Diary Info")
        print("Title : {title}\nContent : {content}\nlast_modified : {last_modified}\ncreate_at : {create_at}".format(
            title=self.title, content=self.content, nlast_modified=self.last_modified, create_at=self.create_at))        
        
    def applyJson(self, data):
        self.title = data.get('title', None)
        self.content = data.get('content', None)
        self.last_modified = data.get('last_modified', None)
        self.create_at = data.get('create_at', None)