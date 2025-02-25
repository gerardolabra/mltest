# Machine Learning Project

## Project Overview
This project demonstrates a machine learning pipeline for predicting student performance based on various features. The pipeline includes data ingestion, data transformation, model training, and prediction.

### Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Contributing](#contributing)
5. [License](#license)

## Installation Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/gerardolabra/mltest.git

2. Navigate to the project directory:
cd mltest

3. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

4. Install the required dependencies:
pip install -r requirements.txt

## Usage
1. Run the data ingestion script:
python src/components/data_ingestion.py

2. Run the Flask application:
python app.py

3. Access the application in your web browser at
http://127.0.0.1:5000

## Features
Data Ingestion: Reads the dataset and splits it into training and testing sets.
Data Transformation: Preprocesses the data, including scaling and encoding.
Model Training: Trains multiple machine learning models and selects the best one based on performance.
Prediction: Uses the trained model to make predictions on new data.

## Results
flask1.png
flask2.png


## Model Performance

Model	R2 Score
Random Forest	0.85
Decision Tree	0.78
Gradient Boosting	0.88
Linear Regression	0.75
K-Neighbors Regressor	0.70
XGBRegressor	0.87
CatBoosting Regressor	0.86
AdaBoost Regressor	0.80

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

## Project Structure
mltest/
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   ├── pipeline/
│   │   ├── predict_pipeline.py
│   │   ├── train_pipeline.py
│   ├── utils.py
│   ├── logger.py
│   ├── exception.py
├── templates/
│   ├── index.html
│   ├── home.html
├── static/
│   ├── css/
│   ├── js/
├── artifacts/
├── logs/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore

## Contact
For any questions or inquiries, please contact gerardolabraoliva@gmail.com

