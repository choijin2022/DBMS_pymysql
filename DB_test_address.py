import pymysql as my

# Connect to the database(db01)
host = 'localhost'
user = 'root'
password = ''
database = 'db01'

conn = my.connect(host=host, user=user, password=password, database=database)
cur = conn.cursor(my.cursors.DictCursor)  

'''
<사용법>

1. 데이터 저장 
sql = f" query 작성 "
cur.excute(sql) # sql 실행
conn.commit() # DB에 반영

2. 데이터 조회
user1 = cur.fetchone() # 조회 결과 제일 위 데이터 하나 가져옴
print(user1)

user_list = cur.fetchall() # 조회 결과 모두 가져옴
print(user_list[0][{}]) 

'''

# 심플 주소록 만들기


print("===프로그램 시작 ===")

while(True) :
    cmd = input("1.조회 2.등록 3.수정 4.삭제 5.종료 >> ")
    if(cmd == '1') :
        sql = f"SELECT * FROM addressBook"
        cur.execute(sql)
        user_list = cur.fetchall()
        print("==================")
        if(len(user_list)==0) :
            print("저장된 주소가 없습니다.")
            continue

        for user in user_list :
            print("Id      : ",user["uNo"])
            print("name    : ",user["uname"])
            print("address : ", user["addr"])
            print("==================")
    
    elif(cmd == '2') :
        name = input("이름 입력 : ")
        addr = input("주소 입력 : ")
        
        sql = f"INSERT INTO addressBook(uname, addr,regDate) VALUES ('{name}', '{addr}', NOW())"
        cur.execute(sql)
        conn.commit()
        print("등록이 완료되었습니다.")
    
    elif(cmd == '3') :
        num = input("수정할 주소 번호 입력 : ")
        select = input("[1.이름수정, 2.주소수정, 3.All] >> ")
        if select =='1' :
            name = input("이름 입력 : ")
            sql = f"UPDATE addressBook SET uname='{name}',regDate = NOW() WHERE uNo = {num}"
        elif select =='2' :
            addr = input("주소 입력 : ")
            sql = f"UPDATE addressBook SET addr = '{addr}', regDate = NOW() WHERE uNo = {num}"
        else :
            name = input("이름 입력 : ")
            addr = input("주소 입력 : ")
            sql = f"UPDATE addressBook SET uname='{name}', addr = '{addr}', regDate = NOW() WHERE uNo = {num}"
        
        cur.execute(sql)
        conn.commit()
        print("수정이 완료되었습니다.")
    elif(cmd == '4') :
        num = input("삭제할 주소 번호 입력 : ")

        sql = f"DELETE FROM addressBook WHERE uNo = {num}"
        cur.execute(sql)
        conn.commit()
        print("삭제가 완료되었습니다.")

    elif(cmd == '5'):
        print("=== 프로그램 종료 ===")
        break
