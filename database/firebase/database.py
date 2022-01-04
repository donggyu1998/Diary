import firebase_admin
from firebase_admin import credentials, db
from database.model.diary import Diary
from database.model.user import User

class Database:
    cert_file = "database/firebase/firebase_key.json"
    cred = credentials.Certificate(cert_file)
    database_url = "https://diary-73699-default-rtdb.firebaseio.com/"
    
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

    def insertDiary(self, user_uid, diary):
        ref = db.reference('user/{}/diary/'.format(user_uid))            
        ref.push(diary.__dict__)
        
        snapshot = ref.get()

        ret = User()
        ret.refreshDiary(snapshot)
        
        return ret
            
    def deleteDiary(self, user_uid, diary_uid):
        ref = db.reference('user/{}/diary/{}'.format(user_uid, diary_uid))
        ret = ref.delete()
        
        return ret 
    
    def updateDiary(self, user_uid, diary_uid, title, content, last_modified):
        ref = db.reference('user/{}/diary/{}'.format(user_uid, diary_uid))

        diary = Diary()
        diary.setTitle(title)
        diary.setContent(content)
        diary.setLastModified(last_modified)

        ret = ref.update(diary.__dict__)
        return ret
      
    def login(self, id, pw):
        ret = None
        ref = db.reference('user')
        
        snapshot_id = ref.order_by_child('_id').equal_to(id).get()
        items = list(snapshot_id.values())

        if len(items) <= 0:
            print ("Error : Account exists, Try again. ")
            
        else:
            for check in items:
                check_pw = check.get('password', None)
            
            if (pw != check_pw):
                print ("Error : The password is incorrect, Try again. ")
                
            else:
                ret = User()
                ret.applyJson(items[0]) 
                
                user_uid = list(snapshot_id.keys())[0]
                ret.setUid(user_uid)

                print ("Login Success. ")
                
            return ret

    def register(self, user_id, user_pw):
        ref = db.reference('user')

        snapshot_id = ref.order_by_child('_id').equal_to(user_id).get()
        items = list(snapshot_id.values())
        
        if len(items) <= 0:
            user = User()
            user.setId(user_id)
            user.setPassword(user_pw)
            
            ref.push(user.__dict__)
            print ("Register Success. ")
            
        else: 
            print ("Error : Account exists, Try again. ")
        