import pandas as pd
from sklearn.preprocessing import standardScaler
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
df = pd.read_csv("creditcard.csv")
smote = SMOTE()

# print(df.head())
# print(df.isnull().sum())
# print(df['Class'].value_counts())

scaler = StandardScaler()
df['Amount'] = scaler.fit_transform(df[['Amount']])
X = df.drop('Class', axis=1)
y = df['Class']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

print(y_train_res.value_counts())
