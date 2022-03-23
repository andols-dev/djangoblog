# Blog

I have created a Blog using Django and Bootstrap 5.The blog has an authentication system and a visitor needs to create a login username and password in order to visit the blog and make posts.

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

### Blog start page:

![2022-03-17 18 12 58 127 0 0 1 ae1b23c46317](https://user-images.githubusercontent.com/60063451/158856782-ddaaf724-0403-4fbd-aba4-69a623805788.jpg)

***
A message will be shown if no posts have been added.
***

![2022-03-22 18 28 03 127 0 0 1 9c71e89b6af5](https://user-images.githubusercontent.com/60063451/159540436-56782c39-84f5-4cf5-8334-9c0ada3cd6e1.jpg)


### Sign up page:

![2022-03-17 18 23 23 127 0 0 1 86e87fc4f069](https://user-images.githubusercontent.com/60063451/158858737-fd1b8020-943c-4ba6-92f6-b7885c0213c8.jpg)

### Login page:

![2022-03-17 18 19 07 127 0 0 1 3cdb4600d6e9](https://user-images.githubusercontent.com/60063451/158857870-0aaa4198-f839-4d0f-aa33-672c04f8d215.jpg)

***

### A redirection will be made to login page after a visitor has registered as a user. A message will be shown on the login page that a user was registered. From here the newly registered user can login in to the blog.

***
``` python
{% if messages %}
<div class="container">
    <div class="row">
        <div class="col-md-6 offset-md-3">
            {% for message in messages %}<div class="alert alert-success" role="alert">{{ message }}</div>{% endfor %}
        </div>
    </div>
  </div>
{% endif %}
```
![2022-03-23 16 49 26 127 0 0 1 fe30da50683c](https://user-images.githubusercontent.com/60063451/159740403-15ecbbc3-3f71-4b9e-a9e2-d3db68351332.jpg)


***
When creating a user, a user profile will be created automatically using signals.
***
``` python
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)
 ```
***
Pagination
***
``` python
{% if posts %}
        <div class="d-flex justify-content-center">
            <nav aria-label="...">
                <ul class="pagination">
                    {% if posts.has_previous %}
                        <li class="page-item">
                            <a class="page-link"
                               href="?page={{ posts.previous_page_number }}"
                               class="">
                                <span class="sr-only">Previous</span>
                            </a>
                        </li>
                    {% endif %}
                    {% for i in posts.paginator.page_range %}
                        {% if posts.number == i %}
                            <li class="page-item active" aria-current="page">
                                <span class="page-link">{{ i }}</span>
                            </li>
                        {% else %}
                            <li class="page-item">
                                <a class="page-link" href="?page={{ i }}">{{ i }}</a>
                            </li>
                        {% endif %}
                    {% endfor %}
                    {% if posts.has_next %}
                        <li class="page-item">
                            <a class="page-link" href="?page={{ posts.next_page_number }}">Next</a>
                        </li>
                    {% endif %}
                </ul>
            </nav>
        </div>
    {% endif %}
```
