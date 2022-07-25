from os import getenv
from dotenv import load_dotenv

load_dotenv()

params = {
    'host': getenv('DB_HOST', '3.130.126.210'),
    'port': int(getenv('DB_PORT', 3309)),
    'user': getenv('DB_USER', 'pruebas'),
    'password': getenv('DB_PASSWORD', 'VGbt3Day5R'),
    'db': getenv('DB_NAME', 'habi_db'),
    'charset': 'utf8mb4',
}