import praw
from random import choice

reddit = praw.Reddit(
                    client_id='',
                    client_secret='',
                    user_agent='Sauce Bot 1.0 by u/sauce-recipe-bot',
                    username='username',
                    password='pass'
                    )

def check(comment):
    phrase = ['sauce', 'saucy', 'dressing']
    if [i for i in phrase] in comment.body:
        return True
    else:
        return False

recipes = [
    """
    Recipe: Yum Yum Sauce - https://www.foodnetwork.com/recipes/yum-yum-sauce-12241328
    
    Ingredients:
    - 1 cup mayonnaise
    - 3 tablespoons ketchup
    - 1 tablespoon mirin
    - 1 tablespoon rice vinegar
    - 1/2 teaspoon garlic powder
    - 1/2 teaspoon onion powder
    - 1/2 teaspoon paprika
    - Pinch cayenne pepper
    ----------------------------------
    Directions:
    - Whisk the mayonnaise, ketchup, mirin, rice vinegar, garlic powder, onion powder, paprika and cayenne in a medium bowl until smooth.
    - Whisk in 1 tablespoon water until smooth and combined.
    """,
    """
    Recipe: Aioli - https://www.foodnetwork.com/recipes/aioli-12241218
    
    Ingredients:
    - 3 cloves garlic
    - Kosher salt
    - 1 tablespoon lemon juice
    - 2 large egg yolks
    - 1/2 cup neutral oil, such as vegetable or safflower oil
    - 1/2 cup extra-virgin olive oil
    - 1 tablespoon water, plus more if needed
    - Pinch cayenne pepper
    ----------------------------------
    Directions:
    - Smash the garlic cloves with the side of a chef's knife and sprinkle with 1/2 teaspoon salt.
    - Finely chop the garlic, using the side of the knife to periodically mash it against the cutting board, until it becomes a smooth paste. (You can also do this in a mortar and pestle.)
    - To make the aioli in a mini food processor, put the garlic paste in a mini food processor, add the lemon juice and egg yolks and pulse to combine.
    - With the machine running, add the neutral oil a few drops at a time, making sure it incorporates into the yolks and the mixture emulsifies.
    - Once all of the neutral oil is added, scrape down the sides of the work bowl and add the olive oil in the same manner. (If the machine seems like it is working too hard or straining while adding the oil, add the tablespoon of water at this point to loosen the mixture a bit; otherwise, add the tablespoon of water once all of the oil has been added.)
    - Mix in the cayenne. The aioli should be thick, shiny and smooth, with a spreadable consistency similar to jarred mayonnaise.
    - If you want a slightly thinner sauce, add 1 to 2 tablespoons additional water slowly, with the machine running, until you reach the desired consistency.
    - Serve chilled or at room temperature.
    
    - To make the aioli by hand, dampen a kitchen towel and roll up.
    - Form the towel roll into a circle and anchor a bowl in the center.
    - Whisk together the garlic paste, lemon juice and egg yolks in the bowl. Whisk the oils into the mixture as directed above, using one hand to add the oil drop by drop and the other to whisk constantly.
    - Add the oil very slowly at first. Once the mixture has formed a thick emulsification, you can stream the oil in a little faster.
    - If it gets too thick, add the water to loosen it up and continue. Mix in the cayenne.
    """,
    """
    Recipe: Tomato Sauce - u/Nahid145
    
    Ingredients:
    - 2 tablespoons olive oil
    - 3 cloves garlic, minced
    - 1 (28 ounce) can crushed tomatoes
    - 1 teaspoon dried basil
    - Salt and pepper to taste
    ----------------------------------
    Directions:
    - Heat oil in a large skillet over low heat; add garlic and sauté until tender, about 2 minutes.
    - Stir in crushed tomatoes, basil, salt, and pepper. Simmer, stirring occasionally, until slightly thickened, 15 to 20 minutes. Serve immediately.
    """
]

sr = reddit.subreddit('dankmemes')

for comment in sr.stream.comments():
    if check(comment):
        comment.reply(choice(recipes) + '\n this action was performed by a bot, please contact u/sauce-recipe-bot for any questions or concerns.')
        print('Replied to comment ' + comment.submission.url)