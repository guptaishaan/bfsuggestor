import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Step 1: Data Collection
# Load the dataset (assuming the dataset is in the same directory)
data = pd.read_csv('farming_scenarios.csv')

# Step 2: Data Preprocessing
# Convert categorical variables to numerical representations
label_encoders = {}
for column in ['geography', 'resources', 'flood_risk', 'soil_type']:
    label_encoders[column] = LabelEncoder()
    data[column] = label_encoders[column].fit_transform(data[column])

# Split the data into features and target variable
X = data[['geography', 'resources', 'flood_risk', 'soil_type']]
y = data['recommendations']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Model Training
# Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 4: Model Inference
# Evaluate the model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Function to make recommendations
def get_recommendations(geography, resources, flood_risk, soil_type):
    # Convert input scenario to numerical values
    input_data = {
        'geography': [label_encoders['geography'].transform([geography])[0]],
        'resources': [label_encoders['resources'].transform([resources])[0]],
        'flood_risk': [label_encoders['flood_risk'].transform([flood_risk])[0]],
        'soil_type': [label_encoders['soil_type'].transform([soil_type])[0]]
    }
    input_df = pd.DataFrame(input_data)
    
    # Predict recommendations
    recommendation = model.predict(input_df)
    return recommendation[0]

# Example usage
geography = "Northern Burkina Faso, semi-arid region"
resources = "Limited access to machinery, primarily manual labor available, access to basic tools (shovels, hoes)"
flood_risk = "Low flood risk, but prone to dry spells and occasional heavy rains"
soil_type = "Sandy soil with low fertility"

recommendation = get_recommendations(geography, resources, flood_risk, soil_type)
print(f"Recommended action: {recommendation}")
