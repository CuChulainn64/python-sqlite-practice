
import sqlite3
import pandas as pd


db = './data/car_sale.db'

#insert
def add_car_sale(car_sale_df):
    
    conn = sqlite3.connect(db)
    cur = conn.cursor()   
    cur.execute("INSERT INTO car_sales_table (Make, Model, ColorID, VehicleType, CostPrice, SpareParts, LaborCost, Registration_Date, Mileage, PurchaseDate) VALUES (?,?,?,?,?,?,?,?,?,?)", *car_sale_df.values.tolist())
    conn.commit()
    car_sale_id = cur.lastrowid
    conn.close()
    return car_sale_id
    

     
#read
def read_car_sale(car_sale_id):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("SELECT * FROM car_sales_table WHERE StockID =?", (car_sale_id))
    conn.close()
    return cur.fetchone()
    
    
#read all
def read_all_car_sales():
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("SELECT * FROM car_sales_table")
    df = pd.DataFrame(cur.fetchall())
    df.columns = ['StockID', 'Make', 'Model', 'ColorID', 'VehicleType', 'CostPrice', 'SpareParts', 'LaborCost', 'Registration_Date', 'Mileage', 'PurchaseDate']
    df.set_index('StockID', inplace=True)
    conn.close()
    return df
    
    
#update
def update_car_sale(car_sale):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("UPDATE car_sales_table SET Make =?, Model =?, ColorID =?, VehicleType =?, CostPrice =?, SpareParts =?,LaborCost =?, Registration_Date =?, Mileage =?, PurchaseDate =? WHERE StockID =?", car_sale.data_for_update())
    conn.commit()
    conn.close()
    return "Update Successful"

#delete
def delete_car_sale(car_sale_id):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("DELETE FROM car_sales_table WHERE StockID =?", (car_sale_id,))
    conn.commit()
    conn.close()
    return "Delete Successful"
