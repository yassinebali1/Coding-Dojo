from mysqlconnection import connectToMySQL 
class Users: 
    def __init__(self,data): 
        self.first_name=data["first_name"]
        self.last_name=data["last_name"]
        self.email=data["email"]

    @classmethod
    def get_all(cls):
        req= "select * from users;"
        reselt=connectToMySQL('user').query_db(req)
        list_users=[]
        for users in reselt:
            list_users.append(cls(users))

        print(list_users)
        return list_users
    @classmethod
    def create_users(cls,data):
        req="insert into users(first_name,last_name,email) values (%(first_name)s,%(last_name)s,%(email)s);"
        result=connectToMySQL('user').query_db(req,data)
        return result


        
        