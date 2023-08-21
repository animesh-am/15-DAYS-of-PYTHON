class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def get_username(self):
        return self.__username

    def set_username(self, new_username):
        self.__username = new_username

    def display_info(self):
        print(f"Username: {self.__username}")
        print("Password: ********")  # Sensitive information is not displayed


user = User("john_doe", "securepassword")

print("Original User Info:")
user.display_info()
user.set_username("new_username")

print("\nUpdated User Info:")
user.display_info()
