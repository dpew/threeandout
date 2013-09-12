'use strict';

/* Services */

angular.module('taoServices', ['ngResource']).
    factory('FantasyPlayer', function($resource){

  return $resource('rest/fplayer/:Id', {}, {
    query: {method:'GET', params:{Id:'@Id'}, isArray:true}
  });

});
