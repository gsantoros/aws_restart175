"""
Usar o conjundo de dados (dataset) load_breast_cancer disponível na biblioteca scikit-learn;
Utilize o algoritmo Random Forest;
Dividir o conjunto de dados em 70% para treino e 30% para teste, garantindo a reprodutibilidade dos dados com 'random_state';
Variável target (vetor) composta de 0 (maligno) ou 1 (benigno)
"""

from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import random_state

from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.3, random_state=42)

modelo = RandomForestClassifier(random_state=42)

modelo.fit(x_train, y_train)

y_pred = modelo.predict(X_test)
y_pred_proba = modelo.predict_proba(X_test)[:,1]

precisao = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_pred_proba)

print(f"Precisão: {precisao:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1:.4f}")
print(f"AUC-ROC: {auc:.4f}")