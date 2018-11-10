from flask import Flask, request
app =Flask(__name__)
app.config['DEBUG']=True

form = """
<!Doctype html>
<html>
    <head>
        <style>
            .error {{color:red;}}
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="post">
             <div class="container">
               <h1>Sign Up</h1>
               <hr>
               <label for="username"><b>Username</b></label>
               <input type="text" placeholder="Enter Username" name= "username" value='{username}' required>
               <label class= "error">{username_error}</label>
               <br>
               <br>
               <p>
             </div>

               <label for="psw"><b>Password</b></label>
               <input type="password" placeholder="Enter Password" name="Password" value='{Password}' required>
               <label class= "error">{psw_error}</label>
               <br>
               <br>
               <p>

               <label for="psw-repeat"><b>Verify Password</b></label>
               <input type="password" placeholder="Verify Password" name= "Verify_Pwd" value='{Verify_Pwd}'required>
               <label class= "error">{pswrepeat_error}</label>
               <br>
               <br>
               <p>

               <label for="email"><b>Email(optional)</b></label>
               <input type="text" placeholder="Enter Email" name="email" value='{email}'>
               <label class= "error">{email_error}</label>
               <br>
               <br>

             <div class="clearfix">
             <input type="Submit" value="Submit"/> 
             </div>
  
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format(username='',username_error='', Password='', psw_error='',Verify_Pwd='',pswrepeat_error='', email='', email_error='')

def username_validate(username):
    if len(username) > 3 and len(username) < 20 and username != username.isspace():
        return True
    else:
        return False

def pwd_validate(Password):
    if len(Password) > 3 and len(Password) < 20 and Password != Password.isspace():
        return True
    else:
        return False

def verifypwd_validate(Verify_Pwd, Password):
    if Verify_Pwd == Password:
        return True
    else:
        return False

def email_validate(email):
    if len(email) > 3 and len(email) < 20 and email != email.isspace():
        if email.count("@")==1 and email.count(".")==1:
            return True
    return False



@app.route("/", methods=['Post'])
def validate_form():

    username = request.form['username']
    Password = request.form['Password']
    Verify_Pwd = request.form['Verify_Pwd']
    email = request.form['email']

    username_error = ''
    psw_error = ''
    pswrepeat_error = ''
    email_error= ''

    if not username_validate(username):
        username_error = 'Not a valid Username'
    if not pwd_validate(Password):
        psw_error='Not a valid Password'
        Password=''
        Verify_Pwd =''
    if not verifypwd_validate(Verify_Pwd, Password):
        pswrepeat_error = 'Password doesnot match'
        Verify_Pwd =''
    if not email_validate(email):
        email_error = 'Invalid email address'

    if not username_error and not psw_error and not pswrepeat_error and not email_error:
        return 'Welcome, ' + username
    else:
        return form.format (username_error=username_error,psw_error=psw_error, pswrepeat_error=pswrepeat_error, email_error=email_error, username=username,Password=Password,Verify_Pwd=Verify_Pwd, email=email)



app.run()
