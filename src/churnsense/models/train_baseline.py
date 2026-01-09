from pathlib import Path
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score, average_precision_score

# Project root = churnsense/
ROOT = Path(__file__).resolve().parents[3]
RAW_PATH = ROOT / "data" / "raw" / "churn.csv"
MODEL_PATH = ROOT / "models" / "baseline_logreg.joblib"

# Columns that often leak the answer in churn datasets (drop if present)
LEAKAGE_COLS = ["CustomerStatus", "ChurnScore", "ChurnReason", "ChurnCategory"]

def find_target_column(df: pd.DataFrame) -> str:
    candidates = ["ChurnLabel", "Churn", "Exited", "is_churn"]
    for c in candidates:
        if c in df.columns:
            return c
    raise ValueError(
        "Could not find a target column. Expected one of: "
        f"{candidates}. Columns found: {list(df.columns)[:30]}..."
    )

def to_binary_target(y: pd.Series) -> pd.Series:
    # Handles Yes/No, True/False, 0/1
    if y.dtype == "object":
        y = (
            y.astype(str)
             .str.strip()
             .str.lower()
             .map({"yes": 1, "no": 0, "true": 1, "false": 0, "1": 1, "0": 0})
        )
    return y.astype(int)

def main():
    df = pd.read_csv(RAW_PATH)

    target = find_target_column(df)
    y = to_binary_target(df[target])

    drop_cols = [target] + [c for c in LEAKAGE_COLS if c in df.columns]
    X = df.drop(columns=drop_cols, errors="ignore")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    cat_cols = X.select_dtypes(include=["object", "category", "bool"]).columns.tolist()
    num_cols = [c for c in X.columns if c not in cat_cols]

    pre = ColumnTransformer(
        transformers=[
            ("num", Pipeline([
                 ("imputer", SimpleImputer(strategy="median")),
                 ("scaler", StandardScaler())
            ]), num_cols),
        ]
    )

    model = Pipeline(steps=[
        ("preprocess", pre),
        ("clf", LogisticRegression(max_iter=5000, solver="saga", n_jobs=-1))
    ])

    model.fit(X_train, y_train)

    proba = model.predict_proba(X_test)[:, 1]
    roc = roc_auc_score(y_test, proba)
    pr = average_precision_score(y_test, proba)

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    print(f"✅ Saved model: {MODEL_PATH}")
    print(f"ROC-AUC: {roc:.4f}")
    print(f"PR-AUC : {pr:.4f}")

if __name__ == "__main__":
    main()
