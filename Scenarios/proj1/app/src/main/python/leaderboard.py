from pocketbase import PocketBase  # Client also works the same
import pocketbase.client
def update(username):
    client = PocketBase('https://late-diamond.pockethost.io')
    admin_data = client.admins.auth_with_password("sahilgaikwadofficial2004@gmail.com", "Sahil@123456")
    record = client.collection('userDetails').get_full_list()
    for x in record:
        if x.username1 == username:
            tempPoints = str(int(x.leaderboard) + 1)
            data = {
                "leaderboard": tempPoints
            }
            record = client.collection('userDetails').update(x.id,data)
            return tempPoints
