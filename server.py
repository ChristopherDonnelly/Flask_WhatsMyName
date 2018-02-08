'''
Create a project that allows users to submit a form.

"/": renders a landing page with a form.

"/process": the route your form should submit to. In your process function, print the user's name and redirect to root.
'''

# Import Flask to allow us to create our app, and import
# render_template to allow us to render HTML Files.
from flask import Flask, render_template, request, redirect

app = Flask(__name__)                     # Global variable __name__ tells Flask whether or not we
                                          # are running the file directly or importing it as a module.

@app.route('/')                           # The "@" symbol designates a "decorator" which attaches the
                                          # following function to the '/' route. This means that
                                          # whenever we send a request to localhost:5000/ we will run
                                          # the following "hello_world" function.

def display_index():
    return render_template('index.html')    # Render the template and return it!

@app.route('/process', methods=['POST'])
def process():
    print "Got Post Info"
    # we'll talk about the following two lines after we learn a little more
    # about forms
    name = request.form['name']
    email = request.form['email']       # redirects back to the '/' route

    print 'Name: {}'.format(name)

    return redirect('/')


app.run(debug=True)                       # Run the app in debug mode.