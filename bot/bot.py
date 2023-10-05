import requests
import random
import string
import json

with open("config.json", "r") as config_file:
    config = json.load(config_file)

base_url = "http://127.0.0.1:8000"


def generate_random_string(length):
    letters = string.ascii_letters
    return "".join(random.choice(letters) for _ in range(length))


def signup_users():
    for i in range(1, config["number_of_users"] + 1):
        email = f"user{i}@example.com"
        password = f"user{i}12qwas"
        response = requests.post(
            f"{base_url}/api/user/register/",
            json={"email": email, "password": password},
        )
        if response.status_code == 201:
            print(f"User {email} signed up successfully.")
        else:
            print(f"Failed to sign up user {email}.")


def create_posts(user_id, token):
    num_posts = random.randint(1, config["max_posts_per_user"] + 1)
    for _ in range(num_posts):
        content = generate_random_string(20)
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.post(
            f"{base_url}/api/posts/",
            json={"user": user_id, "content": content},
            headers=headers,
        )
        if response.status_code == 201:
            print(f"User {user_id} created a post.")
        else:
            print(f"Failed to create a post for user {user_id}.")


def like_posts(user_id, token):
    num_likes = random.randint(1, config["max_likes_per_user"] + 1)

    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(
        f"{base_url}/api/posts/",
        headers=headers,
    )
    if response.status_code != 200:
        print(f"Failed to retrieve posts for user {user_id}.")
        return

    posts = response.json()

    if not posts:
        print("No posts found.")
        return

    for _ in range(num_likes):
        post = random.choice(posts)
        post_id = post["id"]

        response = requests.post(
            f"{base_url}/api/posts/{post_id}/like/", headers=headers
        )

        if response.status_code == 201:
            print(f"User {user_id} liked post {post_id}")
        else:
            print(f"Failed to like post {post_id} for user {user_id}.")


def get_jwt_token(email, password):
    response = requests.post(
        f"{base_url}/api/user/token/",
        data={"email": email, "password": password}
    )
    if response.status_code == 200:
        token = response.json()["access"]
        return token
    else:
        print(f"Failed to get JWT token for user {email}.")
        return None


def main():
    signup_users()

    for i in range(1, config["number_of_users"] + 1):
        email = f"user{i}@example.com"
        password = f"user{i}12qwas"
        token = get_jwt_token(email, password)
        create_posts(i, token)
        like_posts(i, token)


if __name__ == "__main__":
    main()
