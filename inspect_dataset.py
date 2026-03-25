import pandas as pd 
import os 
 
print("="*60) 
print("Dataset Inspection") 
print("="*60) 
 
dataset_path = 'data/student-por.csv' 
 
separators = [';', ',', '\t'] 
 
for sep in separators: 
    try: 
        print(f"\nTrying separator: '{sep}'") 
        df = pd.read_csv(dataset_path, sep=sep, nrows=5) 
        print(f"  Shape: {df.shape}") 
        print(f"  Columns: {df.columns.tolist()}") 
        print(f"  First row: {df.iloc[0].tolist()}") 
        if 'G3' in df.columns: 
            print(f"  ✅ Found G3 column!") 
            print(f"  G3 values: {df['G3'].tolist()}") 
        break 
    except Exception as e: 
        print(f"  Error: {e}") 
