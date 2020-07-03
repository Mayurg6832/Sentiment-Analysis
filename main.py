from flask import Flask,render_template,request
import pickle
import requests


app = Flask(__name__)
model = pickle.load(open('model_pickle','rb'))
vectorizer = pickle.load(open('vectorizer','rb'))

@app.route('/',methods=['GET'])

def Home():
	return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
	if request.method == 'POST':
		review = str(request.form['review'])
		print(review)
		val = model.predict(vectorizer.transform([review]))
		if val[0] == 0:
			return render_template('index.html',prediction_text="User liked it 😍")
		else:
			return render_template('index.html',prediction_text="User Did't'like it 😔")
	else:
		return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)