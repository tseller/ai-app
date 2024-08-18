from floggit import flog

@flog
def main(comments: str):
    return {
        'board': 'Hello World!'
    }
