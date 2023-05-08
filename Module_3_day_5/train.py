from sklearn import datasets
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import fire
import mlflow
import pandas as pd


def preprocess_data(df: pd.DataFrame):
    df["style"] = df["style"].replace("red", 1)
    df["style"] = df["style"].replace("white", 0)

    return df


def get_metrics(y_true, y_pred):
    from sklearn.metrics import accuracy_score, precision_score, recall_score, log_loss

    acc = accuracy_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred, average="micro")
    prec = precision_score(y_true, y_pred, average="micro")
    recall = recall_score(y_true, y_pred, average="micro")

    return {
        "accuracy": round(acc, 2),
        "precision": round(prec, 2),
        "recall": round(recall, 2),
        "f1_score": round(f1, 2),
    }


def create_experiment(run_name, run_metrics, model):
    mlflow.set_tracking_uri(
        "http://localhost:5010"
    )  # uncomment this line if you want to use any database like sqlite as backend storage for model
    # mlflow.set_experiment(experiment_name)
    # mlflow.log_params(model_metadata)

    with mlflow.start_run():
        for metric in run_metrics:
            mlflow.log_metric(metric, run_metrics[metric])

        mlflow.sklearn.log_model(
            model, "model", registered_model_name="sklearn_logistic_t"
        )

        mlflow.set_tag("tag1", "Logistic Regression")
        mlflow.set_tags({"tag2": "Logistic Search CV", "tag3": "Production"})

    print("Run - %s is logged to Experiment " % (run_name))


def main(file_name: str):
    # training model
    df = preprocess_data(pd.read_csv("wine_dataset.csv"))

    X = df.drop("style", axis=1)
    y = df["style"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    run_name = "Wine1"
    run_metrics = get_metrics(y_test, y_pred)

    create_experiment(run_name, run_metrics, model)


if __name__ == "__main__":
    fire.Fire(main)
