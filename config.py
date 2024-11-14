import re
from os import getenv
# ------------------------------------
# ------------------------------------
from dotenv import load_dotenv
from pyrogram import filters
# ------------------------------------
# ------------------------------------
load_dotenv()
# ------------------------------------
# -----------------------------------------------------
API_ID = int(getenv("API_ID", "24175365"))
API_HASH = getenv("API_HASH", "6c671b52c2acbc665e239c006ed890a2")
# ------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", "7317529707:AAFzgy65_HvGlkXyxUpNRd9dj6eobRQJrAg")
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","@Cute_girl_ll")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME" , "MUSIC_SAKSHI_BOT")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME" , "🌸𝆺𝅥⃝🦋 ⃪ͥ͢ ᷟ•× 𝐒𝐀𝐊𝐒𝐇𝐈 °‌❤️‍🩹✘ᴅ 🕊")
# ---------------------------------------------------------
ASSUSERNAME = getenv("ASSUSERNAME" , "🌸𝆺𝅥⃝🦋 ⃪ͥ͢ ᷟ•× 𝐒𝐀𝐊𝐒𝐇𝐈 °‌❤️‍🩹✘ᴅ 🕊")

API_KEY = "abc921ff654bcf7b3faff8f775d781d8d27d32bfd02d6692eea30249ba781c8b"  # अपना API key यहाँ डालें
# ---------------------------------------------------------


#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://gefigo2922:gefigo2922@music990.29azj.mongodb.net/?retryWrites=true&w=majority&appName=Music990")
#---------------------------------------------------------------
#---------------------------------------------------------------

# ----------------------------------------------------------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# ----------------------------------------------------------------

# ----------------------------------------------------------------
LOGGER_ID = int(getenv("LOGGER_ID", "-1002188495981"))
# ----------------------------------------------------------------
# ----------------------------------------------------------------
OWNER_ID = int(getenv("OWNER_ID", "7423400816"))
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# config.py
OPENAI_API_KEY = 'sk-svcacct-P6WzUuDoe32FfmEZAPYHvXxym4gRpzFDJj8R3LTWvZ1bPQaDLNr0cP9bWinT3BlbkFJf2zLaAxMRLSfocVQkLP0ksWaJPVl4SwHwCEFT_mvnbIujjvt0_cqmjh7gCwA'
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# ----------------------------------------------------------------
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/SK-KING/DJ-MUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # ----------------------------------------------------------------
# -------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------



# ------------------------------------------------------------------------
# -------------------------------------------------------------------------
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/SAKSHI_UPDATES")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/SAKSHI_SUPPORT")
SOURCE = getenv("SOURCE", "https://github.com/SK-KING/DJ-MUSIC")
CHAT = getenv("CHAT", "https://t.me/tg_friends_hub")
# ------------------------------------------------------------------------------
# -------------------------------------------------------------------------------







# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
# ----------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
# --------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------
STRING1 = getenv("STRING_SESSION", "BACZzqEAkjb-fflnfCheX-ZNHgwWnrkHh5QSYVPwmCRdka2GX8XWBp9CDjQacJSVN1VS9w00bJ7XoScBOlhmgKZOdGtsRYEjXt22EDQhCfJrL5icd81tK4C3gLfuaft5N0_25pmHJgyeOArk_Z_eL74RpWE0nTLyx3Ax2KnPepYwwrH5PzaTPJkn8KilIlsOtqmTXz_MTzwKEneGOVLltHcobLePzzTFM5dPKM9hnUNVV-W9zNmVYb2gWWsd-SdrVIihajMxStBSsn_9_pRwmpAvsMkMiYiyp72u45_WbIuYoXvIvLUgvtT-W2Wy5yyYd66wMxmUo8BzkETg9SjuXbaiOa6TWwAAAAHIEVb0AA")
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/xhpqtp.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/fd827f9a4fe8eaa3e8bf4.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
STATS_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/c832e84cd991c865c7e4f.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/e575ae40d6635250974e1.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/03efec694e41e891b29dc.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/4dc854f961cd3ce46899b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
# ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
