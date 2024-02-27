import random
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from flask_sqlalchemy import SQLAlchemy
from SlotMachineBrain import SlotMachine
from par_sheet import ParSheet


# Initialize Flask
app = Flask(__name__)

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
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coin_data.db'
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

# Functions to be moved to class later
def random_weighted_index(reel):
    total_weight = sum(symbol_data['weight'] for symbol_data in reel.values())
    rand_weight = random.uniform(0, total_weight)
    cumulative_weight = 0
    for symbol, symbol_data in reel.items():
        cumulative_weight += symbol_data['weight']
        if rand_weight < cumulative_weight:
            return symbol
    # In case of unexpected situation, return the last symbol
    return symbol

if __name__ == '__main__':
    app.run(debug=True)
