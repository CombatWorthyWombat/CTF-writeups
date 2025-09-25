# Created on Tue Mar 03 
# Python 3
# UTF-8
# @author: CWW

# Checking "n" against factorDB database

from rdout import rdout,style
import requests

class FactorDB:

    def _query(n):
        factorDB_url = f"http://factordb.com/api?query={n}"
        # Query FactorDB API
        response = requests.get(factorDB_url)
        response.raise_for_status()  # Raise an error for HTTP issues
        # Parse the response JSON
        data = response.json()
        FactorDB._parse_response(data)
        # json format is: {'id': [id], 'status': [status], 'factors': [[factor1, exponent1], [factor2, exponent2]]}
    
        # API codes:
        # FF = "Fully factored"
        # C = "Composite, no factors known"
        # CF = "Composite, factors known"
        # P = "Definitley prime"
        # Prp = "Probably prime"
        # U = "Unknown number status"
        # Unit = "Used only for 1"
        # N = "This number is not in database (and was not added due to your settings)"
        
    def _parse_response(data):
        if 'status' in data:
            status = data['status']
            if status == 'FF':
                factors = data.get('factors', [])
                if len(factors) > 0:
                    rdout(style.GREEN, "Successfully factored n (FactorDB):")
                    for factor, exponent in factors:
                        print("Factor:", factor, "to the power of", exponent)
                else:
                    rdout(style.RED, "Couldn't fetch factors for n from FactorDB. Status code 'FF'")
                            
            elif status == 'CF':
                factors = data.get('factors', [])
                if len(factors) > 0:
                    rdout(style.GREEN, "Successfully factored n (FactorDB), some factors remain composite:")
                    for factor, exponent in factors:
                        print("Factor:", factor, "to the power of", exponent)
                else:
                    rdout(style.RED, "Couldn't fetch factors for n from FactorDB. Status code 'CF'")
                            
            elif status == 'C':
                rdout(style.YELLOW, "Composite, no factors known for n.")
                
            elif status == 'P':
                factors = data.get('factors', [])
                if len(factors) > 0:
                    rdout(style.BLUE, "n is definitely prime")
                    for factor, exponent in factors:
                        print("Factor:", factor, "to the power of", exponent)
                else:
                    rdout(style.RED, "Couldn't fetch factors for n from FactorDB. Status code 'P'")
                
            elif status == 'Prp':
                rdout(style.BLUE, "n is probably prime")
                
            elif status == 'U':
                rdout(style.BLUE, "Unknown factor status")
                
            elif status == 'Unit':
                rdout(style.BLUE, "Response code for digit: 1")
                
            elif status == 'N':
                rdout(style.YELLOW, "Number not on FactorDB database")
                    
        else:
            rdout(style.YELLOW, "Unexpected response format from FactorDB.")  



if __name__ == "__main__":
    
    while True:
        try:
            n = int(input("Enter n value to find factors for: "))
            break
        except ValueError as type_error:
            rdout(style.PURPLE, "Please enter a valid integer for n")
        
    FactorDB._query(n)

    