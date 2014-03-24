var PostServices  = angular.module('PostServices', ['ngResource']);

PostServices.factory('Post', ['$resource', function($resource){
    return $resource('/posts/:id', {}, {
        'update': { method:'PUT' }})
}]);

var TagServices  = angular.module('TagServices', ['ngResource']);

TagServices.factory('Tag', ['$resource', function($resource){
    return $resource('/tags/:id', {}, {
        'update': { method:'PUT' }})
}]);

var CommentServices  = angular.module('CommentServices', ['ngResource']);

CommentServices.factory('Comment', ['$resource', function($resource){
    return $resource('/comments/:id', {}, {
        'update': { method:'PUT' }})
}]);


var UserServices  = angular.module('UserServices', ['ngResource']);

UserServices.factory('User', ['$resource', function($resource){
    return $resource('/users/:id', {}, {
        'update': { method:'PUT' }})
}]);



