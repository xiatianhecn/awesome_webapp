' url handlers '

import re, time, json, logging, hashlib, base64, asyncio

from web_frame import get, post

from model_develop import User, Comment, Blog, next_id

@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }