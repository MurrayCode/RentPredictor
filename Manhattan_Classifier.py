import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

class Manhattan_Classifier:
    def __init__(self):
        self.manhattan_data = pd.read_csv("Manhattan.csv")
        self.manhattan_df = pd.DataFrame(self.manhattan_data)

    def build_manhattan_classifier(self):
        features = self.manhattan_df[['bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway',
        'floor', 'building_age_yrs', 'no_fee', 'has_roofdeck', 'has_washer_dryer', 
        'has_doorman', 'has_elevator', 'has_dishwasher', 'has_patio', 'has_gym']]
        labels = self.manhattan_df[['rent']]

        X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size = 0.2, random_state = 8)
        self.classifier = LinearRegression()
        self.classifier.fit(X_train, y_train)
        self.y_predict = self.classifier.predict(X_test)
        return self.classifier

    def predict_manhattan_price(self, bedrooms, bathrooms, size_sqft, min_to_subway, floor, building_age_yrs,
     no_fee, has_roofdeck, has_washer_dryer, has_doorman, has_elevator, has_dishwasher, has_patio, has_gym):
        self.classifier = self.build_manhattan_classifier()
        self.flat_features = [[bedrooms, bathrooms, size_sqft, min_to_subway, floor, building_age_yrs,
     no_fee, has_roofdeck, has_washer_dryer, has_doorman, has_elevator, has_dishwasher, has_patio, has_gym]]
        self.predict = self.classifier.predict(self.flat_features)
        print("Predicted rent: $%.2f" % self.predict)