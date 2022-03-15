import firebase_admin
from firebase_admin import credentials, db
from database.model.diary import Diary
from database.model.user import User

class Database:
    cred = credentials.Certificate("database/firebase/firebase_key.json")
    database_url = "firebase realtime database url"
    
    def __init__(self):
        self._client = None
        self._db = None
        
    def connect(self):
        self._client = firebase_admin.initialize_app(self.cred, {'databaseURL' : self.database_url})

        if (self._client is None):
            print ("Firebase : could not connect to Firebase. ")
            return False
        
        else:
            return True 

    def insertDiary(self, user, diary):
        ref = db.reference('user/{}/diary/'.format(user.getUid()))            
        child = ref.push(diary.__dict__)
        ret = diary.setUid(child.key)
        return ret
            
    def deleteDiary(self, user, diary_uid):
        ref = db.reference('user/{}/diary/{}'.format(user.getUid(), diary_uid))
        ret = ref.delete()
        return ret 
    
    def updateDiary(self, user, diary_uid, title, content, last_modified):
        ref = db.reference('user/{}/diary/{}'.format(user.getUid(), diary_uid))

        diary = Diary()
        diary.setTitle(title)
        diary.setContent(content)
        diary.setLastModified(last_modified)

        ret = ref.update(diary.__dict__)
        return ret
      
    def login(self, id, pw):
        ret = None
        
        ref = db.reference('user')
        
        snapshot = ref.order_by_child('_id').equal_to(id).get()
        items = list(snapshot.values())

        if len(items) <= 0:
            print ("Error : Account is None or exists, Try again. ")
            
        else:
            user_pw = items[0].get('password', None)

            if (pw != user_pw):
                print ("Error : The password is incorrect, Try again. ")
                
            else:
                ret = User()
                ret.applyJson(items[0]) 
                
                user_uid = list(snapshot.keys())[0]
                ret.setUid(user_uid)

                print ("Login Success. ")
                
        return ret

    def register(self, id, pw):
        ref = db.reference('user')

        snapshot = ref.order_by_child('_id').equal_to(id).get()
        items = list(snapshot.values())
        
        if len(items) <= 0:
            
            user = User()
            user.setId(id)
            user.setPassword(pw)
            
            ref.push(user.__dict__)
            print ("Register Success. ")

            return True
        
        else: 
            print ("Error : Account exists, Try again. ")
            return False
