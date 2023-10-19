from passlib.context import CryptContext


pwd_context = CryptContext(schemes = ["bcrypt"], deprecated="auto" )

# an improvement to user authentication. Hashing both the user name and password should be possible. 
# def hash(username: str, password: str)
    #return pwd_context.hash(username, password)


def hash(password: str):
    return pwd_context.hash(password)

def verify(plain_password, harshed_password):
    return pwd_context.verify(plain_password, harshed_password)