accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

print(classification_report(y_test, y_pred))