'''from flask import Flask, request, render_template
import pickle

# Load the trained models and data
electronics = pickle.load(open('data.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

app = Flask(__name__)

# Recommendation function
def recommender(product_name):
    try:
        # Get the index of the product
        product_index = electronics[electronics['name'] == product_name].index[0]
        # Get the similarity scores for the product
        similar_products = list(enumerate(similarity[product_index]))
        # Sort products based on similarity scores
        similar_products = sorted(similar_products, key=lambda x: x[1], reverse=True)[1:11]
        
        # Retrieve the full information of the top 10 recommended products
        recommended_products = []
        for i in similar_products:
            product_info = electronics.iloc[i[0]]
            recommended_products.append({
                'name': product_info['name'],
                'image': product_info['image'],
                'link': product_info['link'],
                'discount_price': product_info['discount_price'],
                'actual_price': product_info['actual_price'],
                'ratings': product_info['ratings'],
                'no_of_ratings': product_info['no_of_ratings']
            })
        return recommended_products
    except IndexError:
        return []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    product_name = request.form['product_name']
    recommendations = recommender(product_name)
    return render_template('result.html', product_name=product_name, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)

'''
from flask import Flask, request, render_template
import pickle
from fuzzywuzzy import process

# Load the trained models and data
electronics = pickle.load(open('data.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

app = Flask(__name__)

# Recommendation function using fuzzy matching
def recommender(product_name):
    try:
        # Use fuzzy matching to find the closest product name
        all_product_names = electronics['name'].tolist()
        closest_match = process.extractOne(product_name, all_product_names)
        
        if closest_match:
            matched_product_name = closest_match[0]
            # Get the index of the product
            product_index = electronics[electronics['name'] == matched_product_name].index[0]
            # Get the similarity scores for the product
            similar_products = list(enumerate(similarity[product_index]))
            # Sort products based on similarity scores
            similar_products = sorted(similar_products, key=lambda x: x[1], reverse=True)[1:11]
            
            # Retrieve the full information of the top 10 recommended products
            recommended_products = []
            for i in similar_products:
                product_info = electronics.iloc[i[0]]
                recommended_products.append({
                    'name': product_info['name'],
                    'image': product_info['image'],
                    'link': product_info['link'],
                    'discount_price': product_info['discount_price'],
                    'actual_price': product_info['actual_price'],
                    'ratings': product_info['ratings'],
                    'no_of_ratings': product_info['no_of_ratings']
                })
            return recommended_products, matched_product_name
        else:
            return [], None
    except IndexError:
        return [], None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    product_name = request.form['product_name']
    recommendations, matched_product_name = recommender(product_name)
    
    if matched_product_name:
        return render_template('result.html', product_name=matched_product_name, recommendations=recommendations)
    else:
        return render_template('result.html', product_name=product_name, recommendations=[], error="Product not found")

if __name__ == '__main__':
    app.run(debug=True)

# similarity.pkl is 703.13 MB; this exceeds GitHub's file size limit of 100.00 MB
