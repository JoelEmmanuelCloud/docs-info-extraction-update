from re import findall
from re import DOTALL

def extract_snippet_from_tags(text, tag='json'):
    # Regex pattern to find the snippet within the <json> and </json> tags
    pattern = rf'<{tag}>(.*?)</{tag}>'
    results = findall(pattern, text, DOTALL)
    
    if results:
        return results[0]
    return text