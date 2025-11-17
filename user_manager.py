class UserManager:
    def __init__(self):
        self.users = []
    
    def add_user(self, name, email):
        user = {"name": name, "email": email}
        self.users.append(user)
    
    def find_user(self, email):
        for user in self.users:
            if user["email"] == email:
                return user
        return None
    
    def delete_user(self, email):
        for i, user in enumerate(self.users):
            if user["email"] == email:
                del self.users[i]
                return True
        return False

def validate_email(email):
    if "@" not in email:
        return False
    return True

def create_user_profile(name, email, age=None):
    profile = {
        "name": name,
        "email": email,
        "age": age
    }
    return profile
