# This file is setting up the logger object to be used in the API

import logging

# import os
# os.makedirs("./logs", exist_ok=True)


logging.basicConfig(
    filename="./logs/api.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - '\n%(message)s\n -------------------------"
)

# You can also adjust the logging level for libraries. 
# passlib's bcrypt version probe raises a harmless warning under bcrypt 4.x
logging.getLogger("passlib").setLevel(logging.ERROR)
# watchfiles logs an INFO line on every reload change detection, which is just noise
# watchfile is the library responsible for detecting file changes and triggering reloads.
logging.getLogger("watchfiles.main").setLevel(logging.WARNING)

def get_logger(name: str = "voting_app") -> logging.Logger:
    return logging.getLogger(name) 