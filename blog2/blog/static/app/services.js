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

