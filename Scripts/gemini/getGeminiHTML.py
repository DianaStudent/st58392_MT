import os
import json
import time
import re
from concurrent.futures import ThreadPoolExecutor
from vertexai.preview.generative_models import GenerativeModel
from google.oauth2 import service_account
import vertexai

key_path = "geminiKey.json"
project_id = "mt-testgen"
location = "us-central1"
model_id = "gemini-2.0-flash-001"

credentials = service_account.Credentials.from_service_account_file(key_path)
vertexai.init(project=project_id, location=location, credentials=credentials)
model = GenerativeModel(model_id)

projects = ["Cezerin", "shopizer", "prestashop", "nopCommerce", "medusa"]
prompt_types = ["simple", "medium", "detailed"]
base_dir = r"C:\Diana\Master\MasterCode\code\Projects"
output_root_folder = "tests\\geminiHTML\\zeroshot"

def generate_test(project, process_name, html_data, prompt_type, prompt_template, output_folder, max_retries=3):
    retries = 0
    while retries < max_retries:
        try:
            prompt = prompt_template.format(html_data=json.dumps(html_data, indent=2))

            response = model.generate_content(
                [prompt],
                generation_config={"temperature": 0.4, "max_output_tokens": 2048}
            )

            matches = re.findall(r"```python(.*?)```", response.text, re.DOTALL)
            output_code = matches[0].strip() if matches else response.text.strip()

            os.makedirs(output_folder, exist_ok=True)
            output_path = os.path.join(output_folder, f"test_{process_name}.py")
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(output_code)
            return
        except Exception as e:
            print(f"ERROR: {process_name} ({prompt_type}) → {e}")
            retries += 1
            time.sleep(10 + retries * 5)
start_time = time.time()

for iteration in range(5):
    print(f"ITERATION: {iteration + 1}")
    for project in projects:
        project_path = os.path.join(base_dir, project, "Processes")
        input_structures = os.path.join(project_path, "data", "cleanData")
        prompts_base = os.path.join(project_path, "data", "prompts", "geminiHTML", "zeroshot")
        output_base = os.path.join(project_path, output_root_folder)
        existing_folders = []
        for pt in prompt_types:
            pt_dir = os.path.join(output_base, pt)
            os.makedirs(pt_dir, exist_ok=True)
            existing_folders.extend([
                int(f) for f in os.listdir(pt_dir) if f.isdigit()
            ])
        folder_index = 1 + max(existing_folders, default=0)
        for json_file in os.listdir(input_structures):
            if not json_file.endswith("_html.json"):
                continue
            process_name = json_file.replace("_html.json", "")
            with open(os.path.join(input_structures, json_file), "r", encoding="utf-8") as f:
                html_data = json.load(f)
            with ThreadPoolExecutor(max_workers=3) as executor:
                for prompt_type in prompt_types:
                    prompt_files = [
                        f for f in os.listdir(prompts_base)
                        if f.startswith(f"{process_name}_{prompt_type}") and f.endswith("_prompt.txt")
                    ]

                    if not prompt_files:
                        continue
                    prompt_file = os.path.join(prompts_base, prompt_files[0])
                    with open(prompt_file, "r", encoding="utf-8") as f:
                        prompt_template = f.read().strip()
                    output_folder = os.path.join(output_base, prompt_type, str(folder_index))
                    executor.submit(
                        generate_test,
                        project, process_name, html_data,
                        prompt_type, prompt_template,
                        output_folder
                    )

print(f"FIN {(time.time() - start_time).total_seconds():.2f} seconds")
