from flask import Flask, render_template

app = Flask('Event Calendar')

events = [
    {
        'title' : 'Tutorial for Boris',
        'start' : '2023-02-04T05:30:00-12:30',
        'description' : 'tutoring',
        'url' : 'https://fullcalendar.io/docs/initialView',
    },
    {
        'title' : 'Eat Hotpot',
        'start' : '2023-02-04',
        'description' : 'tutoring',
        'url' : 'https://fullcalendar.io/docs/initialView',
    }
]


if __name__ == '__main__':
    app.run(debug=True)

@app.route("/")
def home():
    return render_template("cal.html", events=events)



