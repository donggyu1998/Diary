import firebase_admin
import datetime
import json
from firebase_admin import credentials, firestore, db
from database.model.user import User

class Database:
    
    cert_file = "database/firebase/firebase_key.json"
    cred = credentials.Certificate(cert_file)
    database_url = "https://diary-73699-default-rtdb.firebaseio.com/"
    
    def __init__(self):
        self._client = None
        self._db = None
        self._user = None
        
    def connect(self):
        self._client = firebase_admin.initialize_app(self.cred, {'databaseURL' : self.database_url})

        if (self._client is None):
            print("Firebase : could not connect to Firebase")
            return False
        else:
            print("Firebase : connect to Firebase")
            return True 

    def insert(self):
        pass 
    
    def update(self):
        pass
    
    def delete(self):
        pass
    
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
            self._user = User()
            
            for user in user_id_check:
                user_id = user.get('_id', None)
                #user_pw = user.get('password', None)
                
    def register(self, user_id, user_pw):

        ref = db.reference('user')
        
        now = datetime.datetime.now()
        formatted_datetime = now.isoformat()
        create_at = json.dumps(formatted_datetime)
      
        ref.push({
            '_id' : user_id,
            'password' : user_pw,
            'create_at': create_at
        })