from flask import Flask, request, jsonify, render_template
import untitled13  

app = Flask(__name__)

@app.route('/')
def home():
     return render_template("index.html") 

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form  
        user_text = data.get("review", "")

        if not user_text:
            return jsonify({"error": "No review provided"}), 400

        result = untitled13.analyze_sentiment(user_text)
        return jsonify({
            "score": result.get("score"),
            "censored": result.get("censored"),
            "translated": result.get("translated")
        })

    except Exception as e:
        
        print(f"Error during sentiment analysis: {e}")
        return jsonify({
            "score": "Error",
            "censored": "Error during processing.",
            "translated": "Error during processing."
        }), 500 

if __name__ == '__main__':
    app.run(debug=True)