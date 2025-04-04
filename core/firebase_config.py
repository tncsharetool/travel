import pyrebase

firebase_config = {
    "apiKey": "AIzaSyBGZe rE...gN6g4Lc",  # bạn copy key từ Firebase
    "authDomain": "vietnam-ai-travel.firebaseapp.com",
    "databaseURL": "",  # nếu dùng realtime database
    "projectId": "vietnam-ai-travel",
    "storageBucket": "vietnam-ai-travel.appspot.com",
    "messagingSenderId": "725014092380",
    "appId": "1:725014092380:web:c2920e5a7ded9a747f2499",
    "measurementId": "G-JLCFEFDPCG"
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
