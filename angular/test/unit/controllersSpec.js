'use strict';

/* jasmine specs for controllers go here */
describe('FantasyPlayer controllers', function() {

  beforeEach(function(){
    this.addMatchers({
      toEqualData: function(expected) {
        return angular.equals(this.actual, expected);
      }
    });
  });


  beforeEach(module('taoServices'));


  describe('FantasyPlayerListCtrl', function(){
    var scope, ctrl, $httpBackend;

    beforeEach(inject(function(_$httpBackend_, $rootScope, $controller) {
      $httpBackend = _$httpBackend_;
      $httpBackend.expectGET('../../../rest/fplayers').
          respond([{"id": 1, "user": 2, "teamname": "whatever", "email": "foo.bar@gmail.com", "league": 0}]);

      scope = $rootScope.$new();
      ctrl = $controller(FantasyPlayerListCtrl, {$scope: scope});
    }));


    it('should create "fantasy player" model with 1 fantasy player fetched from xhr', function() {
      expect(scope.players).toEqual([]);
      $httpBackend.flush();

      expect(scope.players).toEqualData(
          [{"id": 1, "user": 2, "teamname": "whatever", "email": "foo.bar@gmail.com", "league": 0}]);
    });


  });


  describe('FantasyPlayerDetailCtrl', function(){
    var scope, $httpBackend, ctrl,
        xyzPhoneData = function() {
          return {
              "id": 1,
              "user": 2,
              "teamname": "whatever",
	       "email": "foo.bar@gmail.com",
               "league": 0
          }
        };


    beforeEach(inject(function(_$httpBackend_, $rootScope, $routeParams, $controller) {
      $httpBackend = _$httpBackend_;
      $httpBackend.expectGET('../../../rest/fplayers/1').respond(xyzPhoneData());

      $routeParams.Id = '1';
      scope = $rootScope.$new();
      ctrl = $controller(FantasyPlayerDetailCtrl, {$scope: scope});
    }));


    it('should fetch fantasy player detail', function() {
      expect(scope.player).toEqualData({});
      $httpBackend.flush();

      expect(scope.player).toEqualData(xyzPhoneData());
    });
  });
});
