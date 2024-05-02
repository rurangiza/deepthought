
class Exo:
    def __init__(self, data: str) -> None:
        self.data = data
        self.title = None
        self.number = None
        self.compilationCMD = None
        self.passed = False
        self.error_type = None
    
    # generates an HTML component with all data inserted
    def get(self):
        pass

    def __str__(self) -> str:
        return "This is an exercice"

class Test:
    def __init__(self, data: str) -> None:
        self.data = data
        self.returnedfiles = {}
        self.exercices = None

"""
text_to_HTML: converts raw text into HTML
"""
def text_to_HTML(text: str) -> str:

    # split into lines and clean up
    start = text.find("= ex")
    lines = [line.strip().rstrip("/\r") for line in text[start:].split("\n")]
    
    # convert text to HTML
    html = ""
    for line in lines:
        if line.startswith("= ex"):
            html += to_title(line)
        elif line.startswith("= Test"):
            html += to_subtitle(line)
        elif line.startswith("$>"):
            html += to_script(line)
        else:
            html += to_paragraph(line)
    return html

def to_title(line: str) -> str:
    clean = line.replace("= ex", "").rstrip("=").strip()
    return f'<h1>{clean}</h1>'

def to_subtitle(line: str) -> str:
    clean = line.strip().replace("= Test", "").rstrip("=")
    return f'<h3> Test {clean}</h3>'

def to_script(line: str) -> str:
    clean = line.strip().replace("$>", "").lstrip()
    return f'<p><span>$></span> {clean}</p>'

def to_paragraph(line: str) -> str:
    clean = line.strip()
    return f'<p>{clean}</p>'
