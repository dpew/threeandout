function BuzzController($resource) {
  this.userId = 'googlebuzz';
  this.Activity = $resource(
    'https://www.googleapis.com/buzz/v1/activities/:userId/:visibility/:activityId/:comments',
    {alt:'json', callback:'JSON_CALLBACK'},
    {get:{method:'JSONP', params:{visibility:'@self'}}, replies: {method:'JSONP', params:{visibility:'@self', comments:'@comments'}}}
  );
}
 
BuzzController.prototype = {
  fetch: function() {
    this.activities = this.Activity.get({userId:this.userId});
  },
  expandReplies: function(activity) {
    activity.replies = this.Activity.replies({userId:this.userId, activityId:activity.id});
  }
};
BuzzController.$inject = ['$resource'];
