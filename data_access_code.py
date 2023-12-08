import orm_test
from model_develop import User, Blog, Comment

def test():
    yield from orm_test.create_pool(user='www-data', password='www-data', db='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()

for x in test():
    pass