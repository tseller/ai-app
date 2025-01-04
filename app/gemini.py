import vertexai
from vertexai.generative_models import GenerativeModel
from floggit import flog

PROJECT_ID = "learned-grammar-426001-g1"
vertexai.init(project=PROJECT_ID, location="us-west1")

model = GenerativeModel("gemini-1.5-flash-002")
@flog
def generate_content(prompt):
    response = model.generate_content(prompt)
    return response.text
