# main class of the program, when called it will initiate a new insctance of User with attributes defined below:
class User:
    def __init__(self, name, engagement):
        self.name = name
        self.engagement_metrics = engagement
        self.score = 0

    def __repr__(self):
        return f"<User {self.name}>"

    
def get_user_score(user):
    try:
        user.score = perform_calculation(user.engagement_metrics)
    except KeyError:
        print("Incorre values provided to our calculation function.")
        raise
    finally:
        if user.score > 10000:
            send_engagement_notification(user)

def perform_calculation(metrics):
    return metrics['clicks'] * 5 * metrics['hits'] * 2

def send_engagement_notification(user):
    print(f"Notification sent to {user}.")

my_user = User('Rolf', {'clicks': 61, 'hits': 100}) # typo click instead of clicks would cause an error to be reraised with raise keyword after the custom error printed out
# my_user = User('Rolf', {'click': 61, 'hits': 100}) -> typo in clicks would cause the except to be executed and "Incorre values provided to our calculation function." will be
# printed


get_user_score(my_user)