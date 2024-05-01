"""
text_to_HTML: converts raw text into HTML
"""
def text_to_HTML(text: str) -> str:
    html = ""
    lines = [line.strip().replace("/\r", "") for line in text.split("\n")]
    return lines