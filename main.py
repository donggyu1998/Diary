from database.dbmanager import DBManager
from database.model.user import User
from database.model.diary import Diary
from optparse import Option, OptionParser

def main():

    dbmanager = DBManager.getInstance()
    user = User()
    
    parser = OptionParser()
    parser.add_option("-l", "--login", dest="login", type='str', help="cmd -l [id],[password]")
    parser.add_option("-o", "--logout", dest="logout", type='str', help="cmd : -o [id]")
    parser.add_option("-r", "--register", dest="register", type='str', help="cmd -r [id],[password]")
    
    parser.add_option("-i", "--insert", dest="insert", type='str', help="cmd : -w [uid],[title],[content]")
    parser.add_option("-f", "--find", dest="find", type='str', help="cmd : -f [reference]")
    parser.add_option("-d", "--delete", dest="delete", type='str', help="cmd : -d [uid ( key )]")
    parser.add_option("-u", "--update", dest="update", type='str', help="cmd : -u [uid],[title],[content]")
    
    (options, args) = parser.parse_args()
        
    if options.login:
         
        data = options.login.split(',')
        user_id = data[0]
        user_pw = data[1]
        
        dbmanager.login(user_id, user_pw)

    elif options.logout:
        
        data = options.logout
        print(data)
                
    elif options.register:
        
        data = options.register.split(',')
        user_id = data[0]
        user_pw = data[1]
    
        dbmanager.register(user_id, user_pw)
    
    elif options.find:
        
        data = options.find
        dbmanager.find(data)
        
    elif options.insert:
        
        data = options.insert.split(',')
        uid = data[0]
        title = data[1]
        content = data[2]
        
        diary = Diary()
        diary.insert(uid, title, content)

    elif options.delete:
        
        uid = options.delete
        
        diary = Diary()
        diary.delete(uid)
    
    elif options.update:
        
        data = options.update.split(',')
        uid = data[0]
        title = data[1]
        content = data[2]
        
        diary = Diary()
        diary.update(uid, title, content)    
    
    # 로그인 상태 유지 및 판단하여 동작
    # find
                
if __name__ == "__main__":
    main()