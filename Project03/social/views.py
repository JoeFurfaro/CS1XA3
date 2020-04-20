from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages

from . import models

def messages_view(request):
    """Private Page Only an Authorized User Can View, renders messages page
       Displays all posts and friends, also allows user to make new posts and like posts
    Parameters
    ---------
      request: (HttpRequest) - should contain an authorized user
    Returns
    --------
      out: (HttpResponse) - if user is authenticated, will render private.djhtml
    """
    if request.user.is_authenticated:
        if request.session.get("num_post_show") == None:
            request.session["num_post_show"] = 1

        user_info = models.UserInfo.objects.get(user=request.user)

        # TODO Objective 9: query for posts (HINT only return posts needed to be displayed)
        posts = models.Post.objects.all().order_by('-timestamp')
        posts = posts[0:request.session.get("num_post_show")]
        for post in posts:
            post.self_liked = user_info in post.likes.all()

        # TODO Objective 10: check if user has like post, attach as a new attribute to each post

        context = { 'user_info' : user_info
                  , 'posts' : posts }
        return render(request,'messages.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def account_view(request):
    """Private Page Only an Authorized User Can View, allows user to update
       their account information (i.e UserInfo fields), including changing
       their password
    Parameters
    ---------
      request: (HttpRequest) should be either a GET or POST
    Returns
    --------
      out: (HttpResponse)
                 GET - if user is authenticated, will render account.djhtml
                 POST - handle form submissions for changing password, or User Info
                        (if handled in this view)
    """
    if request.user.is_authenticated:
        form = None

        # TODO Objective 3: Create Forms and Handle POST to Update UserInfo / Password

        user_info = models.UserInfo.objects.get(user=request.user)

        if request.method == 'POST':
            type = request.POST['type']
            if type == "details":
                employment = request.POST['employment']
                location = request.POST['location']
                birthday = request.POST['birthday']
                if birthday == "":
                    birthday = None
                user_info.employment = employment
                user_info.location = location
                user_info.birthday = birthday
                user_info.save()
            elif type == "interests":
                new_interest = request.POST['interest']
                user_info.interests.add(models.Interest.objects.create(label=new_interest))
                user_info.save()
            elif type =="password":
                new_pass = request.POST['new-password']
                user_info.user.set_password(new_pass)
                user_info.user.save()


        context = { 'user_info' : user_info,
                    'form' : form }
        return render(request,'account.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def people_view(request):
    """Private Page Only an Authorized User Can View, renders people page
       Displays all users who are not friends of the current user and friend requests
    Parameters
    ---------
      request: (HttpRequest) - should contain an authorized user
    Returns
    --------
      out: (HttpResponse) - if user is authenticated, will render people.djhtml
    """
    if request.user.is_authenticated:
        if request.session.get("num_people_show") == None:
            request.session["num_people_show"] = 1
        user_info = models.UserInfo.objects.get(user=request.user)
        # TODO Objective 4: create a list of all users who aren't friends to the current user (and limit size)
        all_people = []
        people = models.UserInfo.objects.all()
        friends = user_info.friends.all()
        for person in people:
            if person not in friends and person != user_info:
                all_people.append(person)

        if len(all_people) > 0:
            all_people = all_people[0:request.session.get("num_people_show")]

        # TODO Objective 5: create a list of all friend requests to current user
        friend_requests = models.FriendRequest.objects.filter(to_user=user_info)

        context = { 'user_info' : user_info,
                    'all_people' : all_people,
                    'friend_requests' : friend_requests }

        return render(request,'people.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def like_view(request):
    '''Handles POST Request recieved from clicking Like button in messages.djhtml,
       sent by messages.js, by updating the corrresponding entry in the Post Model
       by adding user to its likes field
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute postID,
                                a string of format post-n where n is an id in the
                                Post model

	Returns
	-------
   	  out : (HttpResponse) - queries the Post model for the corresponding postID, and
                             adds the current user to the likes attribute, then returns
                             an empty HttpResponse, 404 if any error occurs
    '''
    post_id = request.POST.get('btnID')
    if post_id is not None:
        # remove 'post-' from postID and convert to int
        # TODO Objective 10: parse post id from postIDReq
        postID = int(post_id[5:])

        if request.user.is_authenticated:
            # TODO Objective 10: update Post model entry to add user to likes field
            user_info = models.UserInfo.objects.get(user=request.user)
            posts = models.Post.objects.all().order_by('-timestamp')

            post = posts[postID]
            if user_info not in post.likes.all():
                post.likes.add(user_info)

            # return status='success'
            return HttpResponse('success')
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('like_view called without postID in POST')

def post_submit_view(request):
    '''Handles POST Request recieved from submitting a post in messages.djhtml by adding an entry
       to the Post Model
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute postContent, a string of content

	Returns
	-------
   	  out : (HttpResponse) - after adding a new entry to the POST model, returns an empty HttpResponse,
                             or 404 if any error occurs
    '''
    postContent = request.POST.get('post_text')
    if postContent is not None:
        if request.user.is_authenticated:
            user_info = models.UserInfo.objects.get(user=request.user)
            # TODO Objective 8: Add a new entry to the Post model
            post = models.Post(owner=user_info, content=postContent)
            post.save()
            # return status='success'
            return HttpResponse("success")
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('post_submit_view called without postContent in POST')

def more_post_view(request):
    '''Handles POST Request requesting to increase the amount of Post's displayed in messages.djhtml
    Parameters
	----------
	  request : (HttpRequest) - should be an empty POST

	Returns
	-------
   	  out : (HttpResponse) - should return an empty HttpResponse after updating hte num_posts sessions variable
    '''
    if request.user.is_authenticated:
        # update the # of posts dispalyed
        if request.session.get("num_post_show") == None:
            request.session["num_post_show"] = 1

        request.session["num_post_show"] += 1
        # TODO Objective 9: update how many posts are displayed/returned by messages_view

        # return status='success'
        return HttpResponse('success')

    return redirect('login:login_view')

def more_ppl_view(request):
    '''Handles POST Request requesting to increase the amount of People displayed in people.djhtml
    Parameters
	----------
	  request : (HttpRequest) - should be an empty POST

	Returns
	-------
   	  out : (HttpResponse) - should return an empty HttpResponse after updating the num ppl sessions variable
    '''
    if request.user.is_authenticated:
        # update the # of people dispalyed
        if request.session.get("num_people_show") == None:
            request.session["num_people_show"] = 1

        request.session["num_people_show"] += 1

        # TODO Objective 4: increment session variable for keeping track of num ppl displayed

        # return status='success'
        return HttpResponse("success")

    return redirect('login:login_view')

def friend_request_view(request):
    '''Handles POST Request recieved from clicking Friend Request button in people.djhtml,
       sent by people.js, by adding an entry to the FriendRequest Model
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute frID,
                                a string of format fr-name where name is a valid username

	Returns
	-------
   	  out : (HttpResponse) - adds an etnry to the FriendRequest Model, then returns
                             an empty HttpResponse, 404 if POST data doesn't contain frID
    '''
    frID = request.POST.get('frID')
    if frID is not None:
        # remove 'fr-' from frID
        username = frID[3:]
        if request.user.is_authenticated:
            user_info = models.UserInfo.objects.get(user=request.user)
            users = models.UserInfo.objects.all()
            target_user = None
            for user in users:
                if user.user.username == username:
                    target_user = user
            # TODO Objective 5: add new entry to FriendRequest
            req_match = models.FriendRequest.objects.filter(to_user=target_user, from_user=user_info)
            if len(req_match) == 0:
                friend_req = models.FriendRequest(to_user=target_user, from_user=user_info)
                friend_req.save()
            # return status='success'
            return HttpResponse("success")
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('friend_request_view called without frID in POST')

def accept_decline_view(request):
    '''Handles POST Request recieved from accepting or declining a friend request in people.djhtml,
       sent by people.js, deletes corresponding FriendRequest entry and adds to users friends relation
       if accepted
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute decision,
                                a string of format A-name or D-name where name is
                                a valid username (the user who sent the request)

	Returns
	-------
   	  out : (HttpResponse) - deletes entry to FriendRequest table, appends friends in UserInfo Models,
                             then returns an empty HttpResponse, 404 if POST data doesn't contain decision
    '''
    data = request.POST.get('frID')
    if data is not None:
        # TODO Objective 6: parse decision from data
        username = data[2:]
        type=data[0]
        if request.user.is_authenticated:
            user_info = models.UserInfo.objects.get(user=request.user)
            users = models.UserInfo.objects.all()
            target_user = None
            for user in users:
                if user.user.username == username:
                    target_user = user
            if type == "A":
                # add req
                user_info.friends.add(target_user)
            friend_req = models.FriendRequest.objects.filter(from_user=target_user,to_user=user_info)[0]
            friend_req.delete()
            # TODO Objective 6: delete FriendRequest entry and update friends in both Users

            # return status='success'
            return HttpResponse("success")
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('accept-decline-view called without decision in POST')
