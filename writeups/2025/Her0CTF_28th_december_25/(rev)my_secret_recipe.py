debug = 0

recipe = "\tTo bake the perfect flag-cake: sift the flour, add sugar, crack some eggs,\n \tmelt the butter, blend in vanilla and milk, whisk the cocoa, fold in the baking powder,\n \tswirl in the cream, chop some cherry, toss on sprinkles, preheat the oven, grease the pan,\n \tline it with parchment, set the timer, light a candle, serve on a plate, and garnish with frosting,\n \ta pinch of salt, and crushed nuts for that final touch of sweetness. \n\n"

def tokenise(string):
    tokens = string.split()
    counter = 0
    while counter < len(tokens):
        tokens[counter] = tokens[counter].strip(".,:;!?-[]{}()")
        counter = counter + 1
    return tokens

ingredients = {
    "bake":0x48, "perfect":0x65, "sift":0x72, "flour":0x6f, "sugar":0x7b, "crack":0x30,
    "eggs":0x68, "melt":0x5f, "butter":0x4e, "blend":0x30, "vanilla":0x5f, "milk":0x79,
    "whisk":0x30, "cocoa":0x75, "fold":0x5f, "baking":0x36, "powder":0x30, "swirl":0x54,
    "cream":0x5f, "chop":0x4d, "cherry":0x79, "toss":0x5f, "sprinkles":0x53, "preheat":0x33,
    "oven":0x63, "grease":0x52, "pan":0x65, "line":0x54, "parchment":0x5f, "timer":0x43,
    "light":0x34, "candle":0x6b, "plate":0x33, "garnish":0x5f, "frosting":0x52, "pinch":0x33,
    "salt":0x63, "crushed":0x31, "nuts":0x70, "touch":0x65, "sweetness":0x7d,
    }
    
def decode(tokens):
    counter = 0
    decoded_tokens = []
    debug_tokens = []
    while counter < len(tokens):
        word = tokens[counter]
        if word in ingredients:
            decoded_tokens.append(ingredients[word])
            debug_tokens.append(tokens[counter])
        counter += 1
        
    if debug == True:
        print(debug_tokens)
        
    return decoded_tokens
        
def from_hex(tokens):
    ascii_string = ""
    
    for i in tokens:
        char = chr(i)
        ascii_string = ascii_string + char
        
    return ascii_string
    
if __name__ == "__main__":
    
    tokens = tokenise(recipe)
    decoded = decode(tokens)
    ascii_chars = from_hex(decoded)
    print(ascii_chars)
