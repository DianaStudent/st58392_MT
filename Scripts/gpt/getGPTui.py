import openai
import json
import os
import base64
import time
from openai import OpenAI
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor

load_dotenv("openai_key.env")
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
start_time = time.time()
#project = ["Cezerin", "shopizer", "prestashop", "nopCommerce", "medusa"]
projects = ["prestashop"]
#base_dir = rf"C:\Diana\Master\MasterCode\code\Projects"
base_dir = rf"C:\Diana\Master\MasterCode\MAX\code\Projects"
prompt_types = ["simple", "medium", "detailed"]
resolutions = ["source", "768", "1024"]

def generate_ui_test(process_name, html_data, prompt_type, resolution, prompt_template, image_files, output_folder, max_retries=3):
    retries = 0
    while retries < max_retries:
        try:
            messages = [{
                "role": "user",
                "content": [{"type": "text", "text": prompt_template.format(html_data=json.dumps(html_data, indent=2))}]
            }]
            for img_path in image_files:
                with open(img_path, "rb") as img_file:
                    img_bytes = img_file.read()
                    messages[0]["content"].append({
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64.b64encode(img_bytes).decode()}",
                            "detail": "low"
                        }
                    })
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=messages
            )
            generated_code_parts = response.choices[0].message.content.split("```python")[1:]
            if not generated_code_parts:
                return
            output_file = os.path.join(output_folder, f"test_{process_name}.py")
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(generated_code_parts[0].split("```")[0].strip())
            print(f"SUCCESS: {output_file}")
            return
        except Exception as e:
            if "rate limit" in str(e).lower() or "429" in str(e):
                wait_time = 20 + retries * 10
                print(f"WAIT: {process_name} ({prompt_type}, {resolution}), {wait_time} seconds")
                time.sleep(wait_time)
                retries += 1
            else:
                print(f"ERROR: {process_name} ({prompt_type}, {resolution}): {e}")
                return
    print(f"ERROR: MAX retries {process_name} ({prompt_type}, {resolution})")
for project in projects:
    html_structure_path = os.path.join(base_dir, project, "Processes", "data", "cleanData", "UI_html.json")
    prompts_dir = os.path.join(base_dir, project, "Processes", "data", "prompts", "gpt4o", "zeroshot")
    screenshots_base = os.path.join(base_dir, project, "Processes", "data", "screenshots")
    output_base = os.path.join(base_dir, project, "Processes", "tests", "gpt4o", "ui")
    with open(html_structure_path, "r", encoding="utf-8") as f:
        html_dict = json.load(f)
    prompt_templates = {}
    for prompt_type in prompt_types:
        prompt_file = os.path.join(prompts_dir, f"ui_{prompt_type}_prompt.txt")
        if os.path.isfile(prompt_file):
            with open(prompt_file, "r", encoding="utf-8") as f:
                prompt_templates[prompt_type] = f.read().strip()
        else:
            print(f"ERROR: {prompt_file}")
    for iteration in range(5):
        print(f"ITERATION: {iteration + 1}")
        for process_name, html_raw in html_dict.items():
            print(f"PROCESS: {process_name}")
            html_data = {"html": html_raw}
            with ThreadPoolExecutor(max_workers=3) as executor:
                for prompt_type in prompt_types:
                    prompt_template = prompt_templates.get(prompt_type)
                    if not prompt_template:
                        continue
                    for resolution in resolutions:
                        if resolution == "source":
                            screenshot_dir = os.path.join(screenshots_base, "source", "UI", process_name)
                        else:
                            screenshot_dir = os.path.join(screenshots_base, "resolution", resolution, "UI", process_name)
                        if not os.path.isdir(screenshot_dir):
                            continue
                        image_files = sorted([
                            os.path.join(screenshot_dir, f)
                            for f in os.listdir(screenshot_dir)
                            if f.lower().endswith(".png")
                        ])
                        if not image_files:
                            continue
                        output_root = os.path.join(output_base, prompt_type, resolution)
                        folder_name = str(iteration + 1)
                        output_folder = os.path.join(output_root, folder_name)
                        os.makedirs(output_folder, exist_ok=True)
                        print(f"OUTPUT: {output_folder}")
                        executor.submit(
                            generate_ui_test,
                            process_name, html_data,
                            prompt_type, resolution, prompt_template,
                            image_files, output_folder
                        )
print(f"FIN {(time.time() - start_time):.2f} seconds")

