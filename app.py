@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query', '')
    nsfw = request.json.get('nsfw', True)
    
    try:
        ddgs = DDGS()
        results = list(ddgs.text(query + (" NSFW" if nsfw else ""), max_results=10))
        
        images = list(ddgs.images(query + " NSFW", max_results=6))
        
        return jsonify({
            'text': results,
            'images': images
        })
    except Exception as e:
        print("Search Error:", str(e))  # Para makita mo sa terminal
        return jsonify({'error': str(e)}), 500
