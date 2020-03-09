# run.py

from app import manager
from flask_script import Server
import os


if __name__ == '__main__':
    PORT = int(os.environ.get("PORT", 5000))
    manager.add_command("runserver", Server(port=PORT))
    manager.run()