from flask import Flask, render_template, request, jsonify
import requests

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query', '')
    if not query:
        return jsonify({'error': 'Walang query'}), 400
    
    # Enhanced query for better porn results
    enhanced_query = query + " NSFW OR porn OR xxx OR video"
    
    try:
        # Use a simple web search via requests (fallback)
        headers = {'User-Agent': 'Mozilla/5.0'}
        # For now, return mock + real attempt
        results = [
            {"title": f"Best match for {query}", "href": f"https://www.pornhub.com/search?q={query.replace(' ', '+')}", "body": "High quality results from major sites"},
            {"title": "XVideos Results", "href": f"https://www.xvideos.com/?k={query.replace(' ', '+')}", "body": "Fast streaming videos"}
        ]
        
        return jsonify({
            'text': results,
            'images': []  # pwede natin idagdag later
        })
    except:
        return jsonify({'text': [{"title": "Try these links", "href": "https://www.pornhub.com", "body": "Manual search muna"}]})

if _name_ == '_main_':
    app.run(debug=True, port=5000)
Compose
Write to Denton Sagmayao
