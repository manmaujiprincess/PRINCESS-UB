import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "26934847")) #optional
API_HASH = getenv("API_HASH", "c7b83025a9e28ff15e90c47cd5f78409") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5647701277").split()))
OWNER_ID = int(getenv("OWNER_ID", "5647701277"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Zaid:Princess@cluster0.mblh2hz.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5894087865:AAFNkWVMD9KO9ujYdKtsB3bla1eeDeeEjB8")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkAgIn_apkE75O5nZ2-BU7eMYSVE3ZX2vNACFNZ9PRTkDgfD5JVfEnuqXazvVqx6ddaLyz4o42WrIyPkfDg0QluzCWRFhgZZzGrqnxMlTbNppfcPHV4cwzA2M0KOqHeFFQ_2vgFfpkRk-_NTZf_3SI6y9spdVS0UjQcnKP3EKy9JYTQg6XsuiaaeCJKTHOCKg2q2GKH3GtQTOmL_uUsPHFRh7x30AHPFLOiyH5EWaTZzQpRTki-3c310UYtwm0E3992H9H8fyzHioJzvuuaCzH1Nq7-PW1w1tnNpLaHgYibIsFPZ_UKTLudEQYAR3POks-AEdGV-iniUTK9YGWWZhMXVgAAAAFQoRUdAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
