from flask import Flask, render_template, request
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def upload_form():
    return render_template('upload_form.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'Файл не выбран'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'Файл не выбран'
    
    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return f'Файл "{filename}" загружен!'
    
    return 'Ошибка загрузки'

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)