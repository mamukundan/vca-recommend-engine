import flask
import pandas as pd
from flask import jsonify , request , render_template
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    	return render_template('index.html')

@app.route('/products', methods=['GET'])
def products():
	df = pd.read_csv('C:\\Users\\lenovo\\Downloads\\concern-product.csv', encoding = 'cp1252')
	df_prod = pd.read_csv('C:\\Users\\lenovo\\Downloads\\product_master.csv', encoding = 'cp1252')
	df = df.drop('All', axis=1)
	concern = request.args.get('concern')
	max = int(request.args.get('max'))
	r = df.iloc[df.index[df['SNOMEDTerm'] == concern]]
	s = r.iloc[0]
	s = s.drop('SNOMEDTerm')
	result = s.sort_values(ascending=False)[0:50]
	d = result.to_dict()
	results = []
	for k,v in d.items():
		res = df_prod.loc[df_prod['InvoiceItemId'] == int(k)]
		if (res.empty == False and len(results) < max):
			data = {}
			data['snomedid'] = k
			data['name'] = res['Name'].to_string(index=False)
			data['count'] = int(v)
			results.append(data)
	response_json = json.dumps(results)
	return response_json



app.run()