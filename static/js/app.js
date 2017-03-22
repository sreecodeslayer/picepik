var pApp = angular.module('Picepik', [],function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});
pApp.controller('MainController',['$scope', '$http', '$location', '$window',function($scope,$http,$location,$window){
  	$scope.logout = function(){
          $http({
              url: '/logout',
              method: "POST"
          }).then(function onSuccess(response) {
              if (response.data.status == true) {
                  window.location = '/'
              }
          });
  	};
    $scope.newAddress = function(){
      console.log($scope.new_address);
          $http({
              url: '/portfolio/address-book/new',
              method: "POST",
              data:JSON.stringify({'address':$scope.new_address}),
              headers:{'Content-Type':'application/json'}
          }).then(function onSuccess(response) {
              if (response.data.status == true) {
                console.log("Added new address");
              }
          });

    }

  	$scope.signupUser = function(){
  		$http({
  			url: '/signup',
  			method: 'POST',
  			data: JSON.stringify({'creds':$scope.signup}),
  			headers: {'Content-Type':'application/json'}
  		}).then(function onSuccess(response){
        console.log("Signed up");
  		});
  	}

  	$scope.loginUser = function(){
  		$http({
  			url: '/login',
  			method: 'POST',
  			data: JSON.stringify({'creds':$scope.login}),
  			headers: {'Content-Type':'application/json'}
  		}).then(function onSuccess(response){
        window.location = '/';
  		});
  	}
}]);
