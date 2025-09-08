from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.

print(products[:3])

# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.

customer_preferences = []

response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    # Add the customer preference to the list

    customer_preferences.append(preference)

    response = input("Do you want to add another preference? (Y/N): ").upper()

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.

customer_preferences = set(customer_preferences)

# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []

for item in products:
    temp = dict()
    for key in item.keys():
        if key == 'tags':
            temp[key] = set(item[key])
        else:
            temp[key] = item[key]
        converted_products.append(temp)

# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    matches = 0
    for tag1 in product_tags:
        for tag2 in customer_tags:
            if tag2 == tag1:
                matches += 1
    return matches

# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    recommended_products = []
    for product in products:
        matching_tags = count_matches(product['tags'], customer_tags)
        if matching_tags > 0:
            recommended_products.append([product['name'], matching_tags])
    return recommended_products

# TODO: Step 7 - Call your function and print the results

print(recommend_products(products, customer_preferences))

# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
# 2. How might this code change if you had 1000+ products?

'''
The core operation that I used were loops. The reason loops were used is because with their being a large number of products,
and in some cases certain aspects needed to be modified, implementing loops allowed me to vist each value and do whatever was
needed before moving on to the next value. If there were more than one thousand products, the code would not need to be changed
at all. The only thing that could be improved is making what is printed a bit cleaner and easier to read for the user.
'''