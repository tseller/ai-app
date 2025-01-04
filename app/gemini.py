import vertexai
from vertexai.language_models import GenerativeModel
import logging

logging.basicConfig(level=logging.INFO)
def flog(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Calling function {func.__name__} with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

PROJECT_ID = "learned-grammar-426001-g1"
vertexai.init(project=PROJECT_ID, location="us-west1")


model = GenerativeModel("gemini-1.5-flash-002")
@flog
def generate_content(prompt):
    response = model.generate_content(prompt)
    return response.text
