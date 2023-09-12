from pocketbase import PocketBase  # Client also works the same
import pocketbase.client
def main(textInp, textInp1):
    client = PocketBase('https://late-diamond.pockethost.io')
    admin_data = client.admins.auth_with_password("sahilgaikwadofficial2004@gmail.com", "Sahil@123456")
    username = textInp
    password = textInp1
    data = {
        "username": username,
        "password": password,
        "passwordConfirm": password,
        "username1": username,
        "password1": password,
        "leaderboard": "121",
        "photo": "",
        "questions_right_wrong": ""
    }
    try:
        record = client.collection('userDetails').create(data)
        return "User created successfully"
    except pocketbase.client.ClientResponseError as record:
        return "Username is wrong"