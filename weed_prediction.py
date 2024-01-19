from flask import Flask,request,render_template,session,redirect
import datetime
from DBConnection import Db

app = Flask(__name__)
app.secret_key="weed_prediction"


@app.route('/', methods=['get', 'post'])
def login():
    if request.method == 'POST':
        uname = request.form['em']
        passwd = request.form['ps']
        db = Db()
        QRY = db.selectOne("select * from login WHERE username='" + uname + "' and password='" + passwd + "'")
        if QRY is not None:
            session['lid'] = QRY['login_id']
            if QRY['user_type'] == 'admin':
                session['lg'] = 'lin'
                return '''<script>alert('login successfully');window.location="/admin_home"</script>'''
            elif QRY['user_type'] == 'user':
                session['lg'] = 'lin'
                session['lid']=QRY['login_id']
                return '''<script>alert('login successfully');window.location="/user_home"</script>'''
        else:
            return '''<script>alert('user not found');window.location="/"</script>'''

    else:
        db = Db()
        qry = "select rating.ratings,rating.date,user.name,rating.r_id from user,rating where user.user_id=rating.user_id order by r_id desc"
        res = db.select(qry)

        ar_rt = []

        for im in range(0, len(res)):
            val = str(res[im]['ratings'])
            ar_rt.append(val)
        fs = "/static/star/full.jpg"
        hs = "/static/star/half.jpg"
        es = "/static/star/empty.jpg"
        arr = []

        for rt in ar_rt:
            print(rt)
            a = float(rt)

            if a >= 0.0 and a < 0.4:
                print("eeeee")
                ar = [es, es, es, es, es]
                arr.append(ar)

            elif a >= 0.4 and a < 0.8:
                print("heeee")
                ar = [hs, es, es, es, es]
                arr.append(ar)

            elif a >= 0.8 and a < 1.4:
                print("feeee")
                ar = [fs, es, es, es, es]
                arr.append(ar)

            elif a >= 1.4 and a < 1.8:
                print("fheee")
                ar = [fs, hs, es, es, es]
                arr.append(ar)

            elif a >= 1.8 and a < 2.4:
                print("ffeee")
                ar = [fs, fs, es, es, es]
                arr.append(ar)

            elif a >= 2.4 and a < 2.8:
                print("ffhee")
                ar = [fs, fs, hs, es, es]
                arr.append(ar)

            elif a >= 2.8 and a < 3.4:
                print("fffee")
                ar = [fs, fs, fs, es, es]
                arr.append(ar)

            elif a >= 3.4 and a < 3.8:
                print("fffhe")
                ar = [fs, fs, fs, hs, es]
                arr.append(ar)

            elif a >= 3.8 and a < 4.4:
                print("ffffe")
                ar = [fs, fs, fs, fs, es]
                arr.append(ar)

            elif a >= 4.4 and a < 4.8:
                print("ffffh")
                ar = [fs, fs, fs, fs, hs]
                arr.append(ar)

            elif a >= 4.8 and a <= 5.0:
                print("fffff")
                ar = [fs, fs, fs, fs, fs]
                arr.append(ar)
            print(arr)
        return render_template('loginindex.html', resu=res, r1=arr, ln=len(arr))





# ===============================================================================================================================
#                                                 ADMIN MODULE
# ===============================================================================================================================


@app.route('/admin_home')
def admin_home():
    if session['lg']=='lin':
        return render_template('admin/admin_index.html')

    else:
        return redirect('/')


@app.route('/view_user')
def view_user():
    if session['lg']=='lin':

        db=Db()
        qry=db.select("select * from `user`")
        return render_template('admin/view_users.html',data=qry)

    else:
        return redirect('/')

@app.route('/view_complaint')
def view_complaint():
    if session['lg']=='lin':

        db=Db()
        qry=db.select("select * from `user`,complaint where user.user_id=complaint.user_id")
        return render_template('admin/view_Complaint.html',data=qry)


    else:
        return redirect('/')

@app.route('/reply/<cid>',methods=['get','post'])
def reply(cid):
    if session['lg']=='lin':

        if request.method=="POST":
            r=request.form['textarea']
            db=Db()
            db.update("update complaint set reply='"+r+"', r_date=curdate() where c_id='"+str(cid)+"'")
            return '''<script>alert('success');window.location="/view_complaint"</script>'''
        else:
            return render_template('admin/send_reply.html')

    else:
        return redirect('/')

@app.route('/apprating')
def ar():
    if session['lg']=='lin':

        db=Db()
        qry="select rating.ratings,rating.date,user.name,rating.r_id from user,rating where user.user_id=rating.user_id order by r_id desc"
        res=db.select(qry)

        ar_rt = []

        for im in range(0, len(res)):
            val = str(res[im]['ratings'])
            ar_rt.append(val)
        fs = "/static/star/full.jpg"
        hs = "/static/star/half.jpg"
        es = "/static/star/empty.jpg"
        arr = []

        for rt in ar_rt:
            print(rt)
            a = float(rt)

            if a >= 0.0 and a < 0.4:
                print("eeeee")
                ar = [es, es, es, es, es]
                arr.append(ar)

            elif a >= 0.4 and a < 0.8:
                print("heeee")
                ar = [hs, es, es, es, es]
                arr.append(ar)

            elif a >= 0.8 and a < 1.4:
                print("feeee")
                ar = [fs, es, es, es, es]
                arr.append(ar)

            elif a >= 1.4 and a < 1.8:
                print("fheee")
                ar = [fs, hs, es, es, es]
                arr.append(ar)

            elif a >= 1.8 and a < 2.4:
                print("ffeee")
                ar = [fs, fs, es, es, es]
                arr.append(ar)

            elif a >= 2.4 and a < 2.8:
                print("ffhee")
                ar = [fs, fs, hs, es, es]
                arr.append(ar)

            elif a >= 2.8 and a < 3.4:
                print("fffee")
                ar = [fs, fs, fs, es, es]
                arr.append(ar)

            elif a >= 3.4 and a < 3.8:
                print("fffhe")
                ar = [fs, fs, fs, hs, es]
                arr.append(ar)

            elif a >= 3.8 and a < 4.4:
                print("ffffe")
                ar = [fs, fs, fs, fs, es]
                arr.append(ar)

            elif a >= 4.4 and a < 4.8:
                print("ffffh")
                ar = [fs, fs, fs, fs, hs]
                arr.append(ar)

            elif a >= 4.8 and a <= 5.0:
                print("fffff")
                ar = [fs, fs, fs, fs, fs]
                arr.append(ar)
            print(arr)
        return render_template('admin/view_rating.html', resu=res, r1=arr, ln=len(arr))

    else:
        return redirect('/')

# ===============================================================================================================================
#                                             USER MODULE
# =================================================================================================================================


@app.route('/user_home')
def user_home():
    if session['lg']=='lin':

        return render_template('user/user_index.html')

    else:
        return redirect('/')

@app.route('/register',methods=['get','post'])
def register():

        if request.method=="POST":
            n=request.form['t']
            c=request.form['t1']
            e=request.form['t2']
            p=request.form['t3']
            cp=request.form['t4']
            db=Db()
            if p==cp:
                qry1=db.selectOne("select * from login where username='"+e+"'")
                if qry1 is not None:
                    return '''<script>alert('Email Already exist');window.location="/register"</script>'''

                qry=db.insert("insert into login VALUES ('','"+e+"','"+cp+"','user')")
                db.insert("insert into user VALUES ('"+str(qry)+"','"+n+"','"+c+"','"+e+"')")
                return '''<script>alert('success');window.location="/"</script>'''
            else:
                return '''<script>alert('Password mismatch!!');window.location="/register"</script>'''


        else:
            return render_template('user/reg_index.html')

@app.route('/view_profile')
def view_profile():
    if session['lg']=='lin':

        db=Db()
        qry=db.selectOne("select * from `user` where user_id='"+str(session['lid'])+"'")
        return render_template('user/view_profile.html',data=qry)

    else:
        return redirect('/')


@app.route('/send_rating',methods=['get','post'])
def send_rating():
    if session['lg']=='lin':

        if request.method=="POST":
            r=request.form['star']
            db=Db()
            db.insert("insert into rating VALUES ('','"+str(session['lid'])+"','"+r+"',curdate())")
            return '''<script>alert('success');window.location="/user_home"</script>'''

        else:
            return render_template('user/send_rating.html')

    else:
        return redirect('/')

@app.route('/send_complaint',methods=['get','post'])
def send_complaint():
    if session['lg']=='lin':

        if request.method=="POST":
            c=request.form['textarea']
            db=Db()
            db.insert("insert into complaint VALUES ('','"+str(session['lid'])+"',curdate(),'"+c+"','pending','pending')")
            return '''<script>alert('success');window.location="/view_reply#wd"</script>'''

        else:
            return render_template('user/send_complaint.html')

    else:
        return redirect('/')

@app.route('/view_reply')
def view_reply():
    if session['lg']=='lin':

        db=Db()
        qry=db.select("select * from complaint where user_id='"+str(session['lid'])+"'")
        return render_template('user/view_reply.html',data=qry)

    else:
        return redirect('/')


# ============================================================================================================================
#                                             MAIN SECTION
# ============================================================================================================================



@app.route('/upload_file',methods=['get','post'])
def upload_file():
    if session['lg']=='lin':
        if request.method=="POST":
            file=request.files['f']
            db=Db()
            date=datetime.datetime.now().strftime("%y%m%d-%H%M%S")
            file.save(r"C:\Users\IDZ\PycharmProjects\weed_prediction\static\file\\"+date+'.jpg')
            path="/static/file/"+date+'.jpg'
            from classify import abc
            fn=abc(r"C:\Users\IDZ\PycharmProjects\weed_prediction\static\file\\"+date+'.jpg')
            print("result",fn)
            return render_template('user/upload.html',data=fn)
        else:
            return render_template('user/upload.html')
    else:
        return redirect('/')


        # if fn==0:
        #     # print("no")
        #     data = [0]
        #     # db.insert("insert into result VALUES ('','" + str(session['lid']) + "',curdate(),'" + str(path) + "','No disease ')")
        #     return render_template('user/upload_file.html',data=data)
        #
        # else:
        #     # print("yes")
        #     data = [1]
        #     # db.insert("insert into result VALUES ('','" + str(session['lid']) + "',curdate(),'" + str(path) + "','Disease predicted')")
        #     return render_template('user/upload_file.html',data=data)

    # else:
    #     return render_template('')










# --------------------------------------------------------------------------------------------------

@app.route('/logout')
def logout():
    session.clear()
    session['lg']=""
    return redirect('/')

if __name__ == '__main__':
    app.run()
