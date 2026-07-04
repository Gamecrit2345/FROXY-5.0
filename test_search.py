from duckduckgo_search import DDGS

with DDGS() as ddgs:
    results = list(ddgs.text("test NSFW", max_results=5))
    print(results)
