# class Users:

#     def __init__(self, username, email, password):
#         self.username = username       # _ => private      __ => more private
#         self.__email = email
#         self.password = password

#     def say_hi(self, user):
#         print(f"Hi {user.username}, I am {self.username}")

#     def get_email(self):
#        print("email accessed")
#        return self.__email

#     def set_email(self, new_email):
#        self.__email = new_email

#     def clean_email(self):
#         return self.__email.lower().strip()

# user1 = Users("ali", "ali@gmail.com", 123)
# user2 = Users("Jana", "jana@gmail.com", "abc")

# # user1.say_hi(user2)

# # print(user1.email)   error
# # print(user1.password)  error

# user1.set_email("  NAda@gmail.com ")
# print(user1.clean_email())
# print(user1.get_email())

# print(user1._email)
#------------------------------------------------

# class User :
#     def __init__ (self,email):
#         self._email=email
#     @property                      #decorator
#     def get_email (self):
#         return self._email
    
# user1= User("nada@gmail.com")
# print(user1.get_email)               # attribute بتعامل مع الميثود ك 

#------------------------------------------------

class User:

    counter=0
    def __init__(self,username,email):
        self.username=username
        self.email=email
        User.counter +=1

user1=User("ali","ali@gmail.com")  
user2=User("ali","ali@gmail.com") 
user3=User("ali","ali@gmail.com") 
user4=User("ali","ali@gmail.com") 
print(User.counter)  

