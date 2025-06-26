# vulnix_easyjerk solve script

local_38 = [88, 110, 96, 107, 123, 86, 102, 117]
    
def find_serial(number_list):
    serial = []
    counter = 0
    
    for x in number_list:
        serial_item = (local_38[counter] - 13) ^ (counter + 7)
        serial.append(serial_item)
        counter = counter + 1
        
    return serial

def characters(number_list):
    string = ""
    counter = 0
    
    for x in number_list:
        character = chr(number_list[counter])
        string = string + character
        counter = counter + 1
        
    return string
    
    
print(characters(find_serial(local_38)))