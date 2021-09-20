"""to practice decorators """
from typing import Callable
import functools

user = {"user_name": "Farhad",
        "access_level": "guest"}


def make_secure(func: Callable) -> Callable:
    """secure the func """

    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        return f"No admin access available for {user['user_name']}."
    return secure_function


@make_secure
def get_admin_password():
    """get the password from the admin"""
    return "12345"


print(get_admin_password())

print(get_admin_password.__name__)

print(get_admin_password.__doc__)
