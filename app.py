from flask import Flask,render_template,url_for,request,redirect,session,json,jsonify
app=Flask(__name__)
from predict import pred
app.secret_key='test'

from flask_sqlalchemy import SQLAlchemy 
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.db'
db=SQLAlchemy(app)

class users(db.Model):
    username=db.Column(db.String(30),primary_key=True)
    password=db.Column(db.String(30))
    def __repr__(self):
        return f"{self.username}:{self.password}"

@app.route('/')
def home():
    return render_template("index1.html",session=session)

@app.route('/login',methods=['POST','GET'])
def login():
    if(request.method=='POST'):
        if(request.form['button']=='Register'):
            username=request.form['un']
            password=request.form['ps']
            new = users(username=username,password=password)
            db.session.add(new)
            db.session.commit()
            session['username'] = username
            return redirect('/')
            
        if(request.form['button']=='Login'):
            username=request.form['unl']
            password=request.form['psl']
            db_obj = users.query.all()
            for i in range(len(db_obj)):
                db_str = str(db_obj[i])
                db_list = db_str.split(':')
                if username == db_list[0]:
                    if password == db_list[1]:
                        session['username'] = username
                        return redirect('/')
                    else:
                        return redirect('/404')
            return redirect('/404') 
            
    return render_template("login.html")


@app.route('/logout')
def logout():
    del session['username']
    return redirect('/')

@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        form_data = (request.form)
        data={}
        if 'breathing' in form_data: data['breathing'] = 1
        else: data['breathing'] = 0
        if 'fever' in form_data: data['fever'] = 1
        else: data['fever'] = 0
        if 'drycough' in form_data: data['drycough'] = 1
        else: data['drycough'] = 0
        if 'sorethroat' in form_data: data['sorethroat'] = 1
        else: data['sorethroat'] = 0
        if 'runnose' in form_data: data['runnose'] = 1
        else: data['runnose'] = 0
        if 'asthma' in form_data: data['asthma'] = 1
        else: data['asthma'] = 0
        if 'chroniclung' in form_data: data['chroniclung'] = 1
        else: data['chroniclung'] = 0
        if 'headache' in form_data: data['headache'] = 1
        else: data['headache'] = 0
        if 'heart' in form_data: data['heart'] = 1
        else: data['heart'] = 0
        if 'diabetes' in form_data: data['diabetes'] = 1
        else: data['diabetes'] = 0
        if 'hypertension' in form_data: data['hypertension'] = 1
        else: data['hypertension'] = 0
        if 'fatigue' in form_data: data['fatigue'] = 1
        else: data['fatigue'] = 0
        if 'gastro' in form_data: data['gastro'] = 1
        else: data['gastro'] = 0
        if 'abroad' in form_data: data['abroad'] = 1
        else: data['abroad'] = 0
        if 'covid' in form_data: data['covid'] = 1
        else: data['covid'] = 0
        if 'large' in form_data: data['large'] = 1
        else: data['large'] = 0
        if 'high' in form_data: data['high'] = 1
        else: data['high'] = 0
        if 'public' in form_data: data['public'] = 1
        else: data['public'] = 0
        print(data)
        output = pred(data["breathing"],data["fever"],data["drycough"],data["sorethroat"],data["runnose"],data["asthma"],data["chroniclung"],data["headache"],data["heart"],data["diabetes"],data["hypertension"],data["fatigue"],data["gastro"],data["abroad"],data["covid"],data["large"],data["high"],data["public"])
        output = str(output)
        return redirect('/result/'+ output)
        
    if 'username' in session:
        return render_template("predict.html")
    else:
        return redirect('/login')

@app.route('/about')
def about():
    return render_template("abt.html", session = session)

@app.route('/result/<res>')
def result(res):
    return render_template('result.html',res=res)

@app.route('/404')
def err():
    return render_template("failed.html")

if __name__ == "__main__":
    app.run(debug=True)
    