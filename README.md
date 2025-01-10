Image Forensics Using Steganography
Overview
This project demonstrates an Image Forensics System built using Flask, which analyzes images for hidden information using Steganographic techniques. It provides a web interface for uploading images and analyzing their Least Significant Bits (LSB), intensity histograms, and pixel intensity distributions. The system uses tools like OpenCV and Matplotlib for image manipulation and data visualization.

Features
Image Analysis
Image Upload: Allows users to upload .png, .jpg, .jpeg, and .gif files for analysis.
LSB Extraction: Extracts the Least Significant Bits (LSB) from the uploaded image to identify potential hidden data.
Image Intensity Histogram: Generates a histogram that represents the pixel intensity distribution of the image.
Pixel Intensity Graph: Visualizes pixel intensity values in a graph for a better understanding of image properties.
Security and Data Handling
File Validation: Ensures uploaded files are of the correct type and below a specified size (e.g., 5 MB).
Storage Location: Uploads and results are stored in non-public directories to prevent unauthorized access.
Downloadable Results: After analysis, users can download the results, which include:
LSB image.
Intensity graph.
Intensity histogram.
User-Friendly Interface
Web Interface: A simple frontend (index.html) for uploading images and viewing analysis results.
JSON Responses: Provides error or success messages in JSON format for ease of integration and feedback.
Endpoints
/
Renders the homepage where users can upload images for analysis.

/upload
Handles image uploads via POST requests and returns success or error messages in JSON format.

/analysis_results
Displays the results of the image analysis, including:

LSB Image.
Pixel intensity graph.
Image intensity histogram.
Download links for results.
Technologies Used
Flask: Backend framework for handling HTTP requests and rendering templates.
OpenCV: Library used for image manipulation and extraction of LSB.
Matplotlib: Tool for generating pixel intensity graphs and histograms.
Werkzeug: Provides secure handling of file uploads.
Setup Instructions
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/Image-Forensics-Using-Steganography.git
cd Image-Forensics-Using-Steganography
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Application:

bash
Copy code
python app.py
Access the Web Interface: Open your browser and go to http://127.0.0.1:5000/ to start using the app.

Directory Structure
php
Copy code
image-forensics-using-steganography/
|
├── app.py                 # Main Flask application
├── uploads/               # Directory for storing uploaded images
├── results/               # Directory for storing analysis results (LSB images, histograms, etc.)
├── templates/             # HTML templates for the web interface
|    └── index.html        # Frontend template for uploading images
├── static/                # Directory for static assets (e.g., CSS, JavaScript)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
Future Enhancements
Integration with Steganography Tools: Enhance the system by adding more advanced steganographic techniques for data extraction.
Real-Time Analysis: Allow real-time image analysis with live feedback.
Advanced Image Processing: Implement additional image manipulation and forensics tools for further analysis.
Cloud Storage: Enable the ability to store and retrieve uploaded images from cloud storage platforms like AWS S3 or Google Cloud Storage.
Contribution
Contributions are welcome! Feel free to fork this repository, create a branch, and submit a pull request with your improvements or new features.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Flask Documentation: For guidance on creating secure and efficient web applications.
OpenCV: For image manipulation and Steganographic analysis.
Matplotlib: For generating graphs and visualizing data.
Open-Source Community: For inspiration and tools to build secure and efficient web applications.
