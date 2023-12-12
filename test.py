import orm_test
import asyncio
from model_develop import User, Blog, Comment

async def test(loop):
    await orm_test.create_pool(loop=loop, user='root', password='password', db='awesome')
    u = User(name='Francis', email='francis@163.com', passwd='1234567890', image='about:blank')
    await u.save()
if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()