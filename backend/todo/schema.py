from ninja import Schema
from django.contrib.auth.models import User

class GetTaskSchema(Schema): 
    title : str
    description : str
    is_done : bool
    user : int

class PostTaskSchema(Schema):
    title : str
    description : str 