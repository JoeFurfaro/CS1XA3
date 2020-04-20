
# CS 1XA3 Project03 - furfaroj
## Setup
#### Cloning the Repository
Clone the course repository and navigate to the Project03 directory with the following commands:
```
git clone https://github.com/JoeFurfaro/CS1XA3
cd CS1XA3/Project03
```
#### Importing Working Conda Environment
Import the usable django conda environment with the following command:
```
conda env create -f proj3env.yml
```
#### Running the Project
The project is now ready to run! You can run the project on your local machine like this (replace python with your local python command or path):
```
python manage.py runserver localhost:8000
```
You can then access the project in a browser [here](http://localhost).

If you would rather run the project on the Mac1XA3 server, navigate to /home/furfaroj/private/CS1XA3/Project03 and run the following command:
```
python manage.py runserver localhost:10029
```
You can the access the project [here](https://mac1xa3.ca/u/furfaroj).

#### Available Testing Users

The following users are available to log in as in the test database:
| Username | Password |
|--|--|
| Pam | password |
| Jim | password |
| Sally | password |
| John | password |
| James | password |


## Objective 01
Description:

- Logs in and signs ups users by sending the contents of POST forms to the signup_view and login_view views
- The login view authenticates the user using their provided username and password
- The signup view creates a new user with the provided details and stores it in the database

Exceptions:

- Will fail user tries to create an account using a username that is already in use (new users must have unique IDs)

## Objective 02
Description:

- Populates the social base template with data from the UserInfo instance of the currently logged in user
- Shows the user's employment, location, birthday, and interests

Exceptions:

- Does not show any message if there are no interests, as this was not asked for

## Objective 03
Description:

- Provides a form for updating the user's password. The form sends POST data to the account_view view which updates and saves the user's new password
- Provides a form for updating the users employment, birthday, and location. The form sends POST data to the account_view view which updates the user's info in the database
- Provides a single-field form for adding interests which sends POST data to the account_view view that adds the interests in the database

Exceptions:

- Does not handle data parsing for valid inputs, as this was not asked for

## Objective 04
Description:

- Displays a list of users that the currently logged in user is not already friends with (by default shows one user)
- The list is rendered by the people_view view and rendered into the people template
- Allows the user to control how many users they can see by using the More button. When the button is clicked, the amount of users in the visible list in incremented by 1
- The number of people to show is reset when the user logs out

Exceptions:

- Shows users that may have already had a friend request sent to them, because we are not asked in the project to accommodate for this

## Objective 05
Description:

- Allows users to send friend requests using the friend request buttons rendered by the people view
- When the button is clicked, POST data is sent to the friend_request_request view, which creates a friend request including the correct users in the FriendRequest model
- The view will block duplicate friend requests between the same two users
- Renders a list of incoming requests using the people_view view into the people template

Exceptions:

- No status change of Send Friend Request buttons, as this was not asked for in the assignment

## Objective 06
Description:

-  Allows users to have the ability to accept and decline incoming friend requests
- The accept and decline buttons, when clicked, send POST data to the accept_decline_view view which processes and deletes the requests appropriately

Exceptions:

- Does not give the user feedback that the action was performed, as this was not asked of us

## Objective 07
Description:

- Displays a list of users that the current logged in user is friends with
- The list is generated from the database by the messages_view view and is rendered in the messages template

Exceptions:

- Does not show any special message to reassure the user that they have no friends :(

## Objective 08
Description:

- This objective allows the logged in user to post a new status using the new post form on the messages page
- When the Post button is clicked, a POST request is sent to the post_submit_view view which creates the new post associated with the logged in user in the database
- The view then renders the messages template with the new message showing

## Objective 09
Description:

- This objective queries a list of all posts sorted newest to oldest, and shows the amount of posts that the user desires (which is 1 by default)
- When the view is run, it collects the posts and shows the correct amount (which is stored in a session variables) and renders them into the messages template
- The amount of posts to show can be increased by clicking the more button (each click increments the session variable by 1)
- The amount of posts to show is reset to 1 when the user logs out

Exceptions:

- Does not show any special message if there are no posts, as this was not asked for

## Objective 10
Description:

- Allows the user to like posts on the messages page and displays the like count of each post visible to the user
- The message_view view processes the like and validates that it is not a duplicate like
- The view then renders all posts into the messages template
- Once a like is placed on a post, the like button is disabled on that post as an extra prevention measure for duplicate likes

Exceptions:

- There is no way for users to unlike posts... guess they are stuck forever in their initial opinion :)

## Objective 11
Description:

- A test database has been created to show off all the features more easily and to help the TAs mark the project! The test user logins can be found in the table below.

| Username | Password |
|--|--|
| Pam | password |
| Jim | password |
| Sally | password |
| John | password |
| James | password |
