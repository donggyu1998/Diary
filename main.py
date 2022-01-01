from database.dbmanager import DBManager
from database.model.user import User
from optparse import Option, OptionParser

def main():

    dbmanager = DBManager.getInstance()
    user = User()

    parser = OptionParser()
    parser.add_option("-l", "--login", dest="login", type='str', help="cmd -lo [id],[password]")
    parser.add_option("-r", "--register", dest="register", type='str', help="cmd -re [id],[password]")
    parser.add_option("-f", "--find", dest="find", type='str', help="cmd : -f [reference]")
    
    (options, args) = parser.parse_args()
    
    if options.login:
        data = options.login.split(',')
        user_id = data[0]
        user_pw = data[1]

    elif options.register:
        data = options.register.split(',')
        user_id = data[0]
        user_pw = data[1]
        dbmanager.register(user_id, user_pw)
    
    elif options.find:
        data = options.find
        dbmanager.find(data)     
if __name__ == "__main__":
    main()