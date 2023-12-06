from web_frame import get, post
import re, time, json, logging, hashlib, base64, asyncio
from model_develop import User, Comment, Blog, next_id


@get('/')
async def index(request):
    users = await User.findAll()
    return {
    '__template__':'text.html',
    'users':users
    }

