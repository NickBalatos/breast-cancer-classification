import pandas as pd

# Ορισμός των ονομάτων των στηλών
column_names = [
    "ID", "Diagnosis",  
    "Radius1", "Texture1", "Perimeter1", "Area1", "Smoothness1", "Compactness1", "Concavity1", "Concave_points1", 
    "Symmetry1", "Fractal_dimension1",
    "Radius2", "Texture2", "Perimeter2", "Area2", "Smoothness2", "Compactness2", "Concavity2", "Concave_points2", 
    "Symmetry2", "Fractal_dimension2",
    "Radius3", "Texture3", "Perimeter3", "Area3", "Smoothness3", "Compactness3", "Concavity3", "Concave_points3", 
    "Symmetry3", "Fractal_dimension3"
]

# Φόρτωση του dataset
file_path = "C:/Users/nbala/Desktop/BreCanPred/Dataset/wdbc.data"
data = pd.read_csv(file_path, header=None, names=column_names)

# Εξαγωγή σε αρχείο Excel
output_file = "C:/Users/nbala/Desktop/BreCanPred/Dataset/wdbc.csv"
data.to_csv(output_file, index=False)

# Εμφάνιση των πρώτων γραμμών
print(data.head())
