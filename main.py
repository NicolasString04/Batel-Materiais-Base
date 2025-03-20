from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/static/<path:filename>')
def static_files(filename):
    return app.send_static_file('static', filename)


@app.route('/pdfs/<path:filename>')
def pdf_files(filename):
    try:
        return send_from_directory('pdfs', filename)
    except FileNotFoundError:
        return "Arquivo não encontrado", 404

if __name__ == '__main__':
    app.run(debug=True)