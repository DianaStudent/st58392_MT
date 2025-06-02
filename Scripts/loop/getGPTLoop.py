import os
import json
import base64
import time
import subprocess
import shutil
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv("openai_key.env")
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
#projects = ["Cezerin", "shopizer", "prestashop", "nopCommerce", "medusa"]
project = "medusa"
resolution = "1024"
base_dir = rf"C:\Diana\MasterCode\code\Projects\{project}\Processes"
base_output_root = os.path.join(base_dir, "tests", "gpt4o", "feedback")

def run_test(test_file_path):
    try:
        result = subprocess.run(["python", test_file_path], capture_output=True, text=True, timeout=60)
        if result.returncode == 0:
            print("PASS")
            return True, ""
        else:
            print("FAIL")
            return False, result.stderr
    except Exception as e:
        return False, str(e)

def generate_test(process_name, html_data, prompt_init_template, prompt_retry_template, image_files, output_run, output_success, max_attempts=10):
    previous_code = ""
    error_message = ""
    for attempt in range(max_attempts):
        print(f"ATTEMPT: {attempt + 1}/{max_attempts} — {process_name}")
        if attempt == 0:
            prompt = prompt_init_template.format(html_data=json.dumps(html_data, indent=2))
        else:
            prompt = prompt_retry_template.format(
                html_data=json.dumps(html_data, indent=2),
                previous_code=previous_code,
                error_message=error_message
            )
        messages = [{
            "role": "user",
            "content": [{"type": "text", "text": prompt}]
        }]
        for img_path in image_files:
            with open(img_path, "rb") as img_file:
                messages[0]["content"].append({
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{base64.b64encode(img_file.read()).decode()}",
                        "detail": "low"
                    }
                })
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=messages
            )
            code_parts = response.choices[0].message.content.split("```python")[1:]
            if not code_parts:
                return False
            code = code_parts[0].split("```")[0].strip()
        except Exception as e:
            print(f"ERROR: {e}")
            return False
        test_file = os.path.join(output_run, f"test_{process_name}_v{attempt+1}.py")
        with open(test_file, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"SUCCESS: {test_file}")
        success, error_message = run_test(test_file)
        if success:
            shutil.copy(test_file, os.path.join(output_success, os.path.basename(test_file)))
            return True
        else:
            previous_code = code
    print(f"FAIL: {max_attempts} attempts.")
    return False

for i in range(5):
    print(f"ITERATION: {i + 1}")
    start = time.time()
    existing = [d for d in os.listdir(base_output_root) if d.isdigit()]
    existing_numbers = sorted([int(d) for d in existing])
    next_number = (existing_numbers[-1] + 1) if existing_numbers else 1
    output_root = os.path.join(base_output_root, str(next_number))
    output_run = os.path.join(output_root, "loops")
    output_success = os.path.join(output_root, "success")
    os.makedirs(output_run, exist_ok=True)
    os.makedirs(output_success, exist_ok=True)
    print(f"OUTPUT: {output_root}")
    input_folder = os.path.join(base_dir, "data", "cleanData")
    prompts_folder = os.path.join(base_dir, "data", "prompts", "gpt4o", "feedback")
    screenshots_base = os.path.join(base_dir, "data", "screenshots", "resolution", resolution)
    all_files = [f for f in os.listdir(input_folder) if f.endswith("_html.json")]
    for file in all_files:
        process_name = file.replace("_html.json", "")
        html_path = os.path.join(input_folder, file)
        prompt_init_path = os.path.join(prompts_folder, f"{process_name}_initial_prompt.txt")
        prompt_retry_path = os.path.join(prompts_folder, f"{process_name}_loop_prompt.txt")
        screenshot_dir = os.path.join(screenshots_base, f"{process_name}_screen")
        with open(html_path, "r", encoding="utf-8") as f:
            html_data = json.load(f)
        with open(prompt_init_path, "r", encoding="utf-8") as f:
            prompt_init_template = f.read()
        with open(prompt_retry_path, "r", encoding="utf-8") as f:
            prompt_retry_template = f.read()
        image_files = sorted([
            os.path.join(screenshot_dir, f)
            for f in os.listdir(screenshot_dir)
            if f.lower().endswith(".png")
        ])
        generate_test(process_name, html_data, prompt_init_template, prompt_retry_template, image_files, output_run, output_success, max_attempts=10)

print(f"FIN {time.time() - start:.2f} seconds")
