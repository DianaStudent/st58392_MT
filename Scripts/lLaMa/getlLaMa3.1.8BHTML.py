import json
import os
import requests
import time
from concurrent.futures import ThreadPoolExecutor

projects = ["Cezerin", "shopizer", "prestashop", "nopCommerce"]
prompt_types = ["simple", "medium", "detailed"]
iterations = 3 
base_dir = r"C:\Diana\MasterCode\Code\Projects"
llava_url = "http://localhost:11434/api/generate"
code_model = "llama3.1:8b"
start_time = time.time()
def generate_test_llama_only(project, process_name, html_data, llama_prompt, output_folder):
    try:
        html_prompt = llama_prompt.format(
            process_name=process_name,
            html_data=json.dumps(html_data, indent=2)
        )
        payload_llama = {
            "model": code_model,
            "prompt": html_prompt,
            "stream": False
        }
        response_llama = requests.post(llava_url, json=payload_llama, timeout=180)
        result = response_llama.json().get("response", "").strip()
        if "```python" in result:
            generated_code = result.split("```python")[1].split("```")[0].strip()
        else:
            generated_code = result
        filename = f"test_{process_name}.py"
        filepath = os.path.join(output_folder, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(generated_code)
        print(f"SUCCESS: {project}/{process_name} → {filename}")
    except Exception as e:
        print(f"ERROR: {project}/{process_name}: {e}")
for project in projects:
    project_path = os.path.join(base_dir, project, "Processes")
    output_base = os.path.join(project_path, "tests", "llamaHTML", "zeroshot")
    existing = []
    if os.path.exists(output_base):
        for d in os.listdir(output_base):
            if d.isdigit():
                existing.append(int(d))
    existing = sorted(set(existing))
    next_index = (existing[-1] + 1) if existing else 1
    iteration_indices = list(range(next_index, next_index + iterations))
    for iteration in iteration_indices:
        print(f"ITERATION: {iteration}")
        input_structures = os.path.join(project_path, "data", "cleanData")
        prompts_base = os.path.join(project_path, "data", "prompts", "llamaHTML", "zeroshot")
        with ThreadPoolExecutor(max_workers=1) as executor:
            ui_html_path = os.path.join(input_structures, "UI_html.json")
            if os.path.isfile(ui_html_path):
                with open(ui_html_path, "r", encoding="utf-8") as f:
                    ui_html_dict = json.load(f)
                for ui_process_name, html_raw in ui_html_dict.items():
                    html_data = {"html": html_raw}
                    for prompt_type in prompt_types:
                        llama_prompt_file = os.path.join(prompts_base, f"ui_{prompt_type}_llama_prompt.txt")
                        if not os.path.isfile(llama_prompt_file):
                            continue
                        with open(llama_prompt_file, "r", encoding="utf-8") as f:
                            llama_prompt = f.read()
                        output_folder = os.path.join(output_base, "ui", prompt_type, "noimg", str(iteration))
                        os.makedirs(output_folder, exist_ok=True)
                        executor.submit(
                            generate_test_llama_only,
                            project, ui_process_name, html_data,
                            llama_prompt, output_folder
                        )
            html_files = [f for f in os.listdir(input_structures) if f.endswith("_html.json") and not f.startswith("UI")]
            for html_file in html_files:
                process_name = html_file.replace("_html.json", "")
                with open(os.path.join(input_structures, html_file), "r", encoding="utf-8") as f:
                    html_data = json.load(f)
                for prompt_type in prompt_types:
                    llama_prompt_file = os.path.join(prompts_base, f"{process_name}_{prompt_type}_llama_prompt.txt")
                    if not os.path.isfile(llama_prompt_file):
                        continue
                    with open(llama_prompt_file, "r", encoding="utf-8") as f:
                        llama_prompt = f.read()
                    output_folder = os.path.join(output_base, prompt_type, "noimg", str(iteration))
                    os.makedirs(output_folder, exist_ok=True)
                    executor.submit(
                        generate_test_llama_only,
                        project, process_name, html_data,
                        llama_prompt, output_folder
                    )
print(f"FIN {(time.time() - start_time).total_seconds():.2f} seconds")
