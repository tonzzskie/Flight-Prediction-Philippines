### **Flight Prediction Philippines**  

A machine learning project designed to predict flight outcomes in the Philippines, such as delays or scheduling impacts. The project provides tools for data exploration, model training, and deployment using a simple Flask web application.  

---

### **Features:**  
- Jupyter Notebook for training and evaluating your custom flight prediction model  
- Pre-processing scripts for data preparation  
- Pre-trained model saved as `c1_flight_rf.pkl` for immediate predictions  
- Flask-based deployment (`app.py`) for serving predictions via a web interface  

---

### **Getting Started**  

#### **Step 1: Clone the Repository**  
```bash  
git clone https://github.com/tonzzskie/Flight-Prediction-Philippines.git
cd Flight-Prediction-Philippines  
```  

#### **Step 2: Install Requirements**  
Ensure you have Python installed. Install the required libraries by running:  
```bash  
pip install -r requirements.txt  
```  

#### **Step 3: Train Your Own Model (Optional)**  
Open the Jupyter Notebook provided for model training and evaluation:  
```bash  
jupyter notebook flight_prediction_training.ipynb  
```  

#### **Step 4: Deploy the Web Application**  
Run the Flask application to serve predictions:  
```bash  
python app.py  
```  

The app will be available at `http://127.0.0.1:5000/`.  

#### **Step 5: Use Pre-Trained Model**  
The pre-trained model is saved as `c1_flight_rf.pkl`. You can load it directly in the app or for testing via a Python script:

```python  
import pickle  

with open('flight_model.pkl', 'rb') as file:  
    model = pickle.load(file)  

# Example usage  
sample_input = [/* your input features */]  
prediction = model.predict([sample_input])  
print("Prediction:", prediction)  
```  

---

### **License**  
This project is licensed under the [MIT License](LICENSE).  

---

### **Contributions**  
Suggestions, issues, and pull requests are welcome to improve this project further!
