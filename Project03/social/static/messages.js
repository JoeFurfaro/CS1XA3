/* ********************************************************************************************
   | Handle Submitting Posts - called by $('#post-button').click(submitPost)
   ********************************************************************************************
   */
function submitPost() {
    // the id of the current button, should be fr-name where name is valid username
    let json_data = { 'post_text' : $("#post-text").val() };
    // globally defined in messages.djhtml using i{% url 'social:like_view' %}
    let url_path = post_submit_url;

    // AJAX post
    $.post(url_path,
           json_data,
           function(data, status) {
               if(status == 'success') {
                   location.reload();
               }
           });
}

/* ********************************************************************************************
   | Handle Liking Posts - called by $('.like-button').click(submitLike)
   ********************************************************************************************
   */
function submitLike(event) {
    // the id of the current button, should be fr-name where name is valid username
    let btnID = event.target.id;
    let json_data = { 'btnID' : btnID };
    // globally defined in messages.djhtml using i{% url 'social:like_view' %}
    let url_path = like_post_url;

    // AJAX post
    $.post(url_path,
           json_data,
           function(data, status) {
               if(status == 'success') {
                   location.reload();
               }
           });
}

/* ********************************************************************************************
   | Handle Requesting More Posts - called by $('#more-button').click(submitMore)
   ********************************************************************************************
   */
function moreResponse(data,status) {
    if (status == 'success') {
        // reload page to display new Post
        location.reload();
    }
    else {
        alert('failed to request more posts' + status);
    }
}

function submitMore(event) {
    // submit empty data
    let json_data = { };
    // globally defined in messages.djhtml using i{% url 'social:more_post_view' %}
    let url_path = more_post_url;

    // AJAX post
    $.post(url_path,
           json_data,
           moreResponse);
}

/* ********************************************************************************************
   | Document Ready (Only Execute After Document Has Been Loaded)
   ********************************************************************************************
   */
$(document).ready(function() {
    // handle post submission
    $('#post-button').click(submitPost);
    // handle likes
    $('.like-button').click(submitLike);
    // handle more posts
    $('#more-button').click(submitMore);
});
