from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def train_model():
    # Load dataset
    data = load_breast_cancer()
    X, y = data.data, data.target

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Create model
    model = LogisticRegression(max_iter=200, solver='liblinear')

    # Train the model
    model.fit(X_train, y_train)

    # Predict
    preds = model.predict(X_test)

    # Evaluate
    accuracy = accuracy_score(y_test, preds)

    print("Model: Logistic Regression")
    print("Accuracy:", accuracy)

    return accuracy


if __name__ == "__main__":
    train_model()
