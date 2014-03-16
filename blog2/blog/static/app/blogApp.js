var blogApp = angular.module('blogApp', ['ngRoute', 'PostServices', 'TagServices'] ,function ($interpolateProvider) {
        $interpolateProvider.startSymbol("{[{");
        $interpolateProvider.endSymbol("}]}");
    });

blogApp.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});

blogApp.config(function($routeProvider) {
		$routeProvider

			// route for the home page
			.when('/', {
				templateUrl : '/templates/home.html',
				controller  : 'mainController'
			})

			// route for the about page
			.when('/detail/:id', {
				templateUrl : '/templates/detail.html',
				controller  : 'detailController',

			});
	});


blogApp.controller('mainController', function($scope, $routeParams, Post, Tag){
    var posts = $scope.posts = Post.query();




});

blogApp.controller('detailController', function($scope, $routeParams, Post, Tag){
    var $id = $routeParams.id;

    var post = $scope.post = Post.get({id: $id});






});