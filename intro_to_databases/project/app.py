from user import User


# This uses the method on user to connect and send data to Postgresql
# user = User("dave@sliame.com", "dave", "torra", None)
# user.save_to_db()

# user1 = User("sammy@sliame.com", "sam", "slam", None)
# user1.save_to_db()

# --------------

# user = User.load_from_db_by_email('dave@sliame.com')
# print(user)
# <User dave@sliame.com>

# --------------

cusomter2 = User("chill@sliame.com", "chill", "shill", None)
cusomter2.save_to_db()
user_from_db = User.load_from_db_by_email('chill@sliame.com')

print(user_from_db)


