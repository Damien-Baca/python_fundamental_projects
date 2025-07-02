from datetime import datetime
from sys import stderr


def log_error(message):
    with open("err.log", "a") as fp:
        now = datetime.now()
        message = f"[{now}] Error - " + message
        fp.write(message)
        print(message, file=stderr)
