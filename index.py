from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# list to store event data
events = []


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/organisation', methods=['GET', 'POST'])
def organisation():
    if request.method == 'POST':
        # organization form submission handling
        event_title = request.form.get('event_name')
        event_date = request.form.get('event_date')
        event_description = request.form.get('event_description')
        num_volunteers = request.form.get('num_volunteers')

        event = {
            'title': event_title,
            'date': event_date,
            'description': event_description,
            'volunteers': num_volunteers
        }

        global events
        events.append(event)
        return redirect(url_for('event_created'))

    return render_template('organisation.html')


@app.route('/event_created')
def event_created():
    return render_template('created.html')


@app.route('/volunteer', methods=['GET', 'POST'])
def volunteer():
    if request.method == 'POST':
        # handle volunteer login
        return redirect(url_for('event_details'))
    return render_template('volunteer.html', events=events) if events else 'No event data available'


@app.route('/event_details')
def event_details():
    global events
    return render_template('Details.html', events=events) if events else 'No event data available'


if __name__ == '__main__':
    app.run(debug=True)
