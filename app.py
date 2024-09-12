from flask import Flask, render_template, request, redirect, url_for
import random
from pinterest_api import fetch_images

# Create an instance of the Flask class
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    # Render the home page template
    return render_template('home.html')

# Global cache variables
geometric_images_cache = []
floral_images_cache = []

# Fetches images from cache or API.
def get_images(query_type):

    global geometric_images_cache, floral_images_cache
    
    if query_type == 'geometric':
        if not geometric_images_cache:
            geometric_images_cache = fetch_images(query_type)
        return geometric_images_cache
    
    elif query_type == 'floral':
        if not floral_images_cache:
            floral_images_cache = fetch_images(query_type)
        return floral_images_cache
    
# Define the route for displaying the result
@app.route('/result', methods=['POST'])
def result():
    # Get the selected design preference and hand orientation from the form
    preference = request.form['preference']
  
    # Fetch images from Pinterest based on the selected preferences
    images = get_images(preference)
    if not images:
        return "No images found for the selected preference and hand.", 404
    # Randomly select one image from the fetched images
    selected_image = random.choice(images)
    # Render the result page template, passing the selected image and preferences
    return render_template('result.html', image=selected_image, preference=preference)

# Define the route for starting over the selection process
@app.route('/start_over')
def start_over():
    # Redirect to the home page to start the selection process again
    return redirect(url_for('home'))

# Check if the script is run directly (not imported), and if so, start the Flask development server
if __name__ == '__main__':
    app.run(debug=True)

