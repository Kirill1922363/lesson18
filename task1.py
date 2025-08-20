from flask import Flask
import requests
import random
import json

app = Flask(__name__)

@app.route('/breeds-dogs', methods=['GET'])
def get_random_dog_breed():

        response = requests.get('https://dogapi.dog/api/v2/breeds')
        data = response.json()

        breeds_list = data['data']
        random_breed = random.choice(breeds_list)
        
        breed_name = random_breed['attributes']['name']
        breed_description = random_breed['attributes']['description']
        
        result = {
            "breed": breed_name,
            "description": breed_description
        }
        
        response = app.response_class(
            response=json.dumps(result),
            status=200,
            mimetype='application/json'
        )
        return response

if __name__ == "__main__":
    print(app.url_map)  
    app.run(debug=True, port=5050)