from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app =Flask (__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFATICATIONS']=False

db=SQLAlchemy(app)




class Student_Registrations(db.Model):
    id =db.Column(db.Integer,primary_key=True,autoincrement=True)
    studentname=db.Column(db.String(50))
    gender=db.Column(db.String(10))
    parentname=db.Column(db.String(100))
    phone=db.Column(db.String(10))
    address=db.Column(db.String(100))


    

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/studentrecord')
def studentrecord():
    return render_template('studentrecord.html')




@app.route('/reg', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':

        studentname = request.form.get('name')
        gender = request.form.get('gender')
        parentname = request.form.get('parentname')
        phone = request.form.get('phone')
        address = request.form.get('address')

        data = Student_Registrations(
            studentname=studentname,
            gender=gender,
            parentname=parentname,
            phone=phone,
            address=address
        )

        db.session.add(data)
        db.session.commit()

        # return "Data Stored Successfully"

    return render_template('form.html')

@app.route('/view')
def view():
    data=Student_Registrations.query.all()
    print(data)
    return render_template('view.html',data=data)


@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    data=Student_Registrations.query.get_or_404(id)
    if request.method == 'POST':
        data.studentname = request.form.get('name')
        data.gender = request.form.get('gender')
        data.parentname = request.form.get('parentname')
        data.phone = request.form.get('phone')
        data.address = request.form.get('address')
        db.session.commit()
        return redirect(url_for('view'))
    return render_template('update.html',data=data)


@app.route('/delete/<int:id>')
def delete(id):
    data=Student_Registrations.query.get_or_404(id)
    db.session.delete(data)
    db.session.commit()
    return 'data deleted'







if __name__ == '__main__':
    app.run(debug=True)
