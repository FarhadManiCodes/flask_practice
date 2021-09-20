"""to practice decorators """
from typing import Callable
import functools


def make_secure(access_level:str) -> Callable:
    """secure decorator"""
    def decorators(func: Callable) -> Callable:
        """secure the func """
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            return f"No {access_level} access available for {user['user_name']}."
        return secure_function
    return decorators    


@make_secure("admin")
def get_admin_password(panel:str) -> str:
    """get the password from the admin"""
    if panel == "admin":
        return "12345"
    if panel == "billing":
        return "super secure password"
    return "not authorized panel"


@make_secure("user")
def get_dashboard_password():
    return "user: user_password"


user = {"user_name": "Farhad", "access_level": "admin"}
print(get_dashboard_password())
print(get_admin_password("billing"))