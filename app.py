from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store answers across multiple pages
answers = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/question1', methods=['GET', 'POST'])
def question1():
    if request.method == 'POST':
        answers['conflict'] = request.form.get('conflict')
        return redirect(url_for('question2'))
    return render_template('question1.html')

@app.route('/question2', methods=['GET', 'POST'])
def question2():
    if request.method == 'POST':
        answers['hangout'] = request.form.get('hangout')
        return redirect(url_for('question3'))
    return render_template('question2.html')

@app.route('/question3', methods=['GET', 'POST'])
def question3():
    if request.method == 'POST':
        answers['vibe'] = request.form.get('vibe')
        return redirect(url_for('result'))
    return render_template('question3.html')

@app.route('/result')
def result():
    # Determine which mob matches the answers
    conflict = answers.get('conflict')
    hangout = answers.get('hangout')
    vibe = answers.get('vibe')

    if conflict == 'avoid' and hangout == 'solo' and vibe == 'chill':
        mob = 'Enderman'
        description = "You're mysterious, calm, and a bit misunderstood. People admire your quiet strength."
        image = url_for('static', filename='images/enderman.jpg')
    elif conflict == 'fight' and hangout == 'group' and vibe == 'chaotic':
        mob = 'Creeper'
        description = "You bring energy and excitement—sometimes too much! But hey, you're unforgettable."
        image = url_for('static', filename='images/creeper.jpg')
    elif conflict == 'talk' and hangout == 'animals' and vibe == 'nature':
        mob = 'Wolf'
        description = "Loyal and wild, you stick by your friends and love the outdoors."
        image = url_for('static', filename='images/wolf.jpg')
    else:
        mob = 'Iron Golem'
        description = "You're practical, a bit quirky, and always have something interesting going on. Hmmm..."
        image = url_for('static', filename='images/irongolem.jpg')

    return render_template('result.html', mob=mob, description=description, image=image)

if __name__ == '__main__':
    app.run(debug=True)
