from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Gayatri",
        "date": date(2024, 9, 20),
        "title": "Mountain Hiking",
        "excerpt": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed faucibus, ipsum eget rutrum semper, justo nunc ultricies lectus, at congue ligula velit vitae purus.",

        "content": """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed faucibus, ipsum eget rutrum semper, justo nunc ultricies lectus, at congue ligula velit vitae purus. 
        
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed faucibus, ipsum eget rutrum semper, justo nunc ultricies lectus, at congue ligula velit vitae purus.
        
         Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed faucibus, ipsum eget rutrum semper, justo nunc ultricies lectus, at congue ligula velit vitae purus.
        """

    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Gayatri",
        "date": date(2024, 9, 20),
        "title": "Programming Is Great!!",
        "excerpt": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed faucibus, ipsum eget rutrum semper, justo nunc ultricies lectus, at congue ligula velit vitae purus.",

        "content": """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed faucibus, ipsum eget rutrum semper, justo nunc ultricies lectus, at congue ligula velit vitae purus. 
        
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed faucibus, ipsum eget rutrum semper, justo nunc ultricies lectus, at congue ligula velit vitae purus.
        
         Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed faucibus, ipsum eget rutrum semper, justo nunc ultricies lectus, at congue ligula velit vitae purus.
        """

    }, {
        "slug": "into-thewoods",
        "image": "woods.jpg",
        "author": "Gayatri",
        "date": date(2024, 9, 20),
        "title": "Nature at its best!!!",
        "excerpt": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed faucibus, ipsum eget rutrum semper, justo nunc ultricies lectus, at congue ligula velit vitae purus.",

        "content": """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed faucibus, ipsum eget rutrum semper, justo nunc ultricies lectus, at congue ligula velit vitae purus. 
        
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed faucibus, ipsum eget rutrum semper, justo nunc ultricies lectus, at congue ligula velit vitae purus.
        
         Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed faucibus, ipsum eget rutrum semper, justo nunc ultricies lectus, at congue ligula velit vitae purus.
        """

    }
]

# Helper functions


def get_date(post):
    return post['date']

    # Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_post = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_post
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
