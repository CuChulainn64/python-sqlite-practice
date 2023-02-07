
import crud
from utilities import car_sale, get_input
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def __init__(self):
    global df
    
def get_data():
    df = crud.read_all_car_sales()
    return df
    
def get_max_costPrice():
    return df['CostPrice'].max()
    
def get_min_costPrice():
    return df['CostPrice'].min()
    
def get_avg_costPrice():
    return df['CostPrice'].mean()

def get_mean_costprice_for_makes():
    return pd.DataFrame(df.groupby("Make")["CostPrice"].mean())

def get_mean_costprice_for_models():
    return pd.DataFrame(df.groupby("Model")["CostPrice"].mean())
def get_group_of_makes():
    make = get_input.get_String(prompt="Enter the make: ")
    return df.loc[df["Make"] == make]
def get_group_of_makes_and_models():
    make = get_input.get_String(prompt="Enter the make: ")
    model = get_input.get_String(prompt="Enter the model: ")
    return df.loc[df["Make"] == make & df["Model"] == model]
    
def labor_cost_grouped_by_mileage():
    return pd.DataFrame(df.groupby("Mileage")["LaborCost"].mean())

def labor_cost_grouped_by_make_and_model():
    return pd.DataFrame(df.groupby(["Make", "Model"])["LaborCost"].mean())

def plot_labor_cost_by_reg_date():
    df = df.astype({"Registration_Date": "datetime64[ns]"})
    sorted_df = df.sort_values(by=["Registration_Date"], ascending=True)
    plt.plot(sorted_df["Registration_Date"], sorted_df["LaborCost"])
    plt.xlabel("Registration Date")
    plt.ylabel("Labor cost")
    plt.show()
    
def new_car_sale():
    new_car_sale_df = car_sale.Car_sale().to_df()
    new_car_sale_id = crud.add_car_sale(new_car_sale_df)
    new_car_sale_df.rename(index={-1: new_car_sale_id}, inplace=True)

    df = pd.concat([df, new_car_sale_df], axis=0)
    return df
    

def del_car_sale():
    row_to_delete = get_input.get_int()
    try:
        df = df.drop(labels=row_to_delete)
        crud.delete_car_sale(row_to_delete)
    except Exception as e:
        print(e)
    return df
def update_car_sale():
    car_sale_update = car_sale.Car_sale(get_input.get_int(prompt="Enter the index of the car sale you want to update: ", max=df.index.max(), min=df.index.min()))
    df.loc[car_sale_update.to_df().index] = car_sale_update.to_df()
    crud.update_car_sale(car_sale_update)
    return df
