#!/usr/bin/env python
# coding: utf-8

# # 전화번호 프로그램 만들기
# * 홍길동 010-123-4567
# * 기능1 : 연락처 추가
# * 기능2 : 연락처 전체 보기
# * 기능3 : 검색, 이름을 입력받아서 전화번호 조회
# * 기능4 : 수정, 이름을 입력받아서 전화번호 입력수정
# * 기능5 : 삭제, 이름 입력받아서 삭제
# * 기능6 : 프로그램 종료

# In[ ]:


phonebook = {'홍길동': '010-123-4567'}
command_list = ['추가', '검색', '수정', '삭제', '전체 조회', '종료']

while True:
    command = input('기능 입력: (추가, 검색, 수정, 삭제, 전체 조회, 종료)')
    if command == '추가':
        name = input('이름을 입력해주세요: ')
        if name in phonebook:
            print('이미 등록된 연락처입니다. 수정하시겠습니까?')
            second_command = input('네 / 아니오 로 입력해주세요: ')
            if second_command == '네':
                phone = input('번호를 입력해주세요: ')
                phonebook[name] = phone
            else:
                print('초기 메뉴로 돌아갑니다.')
    elif command == '검색':
        name = input('이름을 입력해주세요: ')
        if name in phonebook:
            print(name, phonebook[name])
        else:
            print('전화번호부에 없는 이름입니다.')
    elif command == '수정':
        name = input('이름을 입력해주세요: ')
        if name in phonebook:
            phone = input('번호를 입력해주세요: ')
            phonebook[name] = phone
            print(phonebook[name], '의 연락처가 ', phone, '로 수정되었습니다.')
        else:
            print('연락처에 없는 이름입니다.')
    elif command == '삭제':
        name = input('이름을 입력해주세요: ')
        if name in phonebook:
            del(phonebook[name])
            print('연락처가 삭제되었습니다.')
        else:
            print('연락처에 없는 이름입니다.')
    elif command == '전체 조회':
        print(phonebook)
    elif command not in command_list:
        print('제공되는 기능이 아닙니다.')
    elif command == '종료':
        print('프로그램을 종료합니다.')
        break


# In[ ]:




