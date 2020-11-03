from database import connect

class User:
    def __init__(self, email, first_name, last_name, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        return f"<User {self.email}>"
        
        # print the object for people
        # print(user)
        # >> <User dave@sliame.com>

    def save_to_db(self):
        with connect() as connection: # fetches the return value and using it as connection
                # Indenting the below content stops me from forgetting to commit
            with connection.cursor() as cursor:
                # with opens and closes, like files
                    cursor.execute('INSERT INTO users (email, first_name, last_name) VALUES (%s, %s, %s)',
                                (self.email, self.first_name, self.last_name))
                                # Similar to string interpolation
        
        # OLD VERSION OF DOING THINGS

        # with connection.cursor() as cursor:
        #     # with opens and closes, like files
        #     cursor.execute('INSERT INTO users (email, first_name, last_name) VALUES (%s, %s, %s)',
        #                   (self.email, self.first_name, self.last_name))
        #                   # Similar to string interpolation
        # connection.commit()
        # connection.close()

    @classmethod
    def load_from_db_by_email(cls, email):
        with connect() as connection: # fetches the return value and using it as connection
                # Indenting the below content stops me from forgetting to commit
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM users WHERE email=%s', (email,)) # we have to pretend that this is a tuple using ','
                user_data = cursor.fetchone() # Basically asking it to get the first row from the table database.
                return cls(email=user_data[1], first_name=user_data[2], last_name=user_data[3], id=user_data[0])
                # last line is returning a new User object and using the data to pass params. The order is dictated
                # by the order of the columns inside postgresql, but we're naming them just to make sure.