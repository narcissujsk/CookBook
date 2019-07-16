import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('test')
log.info("i")
from routes import Mapper

map = Mapper()  # 生成的是 Mapper()实例对象
print (map)
print (type(map))

map.connect('lixin', '/blog', controller='main', action='index')

result = map.match('/blog')

print (result)

map2 = Mapper()
map2.connect(None, '/error/{action}/{id}', controller='error')
result2 = map2.match('/error/ddd/200')
print(result2)

map2.connect(None, '/error/{action:index|lixin}/{id:\d+}', controller='error')
result3 = map2.match('/error/lixin/200')
print(result3)

map3 = Mapper()
map3.connect('/user/list', controller = 'user', action = 'list', conditions={'method' : ['GET', 'HEAD']})
result = map3.match('/user/list')
print(result)

if __name__ == "__main__":
    log.info("yy")