import os


class Config:
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    RESOURCES_DIR = os.path.join(BASE_DIR, 'resources')
    NODE_MODULES_DIR = os.path.join(BASE_DIR, 'node_modules')
    SECRET_KEY = os.environ.get('SECRET_KEY')
