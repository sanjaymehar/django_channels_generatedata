from django.urls import path
from .consumer import*

ws_patterns = [
    path("ws/test/",GenerateName.as_asgi()),
]
