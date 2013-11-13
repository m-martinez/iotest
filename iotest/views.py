import itertools

from pyramid.view import view_config
from pyramid.response import Response
from socketio import socketio_manage
from socketio.namespace import BaseNamespace

from iotest import redis


@view_config(route_name='home', renderer='templates/home.pt')
def home(request):
    return {}


@view_config(route_name='other', renderer='templates/other.pt')
def other(request):
    return {}


@view_config(route_name='socketio')
def socketio(request):
    socketio_manage(request.environ, {
        '/test': TestNamespace
        }, request)
    return Response()


class TestNamespace(BaseNamespace):

    def initialize(self):
        self.spawn(self.emitter)

    def emitter(self):
        client = redis.pubsub()
        client.subscribe('anything')
        for broadcast in client.listen():
            if broadcast['type'] != 'message':
                continue

