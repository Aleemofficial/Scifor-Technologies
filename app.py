# Importing necessary modules
from flask import Flask, render_template

# Creating an instance of the Flask app
app = Flask(__name__)

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    # Example projects data
    projects_data = [
        {'title': 'Project 1', 'description': 'Create a snake game Project 1'},
        {'title': 'Project 2', 'description': 'create tick tac toe using tkinter 2'},
        {'title': 'Project 3', 'description': 'create portfolio using Django Project 3'},
        {'title': 'Project 4', 'description': 'create portfolio using flask Project 4'},
    ]
    return render_template('projects.html', projects=projects_data)

# Running the Flask app
if __name__ == '__main__':
    app.run(debug=True)
