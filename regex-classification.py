import re

# Create a list of all your classified brand terms
with open('brand-terms.txt') as file:
    ExampleBrandTerms = [line.rstrip('\n') for line in file]

# Loop over each term against each other and see if you can find a match, this is to simplify the regex
multi_match = []
for line in ExampleBrandTerms:
    for line1 in ExampleBrandTerms:
        if line1.find(line) != -1 and line != line1:
            multi_match.append(line1)

# In the multi match there are the unecessary terms from our initial list
[ExampleBrandTerms.remove(value) if value in ExampleBrandTerms else 0 for value in multi_match] # removes matching terms

# Compile the remaining brand terms into regex

brand_regex = re.compile('|'.join(ExampleBrandTerms)) # Happy with wildcard matches here

# Create a function to return Brand/Non-brand

def run_match(term):
    if re.search(brand_regex,term) != None:
        return 'Brand'
    else:
        return 'Non-brand'

if __name__ == "__main__":
    result = run_match('canon')
    print(result)

