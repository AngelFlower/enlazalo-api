import bcrypt

def hash_password(password: str) -> str:
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')

def verify_password(hashed_password: str, input_password: str) -> bool:
    try:
        hashed_password_bytes = hashed_password.encode('utf-8')
        input_password_bytes = input_password.encode('utf-8')
        return bcrypt.checkpw(input_password_bytes, hashed_password_bytes)
    except ValueError:
        raise ValueError("Invalid password hash format")
