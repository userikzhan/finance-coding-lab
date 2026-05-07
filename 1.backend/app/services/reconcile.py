import pandas as pd

def reconcile(file):
    df = pd.read_excel(file)

    # пример логики сверки
    df["difference"] = df["expected"] - df["actual"]

    return df.to_dict(orient="records")
