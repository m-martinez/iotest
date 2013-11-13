
Installation
============

::
  virtualenv ./env
  cd ./env
  source bin/activate
  git clone git@github.com:m-martinez/iotest.git
  git clone git@github.com:abourget/gevent-socketio.git
  pip install -e ./gevent-socketio
  pip install -e ./iotest
  pserve --reload iotest/development.ini

