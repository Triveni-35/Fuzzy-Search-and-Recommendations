Just run ipynb it will create pkl files
similarity.pkl is 703.13 MB; this exceeds GitHub's file size limit of 100.00 MB
so I could not add them in repo

<img width="899" alt="image" src="https://github.com/user-attachments/assets/2a957b3d-c702-40c3-9f0f-da75690eea61">
<img width="809" alt="image" src="https://github.com/user-attachments/assets/c45bad47-c7a7-46cc-8cb1-4bf39ac2fcb7">

<img width="560" alt="image" src="https://github.com/user-attachments/assets/06447b2c-671b-4dc0-af12-5faaa9177169">
<img width="923" alt="image" src="https://github.com/user-attachments/assets/c0c0efb0-e9c4-4404-b257-0227cc73a418">

1. Dataset and Similarity Calculation
Objective: Create a recommendation engine that suggests similar products based on a given product.
Data: You provided a dataset containing product information like name, image, link, ratings, no_of_ratings, discount_price, and actual_price.
Similarity Model:
We assumed the presence of a pre-trained similarity matrix that compares products using features such as their textual descriptions, product attributes, or embeddings. This matrix contains similarity scores between all pairs of products.
Pickled Data: The dataset and the similarity matrix were loaded using pickle, allowing us to work with the pre-processed data without recalculating it every time.
2. Flask Web Application
We built a simple web application using Flask to allow users to input a product name and receive recommendations based on their input.
Core Components:
index.html: The homepage where users can input a product name in a search field.
app.py: The main Python script handling the logic of the web application.
Routes:
/: Displays the search form.
/recommend: Handles form submission and returns recommendations.
Recommendation Function:
Exact Matching: Initially, we built a function that searched for an exact match of the product name entered by the user in the dataset.
Recommendation Logic: Once the product is found, we used the similarity matrix to get the top 10 most similar products and returned details about these products (name, image, price, etc.).
3. Key Improvement: Fuzzy Matching
Problem: The initial exact matching approach required users to input the exact product name. If the name was incomplete or misspelled, no results would be returned.
Solution: We introduced fuzzy matching using the fuzzywuzzy library. This allows the search engine to find products even if the user types a partial or incorrect name by finding the closest match.
fuzzywuzzy.process.extractOne(): This function takes the user’s input and compares it with the product names in the dataset to find the closest match based on string similarity.
4. Result Display
Once we have the recommendations, we render them on a results page with all the relevant details about each product.
Recommendation Output:
Product name
Image
Discount price and actual price
Number of ratings and average rating
A link to the product page
Enhanced result.html:
The results were displayed in a visually appealing format using CSS, including product cards, hover effects, and a responsive layout for a clean look.
5. Styling with CSS
We added custom CSS to make the web pages more visually appealing and modern:
Gradient Backgrounds: Applied to both the search and results pages for a modern look.
Form and Buttons Styling: The input fields and buttons were designed with padding, rounded corners, and hover effects for a better user experience.
Product Cards: In the results, each product was displayed in a card format with shadow effects and a hover zoom for better interactivity.
6. Error Handling
We accounted for cases where:
No product matched the search query (even after fuzzy matching).
In such cases, a message is displayed, informing the user that no product was found.
7. Summary of Key Technologies and Libraries Used
Flask: A lightweight web framework to build the web app.
Pandas: Used to handle the dataset and perform product lookups.
Pickle: To load the pre-trained similarity matrix and dataset efficiently.
fuzzywuzzy: For fuzzy matching and finding the closest product names when users provide incomplete or incorrect input.
HTML/CSS: To structure and style the web pages, ensuring a modern and responsive user interface.
Similarity Matrix: Pre-calculated similarity scores between products to enable product recommendations.
8. Flow of the Web App
Homepage: The user inputs a product name.
Fuzzy Matching: The input is compared against the dataset, and the closest matching product is identified.
Recommendation: Based on the selected product, the system retrieves the top 10 similar products using the similarity matrix.
Result Display: The recommendations are displayed on a separate page with detailed product information.
Error Handling: If no close match is found, an error message is shown.
