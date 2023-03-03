from kivymd.toast import toast
import base64
import json

def check_user_login_values(username, password):
        with open("database/login_values.txt", "r") as file:
            data = file.read()
        
        if data is not None:
            data = json.loads(data)
            
            try:
                values = data.get(username)
                check_pass = values.split(" ")[0]
                # check_pass = base64.b64decode(check_pass).decode("utf-8")
                
                if password == check_pass:
                    return True
                
                else:
                    print(check_pass)
                    toast("Incorrect Email or Password.")
                    
            except:
                toast("Incorrect Email or Password.")