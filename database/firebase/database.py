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
            print("Firebase : connect to Firebase")
            return True 

    def insert(self, uid, data):
        
        ref = db.reference('user/-{}/diary'.format(uid))
        user = User()
        user.setDiary(data)
        
        for data in user.getDiary():
            print(data.__dict__) 
            ref.push(data.__dict__)

    def update(self, uid, title, content):
        
        ref = db.reference('user/-MsSY3AmHgiDWeE4j4Ys/diary/-{}'.format(uid))
        
        data = { 
                'title':title,
                'content':content,
                'last_modified':datetime.datetime.now().isoformat()
            }
        
        ref.update(data)
                
    def delete(self, uid):
    
        ref = db.reference('user/-MsSY3AmHgiDWeE4j4Ys/diary')
        ref.child(uid).delete()
        
    def dtest(self, data):
        print(data)
        
    def find(self, data):
        ref = db.reference()
        user = ref.child(data).get()
        print(user)
    
    def login(self, user_id, user_pw):
            
        ref = db.reference('user')
        
        user_id_snapshot = ref.order_by_child('_id').equal_to(user_id).get()
        user_id_check = list(user_id_snapshot.values())
        
        if len(user_id_check) == 0:
            print("존재하지 않는 계정입니다.")
        
        elif len(user_id_check) > 0:
            
            user = User()
            
            for data in user_id_check:
                user_id = data.get('_id', None)
                user_pw = data.get('password', None)
                
                user.setId(user_id)
                user.setPassword(user_pw)
                user.setState(user.USER_STATE_CONNECT)
                print("connect {} {} {}".format(user_id, user_pw, user.getState()))
                
    def register(self, user_id, user_pw):

        user = User()
        user.setId(user_id)
        user.setPassword(user_pw)
        
        ref = db.reference('user')
        ref.push(user.__dict__)