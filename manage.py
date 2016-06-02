from flask_script import Manager
from app.app import create_app

manager = Manager(create_app)

# @manager.command
# def hello():
#     print "hello"

if __name__ == "__main__":
    manager.run()





