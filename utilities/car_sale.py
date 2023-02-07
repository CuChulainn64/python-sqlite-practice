
from models import get_input    
import pandas as pd
class Car_sale:
#
       
    def __init__(self, stock_id=-1):
        self.StockID = stock_id
        self.Make = get_input.get_String(prompt="Enter Make: ")
        self.Model = get_input.get_String(prompt="Enter Model: ")
        self.ColorID = get_input.get_int(prompt="Enter Color ID: ")
        self.VehicleType = get_input.get_String(prompt="Enter Vehicle Type: ")
        self.CostPrice = get_input.get_int(prompt="Enter Cost Price: ")
        self.SpareParts = get_input.get_int(prompt="Enter Spare Parts: ")
        self.LaborCost = get_input.get_int(prompt="Enter Labor Cost: ")
        self.Registration_Date = get_input.get_date_as_str(prompt="Enter Registration Date: ")
        self.Mileage = get_input.get_int(prompt="Enter Mileage: ")
        self.PurchaseDate = get_input.get_date_as_str(prompt="Enter Purchase Date: ")    

    #getters
    def get_Stock_id(self):
        return self.StockID
    def get_Make(self):
        return self.Make
    def get_Model(self):
        return self.Model
    def get_ColorID(self):
        return self.ColorID
    def get_VehicleType(self):
        return self.VehicleType
    def get_CostPrice(self):
        return self.CostPrice
    def get_SpareParts(self):
        return self.SpareParts
    def get_LaborCost(self):
        return self.LaborCost
    def get_Registration_Date(self):
        return self.Registration_Date
    def get_Mileage(self):
        return self.Mileage
    def get_PurchaseDate(self):
        return self.PurchaseDate

    #setters
    def set_Stock_id(self,StockID):
        self.Stock_id = StockID
        
    def set_Make(self,Make):
        self.Make = Make
        
    def set_Model(self,Model):
        self.Model = Model
        
    def set_ColorID(self,ColorID):
        self.ColorID = ColorID
        
    def set_VehicleType(self,VehicleType):
        self.VehicleType = VehicleType
        
    def set_CostPrice(self,CostPrice):
        self.CostPrice = CostPrice
        
    def set_SpareParts(self,SpareParts):
        self.SpareParts = SpareParts
        
    def set_LaborCost(self,LaborCost):
        self.LaborCost = LaborCost
        
    def set_Registration_Date(self,Registration_Date):
        self.Registration_Date = Registration_Date
        
    def set_Mileage(self,Mileage):
        self.Mileage = Mileage
        
    def set_PurchaseDate(self,PurchaseDate):
        self.PurchaseDate = PurchaseDate
        
    def __str__(self):
        return "StockID: " + str(self.StockID) + "\nMake: " + str(self.Make) + "\nModel: " + str(self.Model) + "\nColorID: " + str(self.ColorID) + "\nVehicleType: " + str(self.VehicleType) + "\nCostPrice: " + str(self.CostPrice) + "\nSpareParts: " + str(self.SpareParts) + "\nLaborCost: " + str(self.LaborCost) + "\nRegistration_Date: " + str(self.Registration_Date) + "\nMileage: " + str(self.Mileage) + "\nPurchaseDate: " + str(self.PurchaseDate)
    
    def to_df(self):
        data = {'StockID': [self.StockID], 'Make': [self.Make], 'Model': [self.Model], 'ColorID': [self.ColorID], 'VehicleType':[self.VehicleType], 'CostPrice': [self.CostPrice], 'SpareParts':[self.SpareParts], 'LaborCost':[self.LaborCost], 'Registration_Date':[self.Registration_Date], 'Mileage':[self.Mileage], 'PurchaseDate':[self.PurchaseDate]}
        df = pd.DataFrame(data)
        #set the index to StockID
        df.set_index('StockID', inplace=True)
        #print(df)
        return df
    def data_for_update(self):
        return [self.Make, self.Model, self.ColorID, self.VehicleType, self.CostPrice, self.SpareParts, self.LaborCost, self.Registration_Date, self.Mileage, self.PurchaseDate, self.StockID]
