class UserData():
    def __init__(self, name,psw,fname,lname,phone,userId=-1):
        self.userId = userId
        self.userName = name
        self.password = psw
        self.firstName = fname
        self.lastName = lname
        self.phoneNumber = phone
        
    # Default object to string conversion
    def __str__(self):
        return f"""
                UserId = {self.userId}
                UserName = {self.userName}
                FirstName = {self.firstName}
                LastName = {self.lastName}
                PhoneNumber = {self.phoneNumber}
            """
        