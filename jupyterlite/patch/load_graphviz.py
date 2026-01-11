# load_graphviz.py - download Graphviz WASM assets and patch JupyterLite index.html
import os
import urllib.request
import shutil

# Get the directory of the parent of this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(SCRIPT_DIR)
ROOT_DIR = os.path.dirname(PARENT_DIR)

# 1. Download Graphviz WASM files to local
GRAPHVIZ_VERSION = "1.18.0"
GRAPHVIZ_ESM_URL = f"https://cdn.jsdelivr.net/npm/@hpcc-js/wasm-graphviz@{GRAPHVIZ_VERSION}/+esm"
STATIC_DIR = os.path.join(ROOT_DIR, "site", "lite", "static", "graphviz")

def download_graphviz_files():
    """Download Graphviz WASM files to local static directory"""
    os.makedirs(STATIC_DIR, exist_ok=True)
    
    # Download the ESM bundle
    esm_filename = "graphviz.esm.js"
    dest_path = os.path.join(STATIC_DIR, esm_filename)
    
    if os.path.exists(dest_path):
        print(f"  {esm_filename} already exists, skipping...")
        return True
        
    try:
        print(f"  Downloading ESM bundle from {GRAPHVIZ_ESM_URL}...")
        with urllib.request.urlopen(GRAPHVIZ_ESM_URL) as response, open(dest_path, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        print(f"  ✓ {esm_filename} downloaded successfully")
        return True
    except Exception as e:
        print(f"  ✗ Error downloading {esm_filename}: {e}")
        return False
    
# 2. Prepare injection script
INJECT_SCRIPT = """
<script type="module">
  console.log("Pre-loading Graphviz WASM from local files...");
  import { Graphviz } from "../static/graphviz/graphviz.esm.js";
  
  // Load Graphviz WASM and store the Promise globally
  window.jupyterGraphvizPromise = Graphviz.load().then(engine => {
      console.log("Graphviz WASM Ready!");
      return engine;
  });
</script>
"""

# 3. Inject code to Generated index.html 
INDEX_PATH = os.path.join(ROOT_DIR, "site", "lite", "lab", "index.html")

print("Step 1: Downloading Graphviz WASM files...")
if not download_graphviz_files():
    print("Error: Failed to download Graphviz files")
    exit(1)

print("\nStep 2: Patching index.html...")
if os.path.exists(INDEX_PATH):
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        html = f.read()

    # Inject the script before </head>
    if "</head>" in html:
        new_html = html.replace("</head>", f"{INJECT_SCRIPT}\n</head>")
        
        with open(INDEX_PATH, "w", encoding="utf-8") as f:
            f.write(new_html)
        print(f"✓ Successfully patched {INDEX_PATH}")
    else:
        print("✗ Error: </head> tag not found in index.html")
else:
    print(f"✗ Error: {INDEX_PATH} not found. Run 'jupyter lite build' first.")