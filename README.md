# Gold Price Prediction

A machine learning project that predicts gold prices using economic indicators. This project includes exploratory data analysis, model training, and a Streamlit web application for making predictions.

## 📋 Project Overview

This project predicts gold prices (GLD) based on key economic indicators using multiple machine learning algorithms. The analysis uses historical data from two time periods (2008-2018 and 2015-2025) to build and evaluate predictive models.

## 📁 Project Structure

```
Gold-price-prediction/
├── app.py                                    # Streamlit web application
├── Gold price prediction.ipynb               # Main analysis and model training notebook
├── Gold price prediction DS 2008-18.ipynb    # Data analysis for 2008-2018 period
├── Gold price prediction DS 2015-25.ipynb    # Data analysis for 2015-2025 period
├── RandomeForest.joblib                      # Trained RandomForest model (serialized)
├── combined_df.csv                           # Combined dataset for modeling
├── gold_model_dataset_2008_2018.csv          # Historical data 2008-2018
├── gold_model_dataset_2015_2025.csv          # Historical data 2015-2025
└── README.md                                 # This file
```

## 🎯 Features & Input Variables

The model uses the following economic indicators to predict gold prices:

| Feature | Description | Source |
|---------|-------------|--------|
| **SPX** | S&P 500 Index | Stock market index |
| **USO** | United States Oil | Crude oil price |
| **SLV** | Silver Price | Silver commodity price |
| **EUR/USD** | Euro to US Dollar Exchange Rate | Currency exchange rate |
| **GLD** | Gold Price (Target) | Gold commodity price (prediction target) |

## 📊 Dataset Information

### Data Characteristics
- **Total Records**: 2,290 rows
- **Missing Values**: None (clean dataset)
- **Time Periods Covered**: 
  - 2008-2018 (Dataset 1)
  - 2015-2025 (Dataset 2)

### Data Features
- Date range spanning multiple economic cycles
- No null values detected
- All numeric features
- Ready for machine learning pipeline

## 🤖 Models Tested

The project evaluates multiple machine learning algorithms:

1. **Random Forest Regressor** ✅ (Deployed Model)
   - Ensemble method using multiple decision trees
   - Currently used in production
   - Captures non-linear relationships

2. **Linear Regression**
   - Baseline model for comparison
   - Assumes linear relationships between features and target

3. **Decision Tree Regressor**
   - Tree-based approach
   - Prone to overfitting

4. **XGBoost Regressor**
   - Gradient boosting implementation
   - Advanced ensemble technique

### Model Evaluation Metric
- **R² Score**: Used to evaluate model performance (higher is better)

## 🚀 Deployment: Streamlit Web App

An interactive web application is provided for making real-time predictions.

### Running the App

```bash
streamlit run app.py
```

### App Features
- Interactive input fields for economic indicators:
  - S&P 500 Index
  - United States Oil price
  - Silver Price
  - EUR/USD Exchange Rate
- Real-time gold price prediction
- Display of input features used for prediction
- User-friendly interface

### Example Prediction
```
Input:
- S&P 500: 1000.0
- USO: 50.0
- SLV: 20.0
- EUR/USD: 1.1

Output: The predicted Gold Price is: $[predicted_value]
```

## 📚 Notebooks Overview

### 1. **Gold price prediction.ipynb** (Main Notebook)
Main analysis notebook containing:
- Data loading and preprocessing
- Exploratory Data Analysis (EDA)
- Data visualization (distributions, correlations, time series)
- Feature engineering
- Data splitting (80% train, 20% test)
- Model training and evaluation
- Comparison of multiple algorithms
- Model serialization

**Key Steps**:
- Data concatenation from two sources
- Missing value handling
- USO feature scaling (multiplied by 8)
- Correlation analysis with GLD
- R² score calculation for model comparison

### 2. **Gold price prediction DS 2008-18.ipynb**
Detailed analysis for the 2008-2018 dataset:
- Dataset shape and structure analysis
- Statistical summaries (mean, median, std, min, max)
- Data quality checks
- Visualizations for 2008-2018 period data

### 3. **Gold price prediction DS 2015-25.ipynb**
Detailed analysis for the 2015-2025 dataset:
- Dataset shape and structure analysis
- Statistical summaries for recent data
- Data quality verification
- Visualizations for 2015-2025 period data

## 🛠️ Technology Stack

- **Python 3.x**
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **scikit-learn** - Machine learning algorithms
  - RandomForestRegressor
  - LinearRegression
  - DecisionTreeRegressor
  - train_test_split
  - metrics (R² score)
- **xgboost** - Gradient boosting
- **matplotlib** - Data visualization
- **seaborn** - Statistical data visualization
- **joblib** - Model serialization
- **Streamlit** - Web application framework

## 📦 Installation & Setup

### Requirements
Create a Python environment and install dependencies:

```bash
pip install pandas numpy scikit-learn xgboost matplotlib seaborn joblib streamlit
```

### Alternative with requirements.txt
If a `requirements.txt` exists:
```bash
pip install -r requirements.txt
```

## 🔄 Workflow

1. **Data Collection**: Historical gold prices and economic indicators
2. **Data Preprocessing**: Cleaning, handling missing values, feature scaling
3. **Exploratory Analysis**: Understanding data distributions and relationships
4. **Model Training**: Training multiple ML algorithms on 80% of data
5. **Model Evaluation**: Testing on 20% of data using R² score
6. **Model Selection**: RandomForest selected as best performing model
7. **Deployment**: Exported to `RandomeForest.joblib` for use in web app

## 📈 Data Analysis Highlights

- **EDA Components**:
  - Distribution analysis of each variable
  - Correlation matrix between features
  - Time series visualization
  - Statistical summaries (mean, median, standard deviation, min, max)

- **Feature Relationships**:
  - Analysis of how economic indicators correlate with gold prices
  - Identification of influential features for prediction

## 💾 Model Artifacts

- **RandomeForest.joblib**: Serialized trained Random Forest model
  - Ready for production use
  - Can be loaded with: `joblib.load('RandomeForest.joblib')`

- **combined_df.csv**: Processed and combined dataset
  - Used for training
  - Contains all features and target variable
  - Dimensions: 2,290 rows × 6 columns (Date, SPX, GLD, USO, SLV, EUR/USD)

## 🎓 Learning Outcomes

This project demonstrates:
- End-to-end machine learning workflow
- Data preprocessing and EDA techniques
- Comparison of multiple ML algorithms
- Model evaluation and selection
- Model deployment and serialization
- Building interactive web applications with Streamlit
- Working with time series financial data

## 📝 Usage Examples

### Making Predictions with Trained Model

```python
import joblib
import pandas as pd

# Load the model
model = joblib.load('RandomeForest.joblib')

# Prepare input data
features = {
    'SPX': 1416.25,
    'USO': 594.0,
    'SLV': 16.28,
    'EUR/USD': 1.4869
}

input_data = pd.DataFrame([features])

# Make prediction
prediction = model.predict(input_data)
print(f"Predicted Gold Price: ${prediction[0]:.2f}")
```

### Running the Streamlit App

```bash
cd path/to/Gold-price-prediction
streamlit run app.py
```

Then open your browser to `http://localhost:8501`

## 📊 Performance Metrics

The models are evaluated using R² (coefficient of determination) score:
- Ranges from -∞ to 1
- Higher values indicate better fit
- 1.0 = perfect predictions
- 0.0 = model predicts mean value
- Negative = worse than mean prediction

## 🔮 Future Improvements

- Incorporate additional economic indicators
- Implement LSTM/time series models for temporal patterns
- Add model confidence intervals
- Cross-validation for robust evaluation
- Hyperparameter tuning for each model
- Real-time data integration from APIs
- Model retraining pipeline

## 📝 Notes

- Data preprocessing includes scaling of USO feature (multiplied by 8) for normalization
- Models trained on 80% of data, evaluated on 20%
- Random state set to 2 for reproducibility
- All datasets have been verified for data quality (no null values)

## 👨‍💻 Author
Self Study Project

## 📄 License
This project is for educational purposes.

---

**Last Updated**: May 2026
