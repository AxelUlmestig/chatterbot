var app = angular.module('botApp', []);
app.controller('chatController', function($scope, $http) {
	$scope.history = ["Bot: Chat with me!"]
	$scope.message = ""	
	$scope.tell_bot = function(message) {
		if(!message) {
			return	
		}
		$scope.history.push("You: " + message)
		$scope.message = ""
		$http({
			    method: 'POST',
			    url: '/api/tell',
			    data: "statement=" + encodeURIComponent(message),
			    headers: {'Content-Type': 'application/x-www-form-urlencoded'}
		})
		.then(function(response){
			bot_response = "Bot: " + response.data
			$scope.history.push(bot_response)		
		})
	}
});
