from pocketbase import PocketBase  # Client also works the same
import pocketbase.client
def main(textInp, textInp2):
    client = PocketBase('https://late-diamond.pockethost.io')
    admin_data = client.admins.auth_with_password("sahilgaikwadofficial2004@gmail.com", "Sahil@123456")
    username = textInp
    password = textInp2
    try:
        authData = client.collection('userDetails').auth_with_password(
            username,
            password
        )
        return "Accepted"
    except pocketbase.client.ClientResponseError as authData:
        return "Invalid auth"