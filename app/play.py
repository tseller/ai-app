from floggit import flog

@flog
def main(comments: str):
    return {
        'board': 'Testing one two three testing!'
    }
