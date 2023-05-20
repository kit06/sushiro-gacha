from flask import Flask, request, redirect, render_template, session, flash

app = Flask(__name__)

#寿司の値段：1,000円以内
@app.route('/matsu')
def matsu():
  return render_template('matsu.html')

#寿司の値段：3,000円以内
@app.route('take')
def take():
    return render_template('take.html')

#寿司の値段：5,000円以内
@app.route('ume')
def ume():
    return render_template('ume.html')


if __name__ == '__main__':
    app.run(debug=True)