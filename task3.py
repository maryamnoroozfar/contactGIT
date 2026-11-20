def __init__(self, name: str,family: str):
    self.name = name
    self.family = family
def get_user_name(self):
    return f"{self.name} {self.family}".title()

User = type(
    "User", 
    (),
    {
        "__init__" : __init__,
        "get_user_name" :get_user_name
    }
    )


user = User("maryam", "noroozfar")
print(user.get_user_name())



# class User:
#     def __init__(self, name: str,family: str):
#         self.name = name
#         self.family = family
#     def get_user_name(self):
#         return f"{self.name} {self.family}".title()


# user = User("maryam", "noroozfar")
# print(user.get_user_name())