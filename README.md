# Option Predictor Pro

## Description
This project predicts the opening price of Bank Nifty option derivatives using machine learning techniques. It leverages historical data such as Bank Nifty's previous closing price, current opening price, and the previous closing price of specific strike prices.

## Technology Stack
The model is implemented in Python, utilizing the following libraries:
- FastAPI
- Streamlit
- Matplotlib
- Seaborn
- Sci-kit learn (sklearn)

The algorithm employed is **RandomForestRegressor** from Sci-kit learn.

## Source Data
The data used to train the model is sourced directly from the National Stock Exchange (NSE) of India. The dataset covers the period from February 23, 2019, to February 15, 2021, using actual real-world data for training purposes.

## Purpose
This tool is designed to assist traders of Index Derivatives like BankNifty and Nifty by providing predictions of derivative opening prices based on historical data. It aims to facilitate informed trading decisions by predicting market trends.

## Developer
- **Developer:** Akshay Soni

## Deployment Instructions
To deploy this application in your environment, follow the steps below:

1. **Clone the Repository**

```commandline
git clone https://github.com/imakshaysoni/Option-Predictor-Pro
```


2. **Install Dependencies**
```commandline
pip install -r requirements.txt
```


3. **Run the Application**
```commandline
uvicorn app:app
streamlit run frontend/streamlit_app.py
```


4. **Access the Application**
Open your web browser and navigate to `http://localhost:5000` (or the specified port).

5. **Usage**
- Input the required parameters such as Bank Nifty's previous closing price, current opening price, and specific strike prices.
- Click on "Predict" to obtain the predicted opening price of the Bank Nifty option derivative.

6. **Further Development**
- Modify `app.py` to include additional features or enhance prediction accuracy.
- Explore different machine learning algorithms or adjust model parameters for better performance.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Feedback
Your feedback is greatly appreciated. If you encounter any issues or have suggestions for improvement, please [submit an issue](https://github.com/your-repo/issues).
