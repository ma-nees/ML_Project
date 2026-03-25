# model_training.py
import pandas as pd
import numpy as np
import os
import sys
import json
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings('ignore')

print("="*60)
print("Student Performance Prediction - Model Training")
print("="*60)

# Get the script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(script_dir, 'data', 'student-por.csv')
models_dir = os.path.join(script_dir, 'models')

print(f"\n📁 Dataset path: {dataset_path}")
print(f"📁 Models directory: {models_dir}")

# Check if dataset exists
if not os.path.exists(dataset_path):
    print(f"\n❌ ERROR: Dataset not found at {dataset_path}")
    sys.exit(1)

print("✅ Dataset found!")

# Load dataset with proper CSV handling
print("\n📊 Loading dataset...")
try:
    # Read the file line by line to properly parse the data
    with open(dataset_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split into lines
    lines = content.strip().split('\n')
    
    # First line is header - split by comma
    header_line = lines[0]
    columns = header_line.split(',')
    print(f"   Found {len(columns)} columns")
    
    # Parse data rows - split by comma
    data = []
    for line_num, line in enumerate(lines[1:], start=2):
        if not line.strip():
            continue
        
        # Split by comma
        values = line.split(',')
        
        # Clean values (remove quotes if present)
        cleaned_values = []
        for val in values:
            val = val.strip()
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            cleaned_values.append(val)
        
        # Ensure we have the right number of values
        if len(cleaned_values) == len(columns):
            data.append(cleaned_values)
        else:
            print(f"   Warning: Line {line_num} has {len(cleaned_values)} values, expected {len(columns)}")
    
    # Create DataFrame
    df = pd.DataFrame(data, columns=columns)
    print(f"✅ Dataset loaded successfully!")
    print(f"   Total records: {len(df)}")
    print(f"   Total features: {len(df.columns)}")
    print(f"   Columns: {', '.join(df.columns[:10])}...")
    
except Exception as e:
    print(f"❌ Error loading dataset: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Convert numeric columns to proper types
print("\n🔄 Converting data types...")
numeric_cols = ['age', 'studytime', 'failures', 'absences', 'G1', 'G2', 'G3', 
                'Medu', 'Fedu', 'traveltime', 'famrel', 'freetime', 'goout', 
                'Dalc', 'Walc', 'health']

for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        print(f"   Converted {col} to numeric")

# Fill NaN values with 0
df = df.fillna(0)

# Check if G3 column exists
print(f"\n📋 Available columns: {len(df.columns)} columns")
print(f"   First 10 columns: {df.columns[:10].tolist()}")

if 'G3' not in df.columns:
    print(f"\n❌ ERROR: 'G3' column not found!")
    sys.exit(1)

# Create target variable: Pass (G3 >= 10) else Fail
df['target'] = (df['G3'] >= 10).astype(int)

pass_count = df['target'].sum()
fail_count = len(df) - pass_count
pass_rate = (pass_count / len(df)) * 100

print(f"\n📈 Target Variable Distribution:")
print(f"   Pass (G3 >= 10): {pass_count} students ({pass_rate:.1f}%)")
print(f"   Fail (G3 < 10): {fail_count} students ({100-pass_rate:.1f}%)")

# Define features to use
feature_cols = ['age', 'studytime', 'failures', 'absences', 'G1', 'G2']
print(f"\n🔧 Using features: {feature_cols}")

# Check if all required features exist
missing_features = []
for f in feature_cols:
    if f not in df.columns:
        missing_features.append(f)

if missing_features:
    print(f"❌ ERROR: Missing features: {missing_features}")
    sys.exit(1)

# One-hot encode categorical columns
categorical_cols = ['school', 'sex', 'address', 'famsize', 'Pstatus', 'Mjob', 'Fjob',
                    'reason', 'guardian', 'schoolsup', 'famsup', 'paid', 'activities',
                    'nursery', 'higher', 'internet', 'romantic']

existing_categorical = [col for col in categorical_cols if col in df.columns]
print(f"\n🔄 Encoding categorical variables: {len(existing_categorical)} columns")

# Create a copy for encoding
df_encoded = df.copy()

# One-hot encode categorical columns
if existing_categorical:
    df_encoded = pd.get_dummies(df_encoded, columns=existing_categorical, drop_first=True)
    print(f"   Encoded {len(existing_categorical)} categorical columns")

# Prepare features and target
X = df_encoded.drop(columns=['G3', 'target'])
y = df_encoded['target']

# Keep only numeric columns
X = X.select_dtypes(include=[np.number])
print(f"   Total features after encoding: {X.shape[1]}")

# Save feature columns for later use
feature_columns = X.columns.tolist()
os.makedirs(models_dir, exist_ok=True)
columns_path = os.path.join(models_dir, 'columns.json')
with open(columns_path, 'w') as f:
    json.dump(feature_columns, f)
print(f"\n✅ Saved {len(feature_columns)} feature columns to columns.json")

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"\n📊 Data Split:")
print(f"   Training set: {X_train.shape[0]} samples ({X_train.shape[0]/len(X)*100:.1f}%)")
print(f"   Testing set: {X_test.shape[0]} samples ({X_test.shape[0]/len(X)*100:.1f}%)")

# Scale features
print("\n🔄 Scaling features...")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("   Features scaled successfully")

# Define models with optimized parameters
models = {
    'KNN': KNeighborsClassifier(n_neighbors=5, weights='distance', metric='minkowski'),
    'DecisionTree': DecisionTreeClassifier(random_state=42, max_depth=10, min_samples_split=5),
    'RandomForest': RandomForestClassifier(random_state=42, n_estimators=100, max_depth=10),
    'LogisticRegression': LogisticRegression(random_state=42, max_iter=1000, C=1.0)
}

print("\n" + "="*60)
print("🚀 Training Models")
print("="*60)

# Train and evaluate models
results = {}
trained_models = {}
detailed_reports = {}

for name, model in models.items():
    print(f"\n📌 Training {name}...")
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred)
    results[name] = round(acc, 4)
    trained_models[name] = model
    
    print(f"   ✅ Accuracy: {acc*100:.2f}%")
    
    # Generate classification report as string for display
    print(f"\n   Classification Report:")
    print(classification_report(y_test, y_pred, target_names=['Fail', 'Pass']))
    
    # Store detailed report as dict
    report = classification_report(y_test, y_pred, target_names=['Fail', 'Pass'], output_dict=True)
    detailed_reports[name] = report
    
    # Generate confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    print(f"\n   Confusion Matrix:")
    print(f"   {'':<12} {'Predicted Fail':<15} {'Predicted Pass':<15}")
    print(f"   {'Actual Fail':<12} {cm[0][0]:>15} {cm[0][1]:>15}")
    print(f"   {'Actual Pass':<12} {cm[1][0]:>15} {cm[1][1]:>15}")

# Save all accuracies
accuracy_path = os.path.join(models_dir, 'accuracy.json')
with open(accuracy_path, 'w') as f:
    json.dump(results, f)
print(f"\n✅ Saved accuracy results to accuracy.json")

# Find best model
best_model_name = max(results, key=results.get)
best_model = trained_models[best_model_name]
best_accuracy = results[best_model_name]

print("\n" + "="*60)
print("📊 Model Performance Summary")
print("="*60)
for name, acc in results.items():
    print(f"{name:20} : {acc*100:>6.2f}%")
print("="*60)
print(f"\n🏆 BEST MODEL: {best_model_name} with {best_accuracy*100:.2f}% accuracy")
print("="*60)

# Save best model
model_path = os.path.join(models_dir, 'model.pkl')
joblib.dump(best_model, model_path)
print(f"\n✅ Saved best model to model.pkl")

# Save scaler
scaler_path = os.path.join(models_dir, 'scaler.pkl')
joblib.dump(scaler, scaler_path)
print(f"✅ Saved scaler to scaler.pkl")

# Save model comparison data for frontend
model_comparison = {}
name_mapping = {
    'KNN': 'K-Nearest Neighbors',
    'DecisionTree': 'Decision Tree',
    'RandomForest': 'Random Forest',
    'LogisticRegression': 'Logistic Regression'
}

for name, acc in results.items():
    display_name = name_mapping.get(name, name)
    model_comparison[display_name] = acc

comparison_path = os.path.join(models_dir, 'model_comparison.json')
with open(comparison_path, 'w') as f:
    json.dump(model_comparison, f)
print(f"✅ Saved model comparison data to model_comparison.json")

# Save detailed reports
reports_path = os.path.join(models_dir, 'detailed_reports.json')
with open(reports_path, 'w') as f:
    json.dump(detailed_reports, f, indent=2)
print(f"✅ Saved detailed reports to detailed_reports.json")

# Print feature importance for tree-based models
print("\n" + "="*60)
print("📊 Feature Importance Analysis")
print("="*60)

if hasattr(best_model, 'feature_importances_'):
    importances = best_model.feature_importances_
    indices = np.argsort(importances)[::-1][:10]  # Top 10 features
    
    print(f"\nTop 10 Most Important Features ({best_model_name}):")
    print(f"{'Rank':<6} {'Feature':<30} {'Importance':<15}")
    print("-"*55)
    for i, idx in enumerate(indices, 1):
        if idx < len(feature_columns):
            feature_name = feature_columns[idx]
        else:
            feature_name = f"Feature_{idx}"
        importance = importances[idx] * 100
        print(f"{i:<6} {feature_name:<30} {importance:>11.2f}%")

print("\n" + "="*60)
print("🎉 Training Complete!")
print("="*60)
print("\n✅ All artifacts saved successfully in 'models' directory:")
print("   - model.pkl (Best performing model)")
print("   - scaler.pkl (Feature scaler)")
print("   - columns.json (Feature column names)")
print("   - accuracy.json (All model accuracies)")
print("   - model_comparison.json (Formatted model comparison)")
print("   - detailed_reports.json (Detailed metrics per model)")

print("\n🚀 Next Steps:")
print("   1. Run the Flask app: python app.py")
print("   2. Serve the frontend: cd ../frontend && python -m http.server 8000")
print("   3. Open browser: http://localhost:8000")
print("\n" + "="*60)