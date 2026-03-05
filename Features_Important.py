importance = model.feature_importances_

features = X.columns

plt.barh(features, importance)

plt.title("Feature Importance in Customer Churn Prediction")

plt.show()