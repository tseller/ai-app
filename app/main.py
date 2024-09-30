from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from floggit import flog
from schemas import Play
from play import main as make_play


app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get('/')
@flog
def root():
    return {
        'service': 'tic-tac-toe'
    }


@app.get('/game')
@flog
def game_route(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="game.html",
        context={}
    )


@app.post('/play')
@flog
def play_route(play: dict) -> dict:
    return make_play(Play.parse_obj(play))
