import os

# TEST CASE 1: Hardcoded High-Risk Secrets
AWS_SECRET_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLEKEY12345"
DATABASE_PASSWORD = "SuperSecretPassword2026!"

def authenticate_user(username, secret_input):
    # TEST CASE 2: Insecure string evaluation
    command = f"verify('{username}', '{secret_input}')"
    eval(command)

def process_user_input(raw_data):
    try:
        # TEST CASE 3: Swallowed exceptions
        exec(raw_data)
    except Exception:
        pass

