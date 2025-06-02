import openai
import json
import os
import time
from openai import OpenAI
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor

load_dotenv("openai_key.env")
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
start_time = time.time()

projects = ["Cezerin", "prestashop", "shopizer", "nopCommerce", "medusa"]
prompt_types = ["simple", "medium", "detailed"]
base_dir = r"C:\Diana\Master\MasterCode\code\Projects"

def generate_test(project, process_name, html_data, prompt_type, prompt_template, output_folder, max_retries=3):
    retries = 0
    while retries < max_retries:
        try:
            messages = [{
                "role": "user",
                "content": [{"type": "text", "text": prompt_template.format(html_data=json.dumps(html_data, indent=2))}]
            }]

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
                print(f"WAIT: {process_name} ({prompt_type}), {wait_time} seconds...")
                time.sleep(wait_time)
                retries += 1
            else:
                print(f"ERROR: {process_name} ({prompt_type}): {e}")
                return
    print(f"ERROR: {process_name} ({prompt_type})")


for iteration in range(3):
    print(f"ITERATION: {iteration + 1}")

    for project in projects:
        print(f"PROJECT: {project}")
        project_path = os.path.join(base_dir, project, "Processes")

        input_structures = os.path.join(project_path, "data", "cleanData")
        prompts_base = os.path.join(project_path, "data", "prompts", "llamaHTML", "zeroshot")
        output_base = os.path.join(project_path, "tests", "gpt4oHTML", "zeroshot")

        shared_output_index = {}
        for prompt_type in prompt_types:
            output_root = os.path.join(output_base, prompt_type)
            os.makedirs(output_root, exist_ok=True)
            existing_folders = [f for f in os.listdir(output_root) if f.isdigit()]
            next_index = 1 + max([int(f) for f in existing_folders], default=0)
            shared_output_index[prompt_type] = next_index

        ui_html_path = os.path.join(input_structures, "UI_html.json")
        if os.path.isfile(ui_html_path):
            
            with open(ui_html_path, "r", encoding="utf-8") as f:
                html_dict = json.load(f)

            for process_name, raw_html in html_dict.items():
                html_data = {"html": raw_html}

                with ThreadPoolExecutor(max_workers=3) as executor:
                    for prompt_type in prompt_types:
                        prompt_file = os.path.join(prompts_base, f"ui_{prompt_type}_prompt.txt")
                        if not os.path.isfile(prompt_file):
                            continue

                        with open(prompt_file, "r", encoding="utf-8") as f:
                            prompt_template = f.read().strip()

                        output_root = os.path.join(output_base, prompt_type)
                        folder_name = str(shared_output_index[prompt_type])
                        output_folder = os.path.join(output_root, folder_name)
                        os.makedirs(output_folder, exist_ok=True)

                        print(f"OUTPUT: {output_folder}")

                        executor.submit(
                            generate_test,
                            project, process_name, html_data,
                            prompt_type, prompt_template, output_folder
                        )

        for json_file in os.listdir(input_structures):
            if not json_file.endswith("_html.json") or json_file == "UI_html.json":
                continue

            process_name = json_file.replace("_html.json", "")
            print(f"PROCESS: {process_name}")

            with open(os.path.join(input_structures, json_file), "r", encoding="utf-8") as f:
                html_data = json.load(f)

            with ThreadPoolExecutor(max_workers=3) as executor:
                for prompt_type in prompt_types:
                    prompt_file = os.path.join(prompts_base, f"{process_name}_{prompt_type}_llama_prompt.txt")
                    if not os.path.isfile(prompt_file):
                        continue

                    with open(prompt_file, "r", encoding="utf-8") as f:
                        prompt_template = f.read().strip()

                    output_root = os.path.join(output_base, prompt_type)
                    folder_name = str(shared_output_index[prompt_type])
                    output_folder = os.path.join(output_root, folder_name)
                    os.makedirs(output_folder, exist_ok=True)

                    print(f"OUTPUT: {output_folder}")

                    executor.submit(
                        generate_test,
                        project, process_name, html_data,
                        prompt_type, prompt_template, output_folder
                    )

print(f"FIN {(time.time() - start_time).total_seconds():.2f} seconds")
