from flask import(
    Flask,redirect,render_template,url_for,request
)
import os
import pyqrcode
app = Flask(__name__,static_url_path="")
app.config["SEND_FILE_MAX_AGE_DEFAULT"]=0
app.secret_key="msayak1269"

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/view",methods=["POST","GET"])
def view():
    if request.method=="POST":
        url=request.form.get("url")
        qrcode = pyqrcode.create(url)
        imgName = f"{APP_ROOT}/static/qrcode.png"
        qrcode.png(imgName,scale=7)
        return redirect(url_for("view"))
    else:    
        return render_template("view.html")



if __name__== "__main__":
    app.run(port=5001,debug=True,host='0.0.0.0')