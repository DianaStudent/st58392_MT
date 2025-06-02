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

#projects = ["Cezerin", "shopizer", "prestashop", "nopCommerce", "medusa"]
projects = ["Cezerin"]
prompt_types = ["simple", "medium", "detailed"]
resolutions = ["source", "768", "1024"]
base_dir = r"C:\Diana\Master\MasterCode\code\Projects"

def generate_test(project, process_name, html_data, prompt_type, resolution, prompt_template, image_files, output_folder, max_retries=3):
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
                print(f"ERROR: {process_name} ({prompt_type}, {resolution})")
                return

            output_file = os.path.join(output_folder, f"test_{process_name}.py")
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(generated_code_parts[0].split("```")[0].strip())

            print(f"SUCCESS: {output_file}")
            return
        except Exception as e:
            if "rate limit" in str(e).lower() or "429" in str(e):
                wait_time = 20 + retries * 10
                print(f"WAIT: Rate limit for {process_name} ({prompt_type}, {resolution}), {wait_time} seconds")
                time.sleep(wait_time)
                retries += 1
            else:
                print(f"ERROR: Generation failed for {process_name} ({prompt_type}, {resolution}): {e}")
                return
    print(f"ERROR: Max retries {process_name} ({prompt_type}, {resolution})")
for iteration in range(5):
    print(f"ITERATION: {iteration + 1}")

    for project in projects:
        project_path = os.path.join(base_dir, project, "Processes")
        print(f"PROJECT: {project}")

        input_structures = os.path.join(project_path, "data", "cleanData")
        prompts_base = os.path.join(project_path, "data", "prompts", "gpt4o", "zeroshot")
        screenshots_base = os.path.join(project_path, "data", "screenshots")
        output_base = os.path.join(project_path, "tests", "gpt4o", "zeroshot")

        shared_output_index = {}
        for prompt_type in prompt_types:
            shared_output_index[prompt_type] = {}
            for resolution in resolutions:
                output_root = os.path.join(output_base, prompt_type, resolution)
                os.makedirs(output_root, exist_ok=True)
                existing_folders = [f for f in os.listdir(output_root) if f.isdigit()]
                next_index = 1 + max([int(f) for f in existing_folders], default=0)
                shared_output_index[prompt_type][resolution] = next_index

        for json_file in os.listdir(input_structures):
            if not json_file.endswith("_html.json"):
                continue

            process_name = json_file.replace("_html.json", "")
            print(f"PROCESS: {process_name}")

            with open(os.path.join(input_structures, json_file), "r", encoding="utf-8") as f:
                html_data = json.load(f)

            with ThreadPoolExecutor(max_workers=3) as executor:
                for prompt_type in prompt_types:
                    prompt_file = os.path.join(prompts_base, f"{process_name}_{prompt_type}_prompt.txt")
                    if not os.path.isfile(prompt_file):
                        print(f"WARNING: {prompt_file}")
                        continue

                    with open(prompt_file, "r", encoding="utf-8") as f:
                        prompt_template = f.read().strip()

                    for resolution in resolutions:
                        if resolution == "source":
                            screenshot_dir = os.path.join(screenshots_base, "source", f"{process_name}_screen")
                        else:
                            screenshot_dir = os.path.join(screenshots_base, "resolution", resolution, f"{process_name}_screen")

                        if not os.path.isdir(screenshot_dir):
                            print(f"WARNING: {resolution} → {screenshot_dir}")
                            continue

                        image_files = sorted([
                            os.path.join(screenshot_dir, f)
                            for f in os.listdir(screenshot_dir)
                            if f.lower().endswith(".png")
                        ])

                        if not image_files:
                            print(f"WARNING: {screenshot_dir}")
                            continue
                        output_root = os.path.join(output_base, prompt_type, resolution)
                        folder_name = str(shared_output_index[prompt_type][resolution])
                        output_folder = os.path.join(output_root, folder_name)
                        os.makedirs(output_folder, exist_ok=True)

                        print(f"OUTPUT: {output_folder}")

                        executor.submit(
                            generate_test,
                            project, process_name, html_data,
                            prompt_type, resolution, prompt_template,
                            image_files, output_folder
                        )

print(f"FIN {(time.time() - start_time):.2f} seconds")

