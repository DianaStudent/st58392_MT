import json
import os
import requests
import time
from concurrent.futures import ThreadPoolExecutor

projects = ["Cezerin", "shopizer", "prestashop", "nopCommerce"]
prompt_types = ["simple", "medium", "detailed"]
iterations = 1
start_time = time.time()
base_path = r"C:\Diana\MasterCode\Code\Projects"
model_name = "llava-llama3:latest"
llava_url = "http://localhost:11434/api/generate"

def generate_test(process_name, html_data, llama_prompt, output_folder):
    try:
        prompt = llama_prompt.format(
            process_name=process_name,
            html_data=json.dumps(html_data, indent=2)
        )
        response = requests.post(llava_url, json={
            "model": model_name,
            "prompt": prompt,
            "stream": False
        }, timeout=180)
        result = response.json().get("response", "").strip()
        if "```python" in result:
            code = result.split("```python")[1].split("```")[0].strip()
        else:
            code = result
        filename = f"test_{process_name}.py"
        filepath = os.path.join(output_folder, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"SUCCESS: {project}/{process_name} → {filename}")
    except Exception as e:
        print(f"ERROR: {process_name}: {e}")

for project in projects:
    project_path = os.path.join(base_path, project, "Processes")
    input_structures = os.path.join(project_path, "data", "cleanData")
    prompts_base = os.path.join(project_path, "data", "prompts", "llamaHTML", "zeroshot")
    output_base = os.path.join(project_path, "tests", "llava-llamav3HTML", "zeroshot")
    for iteration in range(iterations):
        print(f"ITERATION: {iteration + 1}")
        with ThreadPoolExecutor(max_workers=1) as executor:
            ui_html_path = os.path.join(input_structures, "UI_html.json")
            if os.path.isfile(ui_html_path):
                with open(ui_html_path, "r", encoding="utf-8") as f:
                    ui_html_dict = json.load(f)
                for ui_name, html_raw in ui_html_dict.items():
                    html_data = {"html": html_raw}
                    for prompt_type in prompt_types:
                        try:
                            prompt_file = os.path.join(prompts_base, f"ui_{prompt_type}_llama_prompt.txt")
                            if not os.path.isfile(prompt_file):
                                continue
                            with open(prompt_file, "r", encoding="utf-8") as f:
                                llama_prompt = f.read()
                        except Exception:
                            continue
                        out_folder = os.path.join(output_base, "ui", prompt_type, "noimg", str(iteration + 1))
                        os.makedirs(out_folder, exist_ok=True)
                        executor.submit(generate_test, ui_name, html_data, llama_prompt, out_folder)
            html_files = [f for f in os.listdir(input_structures) if f.endswith("_html.json") and not f.startswith("UI")]
            for html_file in html_files:
                process_name = html_file.replace("_html.json", "")
                with open(os.path.join(input_structures, html_file), "r", encoding="utf-8") as f:
                    html_data = json.load(f)
                for prompt_type in prompt_types:
                    try:
                        prompt_file = os.path.join(prompts_base, f"{process_name}_{prompt_type}_llama_prompt.txt")
                        if not os.path.isfile(prompt_file):
                            continue
                        with open(prompt_file, "r", encoding="utf-8") as f:
                            llama_prompt = f.read()
                    except Exception:
                        continue
                    out_folder = os.path.join(output_base, prompt_type, "noimg", str(iteration + 1))
                    os.makedirs(out_folder, exist_ok=True)
                    executor.submit(generate_test, process_name, html_data, llama_prompt, out_folder)
print(f"FIN {(time.time() - start_time):.2f} seconds")

