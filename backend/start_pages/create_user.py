from kivymd.toast import toast
import json
import re


def check_user_create_values(email, password, phone_number, root):
    is_valid_email(email, password, phone_number, root)


def is_valid_email(email, password, phone_number, root):
    if email is not None:

        if len(email) <= 5:
            toast("Your email must be at minimum 5 characters")

        elif re.search("\s", email):
            toast("You cannot have a space in your email.")

        else:
            is_valid_password(email, password, phone_number, root)


def is_valid_password(email, password, phone_number, root):
    if password is not None:

        if len(password) <= 8:
            toast("Your password must be at minimum 8 characters.")

        elif not re.search("[a-z]", password):
            toast("You must have a lowercase letter in your password.")

        # elif not re.search("[A-Z]", password):
        #     toast("You must have a capital letter in your password.")

        # elif not re.search("[0-9]", password):
        #     toast("You must have a number in your password.")

        elif re.search("\s", password):
            toast("You cannot have a space in your password.")

        else:
            create_database_entry(email, password, phone_number, root)


def create_database_entry(email, password, phone_number, root):

    with open("database/login_values.txt", "r") as file:
        data = file.read()

    if data is not None:
        data = json.loads(data)

        data[email] = f"{password}"

        with open("database/login_values.txt", "w") as file:
            file.write(json.dumps(data))

    print("Created user:", email)
    print(email, password, phone_number)

    current_screen = root.current

    # try:
    #     root.get_screen(current_screen).ids['phone_number'].text = "" # only used in create user
    # except:
    #     pass

    root.get_screen(current_screen).ids[
        "email"
    ].text = ""  # same for both login+create screens
    root.get_screen(current_screen).ids["password"].text = ""
    root.current = "Main_Page"
    toast("Created User.")
