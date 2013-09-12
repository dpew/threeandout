'use strict';

/* App Module */

angular.module('tao', ['taoFilters', 'taoServices']).
  config(['$routeProvider', function($routeProvider) {
  $routeProvider.
      when('/fplayer', {templateUrl: 'partials/fplayer-list.html',   controller: FantasyPlayerListCtrl}).
      when('/fplayer/:Id', {templateUrl: 'partials/fplayer-detail.html', controller: FantasyPlayerDetailCtrl}).
      otherwise({redirectTo: '/fplayer'});
}]);
