from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("7761547492:AAF8ubskMrS1fvuTBb0dO_9w_c-X8y0zmLw", "")
BOT_USERNAME = getenv("http://t.me/RUHI_X_QNR_GNG_BOT", "")
admins = {}
API_ID = int(getenv("29568441"))
API_HASH = getenv("b32ec0fb66d22da6f77d355fbace4f2a", "")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
