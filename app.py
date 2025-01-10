from flask import Flask, request, jsonify, send_from_directory, render_template
from werkzeug.utils import secure_filename
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
RESULTS_FOLDER = 'results'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULTS_FOLDER'] = RESULTS_FOLDER

# Serve HTML interface
@app.route('/')
def index():
    return render_template('index.html')

# Helper to save plots
def save_plot(fig, filename):
    fig.savefig(filename)
    plt.close(fig)

# Upload and process images
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['image']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Perform analysis
        original_image = cv2.imread(file_path, cv2.IMREAD_COLOR)
        if original_image is None:
            return jsonify({"error": "Invalid image file"}), 400

        # Convert to grayscale
        gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

        # Perform LSB Analysis
        lsb_image = gray_image & 1
        lsb_image_path = os.path.join(app.config['RESULTS_FOLDER'], f"lsb_{filename}")
        cv2.imwrite(lsb_image_path, lsb_image * 255)

        # Generate LSB Pixel Intensity Graph
        lsb_flat = lsb_image.flatten()
        fig, ax = plt.subplots()
        ax.hist(lsb_flat, bins=2, color='blue', edgecolor='black', alpha=0.7)
        ax.set_title('LSB Pixel Intensity Distribution')
        ax.set_xlabel('Pixel Intensity')
        ax.set_ylabel('Frequency')

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        analysis_dir = os.path.join(app.config['RESULTS_FOLDER'], f"analysis_{timestamp}")
        os.makedirs(analysis_dir, exist_ok=True)

        graph_path = os.path.join(analysis_dir, "lsb_graph.png")
        save_plot(fig, graph_path)

        # Generate Intensity Histogram
        fig, ax = plt.subplots()
        ax.hist(gray_image.ravel(), bins=256, color='orange', edgecolor='black', alpha=0.7)
        ax.set_title('Image Intensity Histogram')
        ax.set_xlabel('Intensity Value')
        ax.set_ylabel('Frequency')

        histogram_path = os.path.join(analysis_dir, "histogram.png")
        save_plot(fig, histogram_path)

        # Save original and LSB images in analysis folder
        original_image_path = os.path.join(analysis_dir, filename)
        cv2.imwrite(original_image_path, original_image)

        lsb_image_output_path = os.path.join(analysis_dir, f"lsb_{filename}")
        cv2.imwrite(lsb_image_output_path, lsb_image * 255)

        return jsonify({
            "original_image": f"/{original_image_path}",
            "lsb_image": f"/{lsb_image_output_path}",
            "lsb_graph": f"/{graph_path}",
            "histogram": f"/{histogram_path}",
            "analysis_folder": analysis_dir
        })

# Serve static files
@app.route('/results/<path:filename>')
def serve_results(filename):
    return send_from_directory(app.config['RESULTS_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
