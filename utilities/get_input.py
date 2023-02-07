import datetime
def get_int(prompt = "Please enter an integer", errorMessage = "That was not an Integer. Please enter an integer", min = None, max = None):
    while True:
        try:
            num = int(input(prompt))
            #check if min is set
            if min != None:
                if num < min:
                    #num is too small
                    raise Exception(f"Input must at least {min}")
            
            
            #check if max is set
            if max != None:
                if num > max:
                    #num is too big
                    raise Exception(f"Input must at most {max}")
           
            break
        except ValueError:
            #input is not valid
            print(errorMessage)
        except Exception as e:
            print(e)
    return num
def get_float(prompt = "Please enter a float", errorMessage = "That was not a Float. Please enter a float", min = None, max = None):
    while True:
        try:
            num = float(input(prompt))
            #check if min is set
            if min!= None:
                if num < min:
                    #num is too small
                    raise Exception(f"Input must at least {min}")
                
            #check if max is set
            if max!= None:
                if num > max:
                    #num is too big
                    raise Exception(f"Input must at most {max}")
           
            break  
        
        except ValueError:
            #input is not valid
            print(errorMessage)
            
        except Exception as e:
            print(e)
            
    return num
def get_String(prompt = "Please enter a String", errorMessage = "That was not a String (how did you do that?). Please enter a string"):
    while True:
        try:
            str = input(prompt)
            break
        except ValueError:
            #input is not valid
            print(errorMessage)
        except Exception as e:
            print(e)
            
    return str
def get_date_as_str(prompt = "Please enter a date", errorMessage = "That was not a valid date. Please enter a date in the format MM/DD/YYYY"):
    while True:
        try:
            date = input(prompt)
            date_split = date.split("/")
            if len(date_split)!= 3:
                #input is not valid
                raise ValueError
            else:
                date_format = '%m/%d/%Y'
                datetime.datetime.strptime(date, date_format)
                return date
        except ValueError:
            #input is not valid
            print(errorMessage)
        except Exception as e:
            print(e)