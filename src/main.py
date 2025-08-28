"""
Implement User Management System
"""

import json

from enum import Enum

class Role(Enum):
    ADMIN = "admin"
    EDITOR = "editor"
    VIEWER = "viewer"

users = {
    "xaqxaq" : {
        "name" : "sung",
        "birthdate" : "961105",
        "id" : "xaqxaq",
        "password" : "password",
        "role" : Role.ADMIN
    },
    "qwer" : {
        "name" : "kim",
        "birthdate" : "971206",
        "id" : "qwer",
        "password" : "password1",
        "role" : Role.EDITOR
    },
    "asdf" : {
        "name" : "park",
        "birthdate" : "980107",
        "id" : "asdf",
        "password" : "password2",
        "role" : Role.VIEWER
    }
}

print("-"*20 + "User LIST" + "-"*20)
print(json.dumps(users, indent=2, default=str))

login = False
current_user = None
while True:
    username = input("아이디를 입력하세요 :")

    if username in users:
        while True:
             
            password = input("패스워드를 입력하세요:")

            if password == users[username]["password"]:
                print("Login successful!")
                print(f"---{username} Profile---")
                print(f"ID : {users[username]["id"]}")
                print(f"Acess LV : {users[username]["role"]}")
                print("")
                current_user = username
                login = True
                break

            else:
                 print("!비밀번호가 틀렸습니다!")
        if login:
             break
             
    else:
         print("!아이디가 없습니다!")

         new_users = input("새 유저이신가요? (Y/N) :")

         if new_users.lower() == "y":
            new_users_name = input("이름을 적어주세요 ex)홍길동 :")
            while True:
                new_users_bdate = input("생년월일을 적어주세요 ex)991010 :")
                if len(new_users_bdate) == 6:
                        if 0 < int(new_users_bdate[2:4]) < 13:
                            if 0 < int(new_users_bdate[4:6]) < 31:
                                  break
                            else:
                              print("!올바르지 않은 일 값!")
                        else:
                             print("!올바르지 않은 월 값!")
                else:
                     print("!형식에 맞게 작성해주세요!")
            while True:
                new_users_ID = input("ID를 적어주세요 :")
                if not new_users_ID in users:
                     break
                else:
                     print("!중복된 ID 입니다!")
            while True:
                    new_users_password = input("비밀번호를 적어주세요 *8글자 이상 :")
                    if len(new_users_password)< 8:
                        print("!비밀번호를 8글자 이상 작성해주세요!")
                    else:
                         break
            users.update({new_users_ID : {
                "name" : new_users_name,
                "birthdate" : new_users_bdate,
                "id" : new_users_ID,
                "password" : new_users_password,
                "role" : Role.VIEWER
                }})
            current_user = new_users_ID
            login = True
            if login:
                 break
         else:
              continue
         print("New users login successful!")
         print(f"---{new_users_ID} Profile---")
         print(f"Name : {users[new_users_ID]["name"]}")
         print(f"Birthdate : {users[new_users_ID]["birthdate"]}")
         print(f"ID : {users[new_users_ID]["id"]}")
         print(f"Password : {users[new_users_ID]["password"]}")
         print(f"role : {users[new_users_ID]["role"]}")
print("-"*20 + "User LIST" + "-"*20)
print(json.dumps(users, indent=2, default=str))
print("")

            
while True:
    print("원하시는 작업을 선택하세요")
    action = input("프로필 수정(1) 프로필 삭제(2)")
    if action== "1":
        if users[current_user]["role"] == (Role.ADMIN and Role.EDITOR):
             users_1 = input("수정할 프로필 아이디를 입력하세요 :")
             if not users_1 in users:
                  print("!해당 아이디가 없습니다!")
                  continue
             else:
                  users_1_1 = input("수정할 항목을 작성해주세요")
                  users_1_2 = input("수정할 내용을 작성해주세요")
                  if users_1_1 == "role":
                       print("역할은 바꿀수 없습니다")
                       continue
                  else:
                       users[users_1][users_1_1] = users_1_2
                       break

        else:
             users_1_3 = input("수정할 항목을 작성해주세요")
             users_1_4 = input("수정할 내용을 작성해주세요")
             if users_1_3 == "role":
                print("역할은 바꿀수 없습니다")
                continue
             else:
                  users[current_user][users_1_3] = users_1_4
                  break

    elif action == "2":
         if users[current_user]["role"] == (Role.ADMIN):
             users_2 = input("삭제할 프로필 아이디를 입력하세요 :")
             if users_2 in users:  
                 del users[users_2]
                 break
             else:
                  print("해당 프로필은 없습니다.")
                  continue

         else:
              users_2_1 = input("삭제하시겠습니까? (Y/N)")
              if users_2_1.lower() == "y":
                   del users[current_user]
                   break
              else:
                   continue
print("-"*20 + "User LIST" + "-"*20)
print(json.dumps(users, indent=2, default=str))
print("")