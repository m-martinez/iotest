from pyramid.config import Configurator
from redis import StrictRedis

redis = StrictRedis()

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('other', '/other')
    config.add_route('socketio', '/socket.io/*remaining')
    config.scan()
    return config.make_wsgi_app()
