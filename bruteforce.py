import hashlib
import itertools

charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

target_hash = "6ebe76c9fb411be97b3b0d48b791a7c9"

def brute_force(charset, length):
    for password in itertools.product(charset, repeat=length):
        password_str = ''.join(password)
        
        # Calculate MD5 hash of the current password
        hashed_password = hashlib.md5(password_str.encode()).hexdigest()
        
        if hashed_password == target_hash:
            return password_str
    return None

password_length = 6
password = brute_force(charset, password_length)

if password:
    print(f"Password found: {password}")
else:
    print("Password not found")
