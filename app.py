import numpy as np
import pandas as pd
import os
import tensorflow as tf
from flask import Flask,app,request,render_template
from keras.models import Model
from keras.preprocessing import image
from tensorflow.python.ops.gen_array_ops import Concat
from keras.models import load_model
from PIL import Image

model = load_model('C:/Users/kudut/OneDrive/Desktop/Major Project/models/plants_91.33fruitsveg.h5')

# Initialize the Flask app
app = Flask(__name__)

# Route for the homepage (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Route for the about page (about.html)
@app.route('/about.html')
def about():
    return render_template('about.html')

# Route for the contact page (contact.html)
@app.route('/contact.html')
def contact():
    return render_template('contact.html')

# Route for the gallery page (gallery.html)
@app.route('/gallery.html')
def gallery():
    return render_template('gallery.html')

# Route for a single gallery item (gallery-single.html)
@app.route('/gallery-single.html')
def gallery_single():
    return render_template('gallery-single.html')

# Route for the prediction page (predict.html)
@app.route('/predict.html', methods=['GET', 'POST'])
def predict():
    result = ''
    image_path = ''
    if request.method == "POST":
        # Get the uploaded image file
        f = request.files['image']
        
        # Get the path where the file will be saved
        basepath = os.path.dirname(__file__)  # Getting the current path where app.py is present
        filepath = os.path.join(basepath, './/static//uploads', f.filename)  # Path to save the uploaded image
        f.save(filepath)

        # Load and process the image
        img = tf.keras.utils.load_img(filepath, target_size=(200, 260))  # Resize image
        x = tf.keras.utils.img_to_array(img)  # Convert image to numpy array
        x = np.expand_dims(x, axis=0)  # Expand dimensions to match the model's input
        

        # Predict the class of the image
        prediction = np.argmax(model.predict(x), axis=1)

        # List of class labels (fruit/vegetable names)
        op = ['aloevera', 'banana', 'bilimbi', 'cantaloupe', 'cassava', 'coconut', 'corn',
            'cucumber', 'curcuma', 'eggplant', 'galangal', 'ginger', 'guava', 'kale',
            'longbeans', 'mango', 'melon', 'orange', 'paddy', 'papaya', 'peper chili',
            'pineapple', 'pomelo', 'shallot', 'soybeans', 'spinach', 'sweet potatoes',
            'tobacco', 'waterapple', 'watermelon']
        
        # Get the result from the prediction list
        result = op[prediction[0]]
        print(result)

        image_path = 'uploads/' + f.filename
        img = Image.open(f)
        
        # Resize the image to a desired size (example: 200x260)
        img = img.resize((100, 100), Image.Resampling.LANCZOS)


        
        # Return the result to the predict page
    return render_template('predict.html', prediction=result,image_path=image_path)

if __name__ == '__main__':
    app.run(debug=True)