from flask import Flask, render_template

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Projects Page
@app.route('/projects')
def projects():
    return render_template('projects.html')

# About Page
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/certifications')
def certifications():
    return render_template('certifications.html')

if __name__ == '__main__':
    app.run(debug=True)