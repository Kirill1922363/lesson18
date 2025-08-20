from flask import Flask, request,render_template
import urllib.parse


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_code_url = None
    user_text = "" 
    if request.method == 'POST':
        user_text = request.form.get('text', '')
        if user_text.strip():
            encoded_text = urllib.parse.quote(user_text)
            qr_code_url = f"https://api.qrserver.com/v1/create-qr-code/?size=200x200&data={encoded_text}"
    
    return render_template('index.html', qr_code_url=qr_code_url, user_text=user_text)

if __name__ == '__main__':
    app.run(debug=True)