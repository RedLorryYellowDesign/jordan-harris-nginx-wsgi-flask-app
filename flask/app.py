from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello World!"

@app.route('/jinja2test')
def jinja2test():
    return render_template('index.html')

@app.route('/cache-me')
def cache():
	return "nginx will cache this response"

@app.route('/info')
def info():

	resp = {
		'connecting_ip': request.headers['X-Real-IP'],
		'proxy_ip': request.headers['X-Forwarded-For'],
		'host': request.headers['Host'],
		'user-agent': request.headers['User-Agent']
	}

	return jsonify(resp)

@app.route('/flask-health-check')
def flask_health_check():
	return "success"
