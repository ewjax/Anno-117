import sys
import json
import os
import webview

if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODINFO_PATH = os.path.join(os.path.dirname(sys.executable if sys.frozen else __file__), "modinfo.json")
COLORPICKER_PATH = os.path.join(BASE_DIR, "colorpicker.html")

class Api:
    def save_color(self, int_color):
        """
        Called from JavaScript.
        Saves the Int Color into modinfo.json
        """
        try:
            with open(MODINFO_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)

            data["Options"]["customcolour"]["default"] = str(int_color)

            with open(MODINFO_PATH, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)

            return f"Saved Int Color {int_color} to modinfo.json"

        except Exception as e:
            return f"Error: {e}"


def inject_js(window):
    """
    Injects a Save button and hooks into the existing Int Color field
    """
    js = """
        (function () {
            const section = document.getElementById('section-int');
            const btn = document.createElement('button');
            btn.textContent = 'Save to modinfo.json';
            btn.style.marginLeft = '6.5em';
            btn.style.marginTop = '1em';

            btn.onclick = () => {
                const value = document.getElementById('intcolor').value;
                if (!value) {
                    alert("No Int Color value found!");
                    return;
                }

                window.pywebview.api.save_color(value).then(msg => {
                    alert(msg);
                });
            };

            section.appendChild(btn);
        })();
    """
    window.evaluate_js(js)


if __name__ == "__main__":
    api = Api()

    window = webview.create_window(
        title="Anno 117 – Custom Player Colour",
        url=COLORPICKER_PATH,
        js_api=api,
        width=900,
        height=600,
    )

    webview.start(inject_js, window)