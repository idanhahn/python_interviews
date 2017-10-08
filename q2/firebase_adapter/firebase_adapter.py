from firebase.firebase import FirebaseAuthentication, FirebaseApplication


class FirebaseAdapter:

    def __init__(self):
        secret = "JSY4MQ99VvTqD4pWS7EScPR6de2HXf9xzE179o1g"
        email = "idan@waycaretech.com"
        debug = False
        admin = True
        url = "https://temp-waycare.firebaseio.com"
        authentication = FirebaseAuthentication(secret, email, debug, admin)
        self._firebase = FirebaseApplication(url, authentication)

    '''
        add all methods here
    '''
