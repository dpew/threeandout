'use strict';

/* Controllers */

function FantasyPlayerListCtrl($scope, FantasyPlayer) {
  $scope.players = FantasyPlayer.query();
}
//FantasyPlayerListCtrl.$inject = ['$scope', 'Phone'];



function FantasyPlayerDetailCtrl($scope, $routeParams, FantasyPlayer) {
  $scope.player = FantasyPlayer.get({Id: $routeParams.Id});
}

//FantasyPlayerDetailCtrl.$inject = ['$scope', '$routeParams', 'FantasyPlayer'];
