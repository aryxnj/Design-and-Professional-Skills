from pocketbase import PocketBase  # Client also works the same
import pocketbase.client
import random
def upload(question, answer):
    try:
        pb = PocketBase('https://late-diamond.pockethost.io')
        admin_data = pb.admins.auth_with_password("sahilgaikwadofficial2004@gmail.com", "Sahil@123456")
        data = {
            "question": question,
            "solution": answer
        }
        record = pb.collection('questionAnswers').create(data)
    except:
        print("something went wrong")
def readRandom():
    pb = PocketBase('https://late-diamond.pockethost.io')
    admin_data = pb.admins.auth_with_password("sahilgaikwadofficial2004@gmail.com", "Sahil@123456")
    record = pb.collection("questionAnswers").get_full_list()
    a = random.choice(record)
    return a.question, a.solution
