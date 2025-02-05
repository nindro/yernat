#A recipe you are reading states how many grams you need for the ingredient. Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces. 
#`ounces = 28.3495231 * grams`
def conv(grams):
    ounces = 28.3495231 * grams
    print(ounces)
grams = int(input())
conv(grams)
#RESULT
#grams = 5
#ounces = 141.7476155