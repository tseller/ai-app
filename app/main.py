from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from floggit import flog

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get('/')
@flog
def play(commands: str):
    return {
        'foo': 'bar'
    }
