# Path issue handled
import sys
from os.path import dirname, abspath

# Add the 'backend' directory to the sys.path
sys.path.insert(0, dirname(abspath(__file__)))


from fastapi import FastAPI
from fastapi import APIRouter
import uvicorn
from api.api import app
import logging
from router.router import router_instance



if __name__ == "__main__":
    logging.info("Uvicorn server execution started.")
    uvicorn.run(app)