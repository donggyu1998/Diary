
import os
import time
import menu
from enum import Enum

class PageState(Enum):
    PAGE_LOGIN = 0
    PAGE_DIARY = 1
    
def displayMenu():
    
    global user 
    global cur_page
    
    if cur_page == PageState.PAGE_LOGIN:
        ret = menu.menuPageLogin()
        
        if not ((ret is None) or # 로그인 실패했을 경우
                (ret is True) or # 회원가입 성공했을 경우 
                (ret is False)): # 회원가입 실패했을 경우

            user = ret
            cur_page = PageState.PAGE_DIARY
            
    elif cur_page == PageState.PAGE_DIARY:
        ret = menu.menuPageDiary(user)
        
        if ret is False: # 로그아웃했을 경우
            cur_page = PageState.PAGE_LOGIN
        
cur_page = PageState.PAGE_LOGIN
user = None 
    
def main():

    while True:
        os.system('cls')
        displayMenu()
        time.sleep(0.5)
        
if __name__ == '__main__':
    main()
