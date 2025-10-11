import os
import zipfile
import base64
from PIL import Image
import io

# Create directory for the project
project_dir = "pcs-academy-quiz-final"
os.makedirs(project_dir, exist_ok=True)
os.makedirs(f"{project_dir}/assets", exist_ok=True)

# Create package.json for Render deployment
package_json = """{
  "name": "pcs-academy-quiz",
  "version": "1.0.0",
  "description": "PCS Academy Educational Quiz Application",
  "main": "index.html",
  "scripts": {
    "build": "echo 'Static site - no build required'",
    "start": "echo 'Static site deployed successfully'"
  },
  "keywords": ["education", "quiz", "pcs-academy", "learning"],
  "author": "PCS Academy School",
  "license": "MIT"
}"""

with open(f"{project_dir}/package.json", "w") as f:
    f.write(package_json)

print("Created package.json")