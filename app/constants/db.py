from os import getenv
from dotenv import load_dotenv

load_dotenv()

params = {
    'host': getenv('DB_HOST'),
    'port': int(getenv('DB_PORT')),
    'user': getenv('DB_USER'),
    'password': getenv('DB_PASSWORD'),
    'db': getenv('DB_NAME'),
    'charset': 'utf8mb4',
}