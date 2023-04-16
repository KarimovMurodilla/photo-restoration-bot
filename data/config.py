from environs import Env

# используем библиотеку environs
env = Env()
env.read_env()

# Telegram Bot
BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список админов

# DB
DATABASE_URL = env.str("DATABASE_URL")

# Colorize
RAPIDAPI_KEY = env.str("RAPIDAPI_KEY")
RAPIDAPI_HOST = env.str("RAPIDAPI_HOST")
RAPIDAPI_URL = env.str("RAPIDAPI_URL")