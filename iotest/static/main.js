+function($) {
  'use strict';

  $(document).ready(function(){

    var socket = io.connect('/test')

    socket.on('connect', function(){

      socket.on('count', function(msg){
        $('#output').prop('value', msg);
      });

      $(window).on('beforeunload', function(){
        socket.disconnect();
      });

    });

  });

}(jQuery);


