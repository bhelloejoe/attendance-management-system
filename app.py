from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory student data
students = [
    {"id": 1, "name": "Marapao Leonilla", "attendance": "Absent", "remarks": ""},
    {"id": 2, "name": "Arguillas Merael", "attendance": "Absent", "remarks": ""},
    {"id": 3, "name": "Celeste Jessa", "attendance": "Absent", "remarks": ""},
    {"id": 4, "name": "Dumagan Bhelloejoe", "attendance": "Absent", "remarks": ""},
    {"id": 5, "name": "Celoscia Virgillo", "attendance": "Absent", "remarks": ""},
]

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html', students=students)

# Route to update attendance
@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    for student in students:
        if student['id'] == id:
            if 'present' in request.form:
                student['attendance'] = 'Present'
            elif 'absent' in request.form:
                student['attendance'] = 'Absent'
            elif 'tardy' in request.form:
                student['attendance'] = 'Tardy'
            elif 'excused' in request.form:
                student['attendance'] = 'Absent with Excuse'
            break
    return redirect(url_for('index'))

# Route to add or view remarks
@app.route('/remarks/<int:id>', methods=['GET', 'POST'])
def remarks(id):
    for student in students:
        if student['id'] == id:
            if request.method == 'POST':
                student['remarks'] = request.form['remarks']
                return redirect(url_for('index'))
            return render_template('remarks.html', student=student)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
