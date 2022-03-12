# Blog

I'am creating a Blog using Django, Tailwind CSS and Crispy Forms.The blog has an authentication system and a visitor need to create a login username and password in order to visit the blog and make posts.

### Features

* Register user
* Login
* Contact
* Read, create, delete and update posts
* Read and delete messages
* Profile page
* Update userprofile
* Password reset
* Pagination
* list of comments in profile page

## Upcoming features


* search in posts page

### Blog start page

***
<br>


![2022-01-08 17 04 49 127 0 0 1 4673f2489882](https://user-images.githubusercontent.com/60063451/148651244-703ee7af-fa8e-4419-8a0b-4b1daa985117.png)


<br>

***

### A redirection will be made to login page after a visitor has registered as a user. A message will be shown on the login page that a user was registered. From here the newly registered user can login in to the blog.

***

![2022-01-22 13 23 46 127 0 0 1 3e89833cff8f](https://user-images.githubusercontent.com/60063451/150638565-669acc52-a23c-425b-8fcf-d058a013014f.png)

***


### A user is presented with new options in the navigation if the user has logged in

***

Left side in the navigation

``` python

{% if user.is_authenticated %}
  <a href="{% url 'create_post'  %}" class="mr-5 hover:text-gray-900">Create post</a>
  <a href="{% url 'profile'  %}"class="mr-5 hover:text-gray-900">My profile</a>
{% endif %}

```

Right side in the navigation

``` python

{% if user.is_authenticated %}
  <img src="{{ user.profile.image.url }}" alt="profile image" class="w-12 h-12 rounded-full object-cover">

  <p class="inline-flex items-center bg-gray-100 border-0 py-1 px-3 mr-5 rounded text-base mt-4 md:mt-0">
    Logged in as: {{ user.username }}
  </p>

  <a href="{% url 'logout' %}" class="inline-flex items-center bg-gray-100 border-0 py-1 px-3 focus:outline-none hover:bg-gray-200 rounded text-base mt-4 md:mt-0">Log out
    <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-1" viewBox="0 0 24 24">
      <path d="M5 12h14M12 5l7 7-7 7"></path>
    </svg>
  </a>
{% else %}
  <a href="{% url 'login'  %}" class="inline-flex items-center bg-gray-100 border-0 py-1 px-3 focus:outline-none hover:bg-gray-200 rounded text-base mt-4 md:mt-0">Login
    <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-1" viewBox="0 0 24 24">
      <path d="M5 12h14M12 5l7 7-7 7"></path>
    </svg>
  </a>
{% endif %}

```
![2022-01-22 09 49 35 127 0 0 1 328fad3a2657](https://user-images.githubusercontent.com/60063451/150633899-9909832f-e26d-4527-8029-92d2ace310fa.png)
***


### Links to post details will be visible if a user is authenticated and visits the posts page 

***

``` python
{% if user.is_authenticated %}
  <a href="{% url 'details' post.id %}" class="text-indigo-500 inline-flex items-center">Details
    <svg class="w-4 h-4 ml-2" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
      <path d="M5 12h14"></path>
      <path d="M12 5l7 7-7 7"></path>
    </svg>
  </a>
{% endif %}

```
![2022-01-22 10 23 45 127 0 0 1 0e4bf0475e4d](https://user-images.githubusercontent.com/60063451/150633974-945f37b7-54ad-4359-b447-fd71d52e01b2.png)
***


### Logged in user can comment on other users posts in the detail page of that post.

***

![2022-01-22 14 59 40 127 0 0 1 5bc9b5517a47](https://user-images.githubusercontent.com/60063451/150641395-f12ea8ea-88c0-4f5e-be0c-0053e82d4ddc.png)

***


### Delete and update options get visible When a logged in user is visiting a post made by the logged in user.

***

``` python

<div class="flex mb-4">
  <a class="flex-grow text-indigo-500 border-b-2 border-indigo-500 py-2 text-lg px-1">Details</a>
  {% if post.author == request.user %}
    <a href="{% url 'update_post' post.id %}" class="flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">Update</a>
    <a href="{% url 'delete' post.id %}" class="flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">Delete</a>
  {% endif %}
</div>

```

![2022-01-22 15 05 36 127 0 0 1 57ee860eeeb7](https://user-images.githubusercontent.com/60063451/150641682-da585c23-5e18-42e5-8591-79fbcf09fded.png)

***

### Delete button on a comment gets visible for the user who made the comment and for the user who made the post.

***

``` python

{% if post_comment.user == request.user or post.author == request.user %}
  <td class="px-6 py-4 whitespace-nowrap">
    <button type="submit" class="bg-red-500 hover:bg-red-700 text-white text-center py-2 px-4 rounded" >Delete</button>
  </td>
{% endif %}

```
![2022-01-24 19 31 12 127 0 0 1 783360c616d1](https://user-images.githubusercontent.com/60063451/150844300-93f03409-d679-4e97-a45c-bb07adf885fc.png)

***

### Profile page

***


![2022-01-23 19 34 03 127 0 0 1 90f9c618caae](https://user-images.githubusercontent.com/60063451/150692868-505cf722-9ebc-4aba-8824-1b131d8ae865.png)

***

### Update profile page

***

![2022-01-23 19 39 25 127 0 0 1 294f8122ee55](https://user-images.githubusercontent.com/60063451/150692936-b61b71a3-2a34-44c0-931e-4405d7617b1c.png)

***

### A success message will appear on the profile page after an update has been made to the user profile.

***

![2022-01-27 17 38 23 127 0 0 1 690a50eee936](https://user-images.githubusercontent.com/60063451/151403832-c1b51dab-3b98-48bf-832a-31685933cf36.png)

***

### Contact page

***

![2022-01-24 19 57 08 127 0 0 1 ed69e38673ea](https://user-images.githubusercontent.com/60063451/150846513-81127e63-a313-4fd4-9076-e6a5aac35239.png)
***

### After a mail has been sent a message will be shown on the posts page.

***

![2022-01-24 20 10 31 127 0 0 1 6c73667824f8](https://user-images.githubusercontent.com/60063451/150848330-5ae0aa10-cf95-4426-9c77-01304a52a179.png)

