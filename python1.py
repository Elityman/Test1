# hello world
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:24:04 2020

@author: wmy
"""

import pickle as p

class person:
    notes={}
    def add(self):
        name=input('Please enter a name of contactor that you want to add: ')
        if name in person.notes:
            print ('the contactor is aready exist!')
        else:
            telephone=input('Please enter the tele of contactor: ')
            addr=input('Please enter the addr of contactor: ')
            label={'telephone':telephone,'address':addr}
            person.notes[name]=label
    def dele(self):
        name=input('Please enter a name of contactor that you want to dele: ')
        if name in person.notes:
            del person.notes[name]
            print("%s" % person.notes.items())
        else:
            print ('the contactor %s is not exist!' %name)
    def search(self):
        name=input('Please enter a name of contactor that you want to search: ')
        if name in person.notes:
            print('the contactor %s telephone is %s , address is %s '%(name,person.notes[name]['telephone'],person.notes[name]['address']))
        else:
            print ('the contactor %s is not exist!' %name)
    def modify(self):
        name=input('Please enter a name of contactor that you want to modify: ')
        if name in person.notes:
            telephone=input('Please enter the tele of contactor: ')
            addr=input('Please enter the addr of contactor: ')
            label={'telephone':telephone,'address':addr}
            person.notes[name]=label
        else:
            print ('the contactor %s is not exist! if you want edit, please choice!' %name)
    def write(self):
       f = open('add_book.txt','wb+')
       p.dump(person.notes,f)
       f.close()
    def read(self):
      file = 'add_book.txt'
      try:
        f = open(file ,'rb+')
        person.notes = p.load(f)
        f.close()
      except:
        f = open(file ,'w')
        f.close()
    def show(self):
      print(person.notes)
      
def menu():
    print('''系统提供以下功能
    1：添加
    2：删除
    3：修改
    4：搜索
    5：退出
    6: 显示全部联系人信息''')
people = person()
people.read()
while True:
  try:
    menu()
    choice = int(input('Please enter the corresponding number operation: '))
    if choice==1:
        people.add()
    elif choice ==2:
        people.dele()
    elif choice ==3:
        people.modify()
    elif choice ==4:
        people.search()
    elif choice ==5:
        people.write()
        break
    elif choice==6:
        people.show()
    else:
        print('Invalid input,Please enter the corresponding number operation: ')
  except ValueError:
      print('Please enter numeric options: ')
