from HW.User import *

class Storage:
    @staticmethod
    def save(user):

        file_name = 'Users.txt'
        with open(file_name, 'r', encoding='utf-8') as new:
            lines=new.readlines()
            new_id = len(lines)+1

        with open(file_name, 'a', encoding='utf-8') as new:
            new.write("login: " + str(user.login) + "; password: " + str(user.password) + "; uniq_id: " + str(new_id) + '\n')
        Storage.save_user(user, new_id)


    @staticmethod
    def save_user(user, id):
        file = open('login'+str(id)+'.txt', 'w')
        file.write("login: " + str(user.login) + "; password: " + str(user.password) + "; uniq_id: " + str(id) + '\n')
