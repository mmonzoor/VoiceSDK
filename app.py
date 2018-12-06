from flask import Flask, Response, request
import json

app = Flask(__name__)

# @app.route('/', methods = ['POST'])
# def root():
# 	return 'Hello, World!'

@app.route('/test', methods = ['GET','POST'])
def test():
	r = request.get_json()
	print(r)
	report = {"version": "1.0", "response": {"outputSpeech": {"type": "SSML","ssml": "<speak>" + "You asked for Escherichia Coli" + "</speak>"},"shouldEndSession": False}}
	resp = json.dumps(report)
	print(json.dumps(report))
	response = Response(resp, mimetype='application/json')
	#response.status_code = 200
	return response
	#return 'You tester you'

app.run(debug=True)
# if __name__ == '__main__':

#     app.run(debug=True)

# drill out the request information
