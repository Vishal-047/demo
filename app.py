import os

def login_user(username, password):
    # SafeLane hates hardcoded secrets!
    admin_password = "supersecretpassword123"
    
    if password == admin_password:
        print("Admin login successful!")
        
        # SafeLane considers eval() extremely dangerous!
        eval(f"print('Welcome {username}')")
        return True
        
    return False

def process_data(data):
    try:
        result = int(data)
    except Exception:
        # SafeLane hates when you silently ignore errors!
        pass
