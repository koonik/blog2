var blogApp = angular.module('blogApp', ['ngRoute', 'PostServices', 'TagServices', 'CommentServices', 'UserServices', 'ngCookies','http-auth-interceptor'] ,function ($interpolateProvider) {
        $interpolateProvider.startSymbol("{[{");
        $interpolateProvider.endSymbol("}]}");
    });

blogApp.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});

blogApp.run(function ($http, $cookies) {
    $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
});


blogApp.directive('login', function($http, $cookieStore, authService){
    return {
        restrict: 'A',
        link: function ($scope, elem, attrs) {

          elem.bind('submit', function () {
            var user_data = {
                  "username": $scope.username,
                  "password": $scope.password
            };

            $http.post('/api-auth/login/', user_data, {"Authorization": ""})
                .success(function(response) {
                    $cookieStore.put('djangotoken', response.token);
                    $http.defaults.headers.common['Authorization'] = 'Token ' + response.token;
                    authService.loginConfirmed();
                });
          });
        }
    }
 });

blogApp.directive('authApplication', function ($cookieStore, $http) {
    return {
        restrict: 'A',
        link: function ($scope, elem, attrs) {

          $scope.$on('event:initial-auth', function () {
             if ($cookieStore.get('djangotoken')) {
               $http.defaults.headers.common['Authorization'] = 'Token ' + $cookieStore.get('djangotoken');
             }

          });
          $scope.$on('event:auth-loginConfirmed', function(){
              $scope.user_is_active = true;
          })
        }
     }
  });

blogApp.config(function($routeProvider) {
		$routeProvider

			.when('/', {
				templateUrl : '/templates/home.html',
				controller  : 'mainController'
			})

			.when('/detail/:id', {
				templateUrl : '/templates/detail.html',
				controller  : 'detailController'

			})

            .when('/create/', {
				templateUrl : '/templates/create.html',
				controller  : 'mainController'

			})

            .when('/edit/:id', {
				templateUrl : '/templates/edit.html',
				controller  : 'detailController'

			});
	});



blogApp.controller('mainController', function($scope, $routeParams, Post, Tag, Comment, $location){
    var posts = $scope.posts = Post.query();
    $scope.newTitle = '';
    $scope.newBody = '';
    var tags = $scope.tags = Tag.query();
    var chosenTags= $scope.chosenTags = [];



    $scope.addPost = function(){
        var tempTags = [];
        for (var i=0; i < $scope.chosenTags.length; i++){
            tempTags.push($scope.chosenTags[i].id);
        }
        var newPost = new Post({title: $scope.newTitle, body: $scope.newBody, tag: tempTags});
        newPost.$save().then(function(){
        posts = $scope.posts = Post.query();
        $location.path('/');
        });

        $scope.newTitle = '';
        $scope.newBody = '';
    };


});

blogApp.controller('detailController', function($scope, $location, $routeParams, Post, Tag, Comment, User){

    var id = $routeParams.id;
    var post = $scope.post = Post.get({id: id});
    $scope.editedPost = null;
    $scope.newTitle = '';
    $scope.newBody = '';
    var tags = $scope.tags = Tag.query();
    var chosenTags= $scope.chosenTags = [];
    var comments = $scope.comments = Comment.query();
    var commentAuthor = $scope.commentAuthor = '';
    var commentBody = $scope.commentBody = '';
    var users =$scope.users = User.query();



    $scope.editPost = function(post) {
        $scope.editedPost = post;
        $scope.originalPost = angular.extend({}, post);
    };

    $scope.doneEditing = function(post) {
        $id=post.id;
        Post.update({id:$id}, post);
        $scope.editedPost = null;
        $location.path('/detail/'+ post.id.toString())

    };

    $scope.addComment = function(){

        var newComment = new Comment({author: $scope.commentAuthor, body: $scope.commentBody, post: id});
        newComment.$save().then(function(){
        comments = $scope.comments = Comment.query();
        $location.path('/detail/'+ post.id.toString());
        commentAuthor = $scope.commentAuthor = '';
        commentBody = $scope.commentBody = '';
        });
    };

});