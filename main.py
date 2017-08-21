from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def cool():
        return render_template("confirm.html")

@app.route("/", methods= ['POST'])
def power():
    print('o')
    username= request.form["username"]
    print('o')
    password= request.form["password"]
    print('o')
    verify= request.form["verify"]
    print('o')
    email= request.form["email"]
    print('o')

    wrongname= ''
    wrongpassword=''
    wrong_password_verify=''
    wrongemail=''

    if len(username) > 20 or len(username) < 3: 
      print('o')
      wrongname="not valid username"

    elif len(password) > 20 or len(password) < 3:
      print('o')
      wrongpassword="not valid password"
          
    if ' ' in username or username=='':
      print('o')
      wrongname= "please enter username"  

    elif ' ' in password or password=='':
      print('o')
      wrongpassword= "please enter password"   

    if verify != password and len(password)>3:
      print('o')
      wrong_password_verify= 'passwords does not match'
      verify= ''      

    if email != '':
      if len(email) < 3 or len(email) > 20 or '@' not in email or '.' not in email:
        print('o')
        wrongemail= "please enter valid email" 
        email= '' 

    if not wrongname and not wrongpassword and not wrong_password_verify:
      print('o')
      return redirect ('/base?username={0}'.format(username))

   
    else:
      print('o')
      return render_template('confirm.html', username=username, email=email, wrongname=wrongname, wrongpassword= wrongpassword, wrong_password_verify=wrong_password_verify, wrongemail=wrongemail)
      
@app.route('/base')
def base():
  username = request.args.get('username')
  return render_template('base.html', username=username)

app.run()        


    




