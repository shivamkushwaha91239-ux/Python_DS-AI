# Create a variable for your fav movie title(str), release year(int), rating(float) out of 10, and watched(bool) and recommend(bool). Print all the variables and their types.

title = input("Enter your favorite movie title: ")
year = int(input("Enter the release year of the movie: "))
rating = float(input("Enter the rating of the movie out of 10: "))
watched = input("Have you watched the movie? (yes/no): ").strip().lower() == "yes"
recommend = input("Would you recommend the movie? (yes/no): ").strip().lower() == "yes"

print("Movie: ", title)
print("Movie type: ", type(title))

print("Release Year: ", year)
print("Year type: ", type(year))

print("Rating: ", rating)
print("Rating type: ", type(rating))

print("Watched: ", watched)
print("Watched type: ", type(watched))

print("Recommend: ", recommend)
print("Recommend type: ", type(recommend))

# create a dict representing a product with keys name, price and tags (list).. Write a code to add a new tag, update the price by applying a 10% discount, and print a formatted sentence describing the final prodduct using f-string.

product = {
    "name" : "Motorbike",
    "price": 70000.00,
    "tags": ["bike", "vehicle", "two-wheeler"]
    }

# add a tag:
product["tags"].extend(["transportation", "motorcycle"])

# update the price by applying a 10% discount
product["price"] = product["price"]*0.90

# print a formatted sentence describing the final product using f-string
print(f"The product is a {product['name']} and its updated price is {product['price']}. Its tags are {product['tags']}")