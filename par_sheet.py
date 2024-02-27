import random

class ParSheet():
    def __init__(self):
        self.image_urls = [
        'img/angel.png',
        'img/apple.png',
        'img/banana.png',
        'img/bar.png',
        'img/blueberry.png',
        'img/dice.png',
        'img/dragon.png',
        'img/goblin.png',
        'img/grape.png',
        'img/grim.png',
        'img/island.png',
        'img/leaf.png',
        'img/money.png',
        'img/pineapple.png',
        'img/seven.png',
        'img/skeleton.png',
        'img/strawberry.png',
        'img/triple-bar.png',
        'img/triple-seven.png',
        'img/ying-yang.png'
    ]

# Function to generate par sheet for a single reel
    def generate_par_sheet(self):
        # Generate random weights for each image
        weights = [random.randint(1, 100) for _ in range(len(self.image_urls))]

        # Calculate the total weight
        total_weight = sum(weights)

        # Calculate the odds ratio for a 1:100 odds (increase for harder odds)
        odds_ratio = total_weight / 100

        # Generate the par sheet dictionary
        par_sheet = {}
        for i, image_url in enumerate(self.image_urls):
            symbol = f'symbol_{i+1}'
            weight = int(weights[i] / odds_ratio)
            par_sheet[symbol] = {'weight': weight, 'image_url': image_url}

        return par_sheet

#Example Usage
# pars = ParSheet()
# reel_par_sheets = [pars.generate_par_sheet() for _ in range(5)]
# for reel in reel_par_sheets:
#     print(f"{reel}")