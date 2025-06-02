import os
import json
import time
import re
import subprocess
from vertexai.preview.generative_models import GenerativeModel, Part
from google.oauth2 import service_account
import vertexai

key_path = "geminiKey.json"
project_id = "mt-testgen"
location = "us-central1"
model_id = "gemini-2.0-flash-001"
credentials = service_account.Credentials.from_service_account_file(key_path)
vertexai.init(project=project_id, location=location, credentials=credentials)
model = GenerativeModel(model_id)
#projects = ["Cezerin", "shopizer", "prestashop", "nopCommerce", "medusa"]
project = "nopCommerce"
resolution = "1024"
max_attempts = 10
base_dir = rf"C:\Diana\MasterCode\code\Projects\{project}\Processes"
base_output_root = os.path.join(base_dir, "tests", "gemini", "feedback")

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
    
def generate_test(process_name, html_data, prompt_init_template, prompt_retry_template, image_files, output_run, output_success):
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
        parts = [prompt] + [
            Part.from_data(data=open(img_path, "rb").read(), mime_type="image/png")
            for img_path in image_files
        ]
        try:
            response = model.generate_content(
                parts,
                generation_config={"temperature": 0.4, "max_output_tokens": 2048}
            )
            matches = re.findall(r"```python(.*?)```", response.text, re.DOTALL)
            code = matches[0].strip() if matches else response.text.strip()
        except Exception as e:
            print(f"ERROR: {e}")
            return False
        test_file = os.path.join(output_run, f"test_{process_name}_v{attempt+1}.py")
        with open(test_file, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"SUCCESS: {test_file}")
        success, error_message = run_test(test_file)
        if success:
            os.makedirs(output_success, exist_ok=True)
            final_path = os.path.join(output_success, f"test_{process_name}_final.py")
            with open(final_path, "w", encoding="utf-8") as f:
                f.write(code)
            return True
        else:
            previous_code = code
        time.sleep(5 + attempt)

    print(f"FAIL: {max_attempts} attempts.")
    return False

def main():
    os.makedirs(base_output_root, exist_ok=True)
    existing = [d for d in os.listdir(base_output_root) if d.isdigit()]
    next_number = max([int(d) for d in existing], default=0) + 1
    output_root = os.path.join(base_output_root, str(next_number))
    output_run = os.path.join(output_root, "loops")
    output_success = os.path.join(output_root, "success")
    os.makedirs(output_run, exist_ok=True)
    os.makedirs(output_success, exist_ok=True)
    print(f"OUTPUT:  {output_root}")
    input_folder = os.path.join(base_dir, "data", "cleanData")
    prompts_folder = os.path.join(base_dir, "data", "prompts", "gemini", "feedback")
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
        generate_test(
            process_name, html_data,
            prompt_init_template, prompt_retry_template,
            image_files, output_run, output_success
        )
if __name__ == "__main__":
    for i in range(5):
        print(f"ITERATION: {i + 1}")
        start = time.time()
        main()
        print(f"FIN {time.time() - start:.2f} seconds")