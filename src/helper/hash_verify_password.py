from passlib.context import CryptContext


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


async def verify_password(password, hash_password):
    return pwd_context.verify(password, hash_password)


async def hashing_password(password):
    return pwd_context.hash(password)