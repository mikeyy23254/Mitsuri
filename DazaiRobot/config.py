class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 21908050
    API_HASH = "6370a6ef27707a19da37962574a4571e"

    CASH_API_KEY = "O143RMB0LZFPQ8F4"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgresql+asyncpg://neondb_owner:npg_XbwV4SzKFn7G@ep-steep-feather-a8wgninx-pooler.eastus2.azure.neon.tech/neondb"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1002630535576)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://Lelouch:Lelouch123@cluster0.vmf8l.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/ad2b38da713ceb2f6085b.jpg"

    SUPPORT_CHAT = "radhasprt"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "7066286653:AAGIDbC858PktjIiCDtJf0Q_AX22uUyOiGw"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "NRT8UF84PEJS"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 5106602523  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [1737646273]  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
