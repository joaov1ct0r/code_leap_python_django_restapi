from django.test import TestCase, Client
from .models import Post

def create_new_post(username, title, content):
    post = Post(
        username=username,
        title=title,
        content=content
    )
    post.save()

    return post

# Create your tests here.
class TestPostView(TestCase):
    def __init__(self, method_name):
        super().__init__(method_name)
        self.path = "/careers/"
        self.client = Client()

    def test_get_all_posts(self):
        create_new_post(
            username="any_username",
            title="any title",
            content="any content"
        )

        response = self.client.get(self.path)

        self.assertEqual(response.status_code, 200)

    def test_delete_post_does_not_exist(self):
        response = self.client.delete(f"{self.path}100/")

        self.assertEqual(response.status_code, 404)

    def test_delete_post(self):
        post = create_new_post(
            username="any_username",
            title="any title",
            content="any content"
        )

        response = self.client.delete(f"{self.path}{str(post.id)}/")

        self.assertEqual(response.status_code, 204)

    def test_create_post_not_valid(self):
        response = self.client.post(
            self.path,
            {
                "title": "any title",
                "content": "any content"
            }
        )

        self.assertEqual(response.status_code, 400)

    def test_create_post(self):
        response = self.client.post(
            self.path,
            {
                "username": "any_username",
                "title": "any title",
                "content": "any content"
            }
        )

        self.assertEqual(response.status_code, 201)

    def test_patch_post_not_valid(self):
        post = create_new_post(
            username="any_username",
            title="any title",
            content="any content"
        )

        response = self.client.patch(
            f"{self.path}{str(post.id)}/",
            {
                "title": "any other title",
            },
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)

    def test_patch_post_does_not_exist(self):
        response = self.client.patch(
            f"{self.path}1000/",
            {
                "title": "any other title",
                "content": "any other content"
            },
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 404)

    def test_patch_post(self):
        post = create_new_post(
            username="any_username",
            title="any title",
            content="any content"
        )

        response = self.client.patch(
            f"{self.path}{str(post.id)}/",
            {
                "title": "any other title",
                "content": "any other content"
            },
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 204)