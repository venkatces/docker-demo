from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
   "https://st2.depositphotos.com/1000877/5947/i/950/depositphotos_59478951-stock-photo-red-kitten.jpg",
    "https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
