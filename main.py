# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    kayra=request.form.get("button_discord")
    ruhsar=request.form.get("button_html")
    info=request.form.get("button_db")
    email=request.form.get("email")
    text=request.form.get("text")
    
    if email:  #y varsa demek. y is not none da kullanabilirdin aynı şey
        with open("yazi.txt", "a", encoding="UTF-8" ) as q:
            q.write("email")
            q.write("text")
    return render_template('index.html', button_python=button_python, kayra=kayra, ruhsar=ruhsar, info=info, email=email, text=text)


if __name__ == "__main__":
    app.run(debug=True)
