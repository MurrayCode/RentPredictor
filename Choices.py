import Brooklyn_Classifier as bc
import Manhattan_Classifier as mc
import Queens_Classifier as qc
class Choices:
    def __init__(self):
        self.mc = mc.Manhattan_Classifier()
        self.bc = bc.Brookyln_Classifier()
        self.qc = qc.Queens_Classifier()

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
        self.has_elevator = int(input("Does the building have a elevator 1 = Yes 0 = No "))
        self.has_dishwasher = int(input("does the flat have a dishwasher 1 = Yes 0 = No "))
        self.has_patio = int(input("Does the flat have a patio 1 = Yes 0 = No "))
        self.has_gym = int(input("Does the Building have a gym 1 = Yes 0 = No "))
        print("************************************************************************")
        print("Predicting Flat Rent...")

    def menu(self):
        print("Flat Rent Prediction Application for New York")
        print("Please Select an area to predict")
        print("1. Manhattan")
        print("2. Brooklyn")
        print("3. Queens")
        choice = int(input("Please Enter your choice: "))
        
        if choice == 1:
            self.flat_features()
            self.mc.predict_manhattan_price(self.bedrooms, self.bathrooms, self.size_sqft, self.min_to_subway, self.floor, self.building_age_yrs, 
        self.no_fee,self.has_roofdeck, self.has_washer_dryer, self.has_doorman, self.has_elevator, 
        self.has_dishwasher, self.has_patio, self.has_gym)

        if choice == 2:
            self.flat_features()
            self.bc.predict_brooklyn_price(self.bedrooms, self.bathrooms, self.size_sqft, self.min_to_subway, self.floor, self.building_age_yrs, 
        self.no_fee,self.has_roofdeck, self.has_washer_dryer, self.has_doorman, self.has_elevator, 
        self.has_dishwasher, self.has_patio, self.has_gym)

        if choice == 3:
            self.flat_features()
            self.qc.predict_queens_price(self.bedrooms, self.bathrooms, self.size_sqft, self.min_to_subway, self.floor, self.building_age_yrs, 
        self.no_fee,self.has_roofdeck, self.has_washer_dryer, self.has_doorman, self.has_elevator, 
        self.has_dishwasher, self.has_patio, self.has_gym)
        else:
            self.menu()