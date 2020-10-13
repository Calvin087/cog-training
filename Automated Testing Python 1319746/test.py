import functools

user = {"username" : "Cally", "access_level": "guest"}

def make_secure(access_level):
    # FACTORY used to create decorators
    
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"no {access_level} access for {user['username']}"
        
        return secure_function

    return decorator

@make_secure("admin")
def my_pass():
    return "1234"

@make_secure("guest")
def get_dashboard_password():
    return "user: user_password"

print(my_pass())
print(get_dashboard_password())

# >> no admin access for Cally
# >> user: user_password

user = {"username" : "Dave", "access_level": "admin"}

print(my_pass())
print(get_dashboard_password())

# >> 1234
# >> no guest access for Dave