from fastapi import APIRouter, HTTPException
from app.schemas import Shorten_url, Original_url, Url
from urllib.parse import urlparse
import string
import random

router = APIRouter()

urls_db = {}

def is_valid_url(url: str) -> bool:
    parsed_url = urlparse(url)
    return parsed_url.scheme in {"http", "https"} and bool(parsed_url.netloc)

def generate_short_code(length=6):
    """Generate a random short code of given length."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

@router.post("/shorten", response_model=Shorten_url)
def shorten_url(url: str):
    if is_valid_url(url):

