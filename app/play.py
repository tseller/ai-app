from floggit import flog
from schemas import Play

@flog
def main(play: Play):
    return {
        'board': play.play
    }