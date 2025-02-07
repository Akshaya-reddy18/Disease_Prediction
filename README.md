# Disease Prediction Model<br>
<br>
# Disease Prediction System  
<br>  
This system is designed to predict the likelihood of four types of diseases: **Diabetes**, **Heart Disease**, **Parkinson's Disease**, and **PCOS (Polycystic Ovary Syndrome)**.  
<br>  
The system is built using raw data provided by the organization, which is used to train machine learning models. These models are then utilized to predict the occurrence of diseases based on user inputs.  
<br>  
To get accurate predictions, users must provide precise input values corresponding to their test results. The system leverages popular Python libraries such as **NumPy**, **Pandas**, and **Scikit-learn** to process data and generate predictions.  
<br>  
The following modules and their respective versions are used to run the prediction system:  
<br>  
<pre>  
      numpy - 1.26.4  
      pandas - 2.2.3  
      pickle - 0.7.5  
      sklearn - 1.6.1  
      streamlit - 1.37.1  
      streamlit_option_menu - 0.4.0  
</pre>  
<br>  
The main file to execute the prediction module is **`web.py`**. The trained machine learning models are stored in the **`MODELS`** folder, while the data preprocessing and feeding logic are handled by files located in the **`MODULES`** folder.  
<br>  
This system provides an intuitive and user-friendly interface for disease prediction, making it accessible for both medical professionals and individuals seeking health insights.
