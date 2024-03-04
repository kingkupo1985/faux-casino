import random
from flask import Flask, render_template
from flask_assets import Environment
from flask_scss import Scss
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy
from PIL import Image
from datetime import date
from par_sheet import ParSheet


# Initialize Flask
app = Flask(__name__)
scss = Scss(app, static_dir='static', asset_dir='static/scss')
assets = Environment(app)

# Jinja Function to put par_sheet to list in html
def dict_values_to_list(d):
    return list(d.values())

# Add custom filter to Jinja environment
app.jinja_env.filters['dict_values_to_list'] = dict_values_to_list

# Initialize Bootstrap & CKeditior
ckedit = CKEditor(app)
Bootstrap(app)

# get  key
app.config['SECRET_KEY'] = "MY SECRET KEY"

# Connecting to Database NOT MADE YET FOR USERS
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///faux_casino.db'
# app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# get current year
year = date.today().year

# Route Functions
@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template("index.html",
                           year=year)

@app.route('/slot-machine', methods=['GET', 'POST'])
def slot_machine():
    reels = {}
    for i in range(1, 6):
        par_sheet = ParSheet().generate_par_sheet()
        reels[i] = par_sheet
        # print(f"What is I: {i}\n reel[{i}]")
        # for j in range(1, 21):
        #     print()
        #     print(f"URL: {par_sheet[f'symbol_{j}']['image_url']} | Weight: {par_sheet[f'symbol_{j}']['weight']}")
    print(f"{reels}")
    return render_template('SlotMachine.html', reels=reels, random_weighted_index=random_weighted_index)


@app.route('/slot-machine2', methods=['GET', 'POST'])
def slot_machine2():
    reels = {}
    for i in range(1, 6):
        par_sheet = ParSheet().generate_par_sheet()
        reels[i] = par_sheet
        print(f"{reels[i]}")
    final_images_urls, symbol_numbers = create_vertical_images(reels)
    return render_template('SlotMachine2.html', images=final_images_urls, symbols_positions=symbol_numbers, year=year)


# Functions to be moved to class later
# def random_weighted_index(reel):
#     total_weight = sum(symbol_data['weight'] for symbol_data in reel.values())
#     rand_weight = random.uniform(0, total_weight)
#     cumulative_weight = 0
#     for symbol, symbol_data in reel.items():
#         cumulative_weight += symbol_data['weight']
#         if rand_weight < cumulative_weight:
#             return symbol
#     # In case of unexpected situation, return the last symbol
#     return symbol

def random_weighted_index(reel_data):
    weights = [reel_data[symbol]['weight'] for symbol in reel_data]
    return random.choices(range(1, len(reel_data) + 1), weights=weights)[0]

def create_vertical_images(reels):
    # Create a list to hold the final images
    final_images_urls = []
    # Create a list to hold symbol IDs and their positions
    symbol_positions = []
    final_symbol_positions = {}
    # Loop through each reel, dividing them into 5 groups
    for i in range(1, 6):
        # Create a blank image with a size large enough to fit all the images
        max_width = 150  # Assuming each image is 150x150
        total_height = 150 * 60  # Total height for 60 images per reel
        final_image = Image.new("RGB", (max_width, total_height))
        y_offset = 0  # Set Y offset
        symbol_positions = []  # Reset Symbol Positions for next reel

        while y_offset < total_height:
            for reel_key, reel_data in reels.items():
                # Check if the reel belongs to the current group
                if reel_key == i:
                    # Randomly select a symbol that needs to be added
                    random_index = random_weighted_index(reel_data)
                    symbol_data = reel_data[f'symbol_{random_index}']
                    # Get the image URL for the symbol
                    image_url = symbol_data['image_url']
                    file_path = f"static/{image_url}"
                    img = Image.open(file_path)

                    # Paste the image onto the final image
                    final_image.paste(img, (0, y_offset))

                    # Update the y offset for the next image
                    y_offset += 150

                    # Append symbol ID and its position to the list
                    symbol_positions.append((random_index, y_offset))

        # Create and Append Save Path
        final_image_save_path = f"static/img/final_image_{i}.png"
        final_image_path = f"img/final_image_{i}.png"
        final_image.save(final_image_save_path)

        # Append the final image to the list
        final_symbol_positions[f'final_image_{i}'] = symbol_positions
        final_images_urls.append(final_image_path)
    print(final_symbol_positions)


    return final_images_urls, final_symbol_positions


# Usage example:
# reels = {}
# for i in range(1, 6):
#     par_sheet = ParSheet().generate_par_sheet()
#     reels[i] = par_sheet
# final_images_url, symbol_numbers = create_vertical_images(reels)
# print(f"Final_images: {final_images_url}")
# print(f"{final_image_url}")
# print(f"{symbol_numbers}")

# final_images_urls = ['img/final_image_1.png', 'img/final_image_2.png', 'img/final_image_3.png','img/final_image_4.png', 'img/final_image_5.png']

if __name__ == '__main__':
    app.run(debug=True)


