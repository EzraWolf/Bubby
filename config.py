
import os
import dotenv

dotenv.load_dotenv()

TOKEN: str = os.getenv('TOKEN')
BOT_ID: int = os.getenv('BOT_ID')
PREFIX: str = os.getenv('PREFIX')
OWNER_ID: int = os.getenv('OWNER_ID')
ADMIN_IDS: str = os.getenv('ADMIN_IDS')
SHARD_CT: int = os.getenv('SHARD_CT')
ALL_INTENTS: bool = os.getenv('ALL_INTENTS')
LOGGING: bool = os.getenv('LOGGING')
LOG_VIGOR: int = os.getenv('LOG_VIGOR')

# Require a min of 1.5s delay between commands
MSG_TIMEOUT: int = 1.5 * 1000

# Neural network settings
NN_HIDDEN_CELL_CT: int = 512
NN_HIDDEN_LAYER_CT: int = 50

# List of paths that contain the bots commands
COG_PATHS: list[str] = [
    'cogs.admin',
    'cogs.economy',
    'cogs.events',
    'cogs.fun',
    'cogs.games',
    'cogs.general',
    'cogs.images',
    'cogs.music',
    'cogs.neural',
    'cogs.utility',
]

# Every 30 seconds in ms
STATUS_DELAY: int = 30 * 1000
STATUS_STATES: dict = {
    'WATCHING': [
        'you',
        'morbius',
        'paint dry',
        '9-5 workers',
        'American Psycho',
        'the british channel',
        'JS devs attempt to escape from reality',
        'Perl devs try to stay relavent',
        'Python devs enjoying the good life',
        'C++ devs explain pointers to the python devs',
        'the Github repo',
        'the CCTV cams',
    ],

    'PLAYING': [
        'you',
        'Github',
        'Bloons TD',
        'cat videos',
        'your mom',
        'therapist meeting',
        'APPLE BASIC',
        'laundry',
    ]
}
