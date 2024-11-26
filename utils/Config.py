import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    CONTAINER_NAME = os.getenv("CONTAINER-NAME")
    STORAGE_CONNECTION_STRING = os.getenv("STORAGE-CONNECTION-STRING")
    STORAGE_ACCOUNT_NAME = os.getenv("STORAGE-ACCOUNT-NAME")
    ENDPOINT = os.getenv("DOC-ENDPOINT")
    KEY = os.getenv("DOC-KEY")