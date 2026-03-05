# Remove unnecessary columns
data = data.drop(['RowNumber','CustomerId','Surname'], axis=1)

# Encode categorical columns
label_encoder = LabelEncoder()

data['Geography'] = label_encoder.fit_transform(data['Geography'])
data['Gender'] = label_encoder.fit_transform(data['Gender'])

print(data.head())