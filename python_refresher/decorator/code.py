"""to practice decorators """
from typing import Callable
import functools

user = {"user_name": "Farhad",
        "access_level": "guest"}


def make_secure(func: Callable) -> Callable:
    """secure the func """

    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        return f"No admin access available for {user['user_name']}."
    return secure_function


@make_secure
def get_admin_password(panel:str) -> str:
    """get the password from the admin"""
    if panel == "admin":
        return "12345"
    if panel == "billing":
        return "super secure password"
    return "not authorized panel"


print(get_admin_password("billing"))

print(get_admin_password.__name__)

print(get_admin_password.__doc__)
