import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

class Classifiers:
    def __init__(self):
        self.data = pd.read_csv("Manhattan.csv")
        self.df = pd.DataFrame(self.data)

    def build_manhattan_classifier(self):

        features = self.df[['bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway',
        'floor', 'building_age_yrs', 'no_fee', 'has_roofdeck', 'has_washer_dryer', 
        'has_doorman', 'has_elevator', 'has_dishwasher', 'has_patio', 'has_gym']]
        labels = self.df[['rent']]

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

class Choices:
    def __init__(self):
        self.mc = Classifiers()

    def flat_features(self):
        self.bedrooms = int(input("Please enter Number of bedrooms in the flat "))
        self.bathrooms = int(input("Enter the number of bathrooms in the flat "))
        self.size_sqft = int(input("Enter the Size per square foot "))
        self.min_to_subway = int(input("Enter time to subway in minutes "))
        self.floor = int(input("Enter Floor number of flat "))
        self.building_age_yrs = int(input("Enter Building age in years "))
        self.no_fee = int(input("Does building have broker free 1 = Yes 0 = No "))
        self.has_roofdeck = int(input("Does building have roof deck 1 = Yes 0 = No "))
        self.has_washer_dryer = int(input("Does the flat have a washer/dryer 1 = Yes 0 = No "))
        self.has_doorman = int(input("Does the building have a doorman 1 = Yes 0 = No "))
        self.has_elevator = int(input("Does the building have a elevator 1 = Yes 0 = No"))
        self.has_dishwasher = int(input("does the flat have a dishwasher 1 = Yes 0 = No "))
        self.has_patio = int(input("Does the flat have a patio 1 = Yes 0 = No "))
        self.has_gym = int(input("Does the Building have a gym 1 = Yes 0 = No "))
        print("************************************************************************")
        print("Predicting Flat Rent...")

    def menu(self):
        print("Flat Rent Prediction Application")
        print("Please Select an area to predict")
        print("1. Manhattan")
        choice = int(input("Please Enter your choice: "))
        if choice == 1:
            self.flat_features()
            self.mc.predict_manhattan_price(self.bedrooms, self.bathrooms, self.size_sqft, self.min_to_subway, self.floor, self.building_age_yrs, 
        self.no_fee,self.has_roofdeck, self.has_washer_dryer, self.has_doorman, self.has_elevator, 
        self.has_dishwasher, self.has_patio, self.has_gym)
        else:
            self.menu()

if __name__ == '__main__':
    choices = Choices()
    choices.menu()

