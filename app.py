from flask import Flask, render_template, request
from hugchat.login import Login
from  hugchat  import hugchat

app = Flask(__name__)

sign = Login("shivanshkumar752@gmail.com", "James.bond.990")
cookies = sign.login()

cookie_path_dir = "./cookies_snapshot"
sign.saveCookiesToDir(cookie_path_dir)

output=[]
query_result=''
@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        query = request.form.get('query')
          
        chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
        query_result = str(chatbot.query(query))

        output.append([query])
        output.append([query_result])

        return render_template('index.html', output=output)
    # " ".join(output)    
    return render_template('index.html')

@app.route('/deletechat')
def deletechat():
    output.clear()
    
    return render_template('index.html', output=output)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)    
