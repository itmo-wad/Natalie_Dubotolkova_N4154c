from flask import Flask, redirect, render_template, send_from_directory, url_for
app = Flask(__name__)


@app.route('/static/<path:filename>')
def static_files(filename):
    return  send_from_directory('static', filename)

@app.route('/profile')
def profile():
    return  render_template('profile.html')

@app.route('/')
def redirect_to_profile():
    return  redirect(url_for('profile'))


app.route('/profile_render')
def profile_render():
    name="Natalie Dubotolkova"
    return render_template('profile_render.html',name=name)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)