from flask import Flask,request
import requests
import json

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '测试成功！'


@app.route('/message',methods = ['POST'])
def mess():
    sk = request.json.get('openaikey')
    msg = request.json.get('msg')
    maxtoken = request.json.get('maxtoken')
    print(sk,msg)
    req = requests.post('https://api.openai.com/v1/completions',
                        json={"prompt": msg, "max_tokens": maxtoken, "model": "text-davinci-003","temperature": 0}, headers={
            'content-type': 'application/json', 'Authorization': 'Bearer ' + sk})
    print(req.status_code)
   
    if req.status_code == 200:

        reqdic = json.loads(req.text)
        print(reqdic)
        # aa = reqdic['choices'][0]['text']
        res = {
            "resmsg":reqdic,
            "code":200
        }
        return res
    else:
        reqdic = json.loads(req.text)
        err = reqdic['error']['message']
        res = {
            "resmsg":err,
            "code":412
        }
        return res


if __name__ == '__main__':
    app.run('127.0.0.1', port=80)
