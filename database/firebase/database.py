import firebase_admin
import json
import datetime
from firebase_admin import credentials, firestore, db
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
            print("Firebase : could not connect to Firebase")
            return False
        
        else:
            return True 

    def insert_diary(self, uid, diary):

        ref = db.reference('user/{}/diary'.format(uid))            
        ret = ref.push(diary.__dict__)
        return ret
    
    def find_all_diaries(self, uid, user):

        ref = db.reference('user/{}/diary'.format(uid))

        items = ref.get()
        user.diary.clear()

        for diary in items.values():
            ret = user.setDiary(diary)     
        
        return ret
        
    def delete(self, user_id):
        ref = db.reference('user/{}/diary'.format(user_id))
        ref.child(user_id).delete()
        
    def update(self, uid, title, content):
        
        ref = db.reference('user/-MsSY3AmHgiDWeE4j4Ys/diary/-{}'.format(uid))
        
        data = { 
                'title':title,
                'content':content,
                'last_modified':datetime.datetime.now().isoformat()
            }
        
        ref.update(data)
        
    def login(self, id, pw):
            
        ret = None
            
        ref = db.reference('user')
        
        snapshot_id = ref.order_by_child('_id').equal_to(id).get()
        
        items = list(snapshot_id.values())

        if len(items) <= 0:
            print("Firebase : 존재하지 않는 계정입니다.")
            
        else:
            check_pw = items[0].get('password', None)
            
            if (pw != check_pw):
                print("Firebase : 비밀번호가 맞지 않습니다.")
                
            else:
                ret = User()
                ret.applyJson(items[0]) 
                
                user_uid = list(snapshot_id.keys())[0]
                ret.setUid(user_uid)

                print("Firebase : 로그인 성공")
                
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
            print("Firebase : 회원가입 성공")
        else: 
            print("Firebase : 존재하는 계정입니다.")
        