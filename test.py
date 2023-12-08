import asyncio
import orm_test
from model_develop import User


async def test(loop):
    await orm_test.create_pool(user='root', password='password', db='awesome', loop=loop)
    u = User(name='Test', email='test@example.com', password='1234567890', image='abut:blank')
    await u.save()


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))