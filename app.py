from flask import Flask, render_template, request, jsonify
from duckduckgo_search import DDGS

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query', '')
    nsfw = request.json.get('nsfw', True)
    
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query + (" NSFW" if nsfw else ""), max_results=12))
        
        images = list(DDGS().images(query + " NSFW", max_results=8))
        
        return jsonify({
            'text': results,
            'images': images
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if _name_ == '_main_':
    app.run(debug=True, host='0.0.0.0', port=5000)
Pek
