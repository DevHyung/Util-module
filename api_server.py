from flask import Flask,request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/user/<userName>')  # URL뒤에 <>을 이용해 가변 경로를 적는다
def hello_user(userName):
    return 'Hello, %s' % (userName)

@app.route('/convert', methods=['POST'])
def post():
    content = request.form['content']
    return 'Hello, %s' % (content)

if __name__ == "__main__":
    app.run()
    """
    import requests

    datas = {'content':"안녕 나는 박형준이야   . . . . . / ]\ / ]\  "}
    html = requests.post("http://127.0.0.1:5000/convert",data=datas)
    print(html.text)
    """