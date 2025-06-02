import json
import os
import requests
import base64
import time
from concurrent.futures import ThreadPoolExecutor

#projects = ["Cezerin", "shopizer", "prestashop", "nopCommerce"]
projects = ["medusa"]
prompt_types = ["simple", "medium", "detailed"]
resolutions = ["source", "672"]
folder_number = 2 
iterations = 1    
#manual_process_list = ["login", "register", "checkout", "addtocart"]
manual_process_list = ["login"]
base_dir = r"C:\Diana\MasterCode\Code\Projects"
llava_url = "http://localhost:11434/api/generate"
text_model = "llava:7b"
code_model = "llama3.1:8b"
start_time = time.time()

def generate_test(project, process_name, html_data, prompt_template, image_files, output_folder):
    try:
        encoded_screenshots = []
        screenshot_names = []
        for img_path in image_files:
            with open(img_path, "rb") as f:
                encoded = base64.b64encode(f.read()).decode("utf-8")
                encoded_screenshots.append(encoded)
                screenshot_names.append(os.path.basename(img_path))
        prompt_screens = prompt_template['llava'].format(
            process_name=process_name,
            screenshot_names=", ".join(screenshot_names)
        )
        payload_llava = {
            "model": text_model,
            "prompt": prompt_screens,
            "images": encoded_screenshots,
            "stream": False
        }
        response_llava = requests.post(llava_url, json=payload_llava, timeout=180)
        screen_description = response_llava.json().get("response", "").strip()
        html_prompt = prompt_template['llama'].format(
            process_name=process_name,
            html_data=json.dumps(html_data, indent=2),
            screen_description=screen_description
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
for iteration in range(iterations):
    print(f"ITERATION: {iteration + 1}")
    for project in projects:
        project_path = os.path.join(base_dir, project, "Processes")
        input_structures = os.path.join(project_path, "data", "cleanData")
        screenshots_base = os.path.join(project_path, "data", "screenshots")
        prompts_base = os.path.join(project_path, "data", "prompts", "llava7b-llama3.18b", "zeroshot")
        output_base = os.path.join(project_path, "tests", "llava7b-llama3.18b", "zeroshot")
        ui_html_path = os.path.join(input_structures, "UI_html.json")
        if os.path.isfile(ui_html_path):
            with open(ui_html_path, "r", encoding="utf-8") as f:
                ui_html_dict = json.load(f)
            for ui_process_name, html_raw in ui_html_dict.items():
                html_data = {"html": html_raw}
                with ThreadPoolExecutor(max_workers=1) as executor:
                    for prompt_type in prompt_types:
                        llava_prompt_file = os.path.join(prompts_base, f"ui_{prompt_type}_llava_prompt.txt")
                        llama_prompt_file = os.path.join(prompts_base, f"ui_{prompt_type}_llama_prompt.txt")
                        if not (os.path.isfile(llava_prompt_file) and os.path.isfile(llama_prompt_file)):
                            continue
                        with open(llava_prompt_file, "r", encoding="utf-8") as f:
                            llava_prompt = f.read()
                        with open(llama_prompt_file, "r", encoding="utf-8") as f:
                            llama_prompt = f.read()
                        for resolution in resolutions:
                            if resolution == "source":
                                screenshot_dir = os.path.join(screenshots_base, "source", "UI", ui_process_name)
                            else:
                                screenshot_dir = os.path.join(screenshots_base, "resolution", resolution, "UI", ui_process_name)
                            if not os.path.isdir(screenshot_dir):
                                continue
                            image_files = sorted([
                                os.path.join(screenshot_dir, f)
                                for f in os.listdir(screenshot_dir)
                                if f.lower().endswith(('.png'))
                            ])
                            if not image_files:
                                continue
                            output_folder = os.path.join(output_base, prompt_type, resolution, str(folder_number))
                            os.makedirs(output_folder, exist_ok=True)
                            executor.submit(
                                generate_test,
                                project, ui_process_name, html_data,
                                {"llava": llava_prompt, "llama": llama_prompt},
                                image_files, output_folder
                            )
        html_files = [f for f in os.listdir(input_structures) if f.endswith("_html.json") and not f.startswith("UI")]
        for html_file in html_files:
            process_name = html_file.replace("_html.json", "")
            if manual_process_list and process_name not in manual_process_list:
                continue
            with open(os.path.join(input_structures, html_file), "r", encoding="utf-8") as f:
                html_data = json.load(f)
            with ThreadPoolExecutor(max_workers=1) as executor:
                for prompt_type in prompt_types:                
                    llava_prompt_file = os.path.join(prompts_base, f"{process_name}_{prompt_type}_llava_prompt.txt")
                    llama_prompt_file = os.path.join(prompts_base, f"{process_name}_{prompt_type}_llama_prompt.txt")
                    if not (os.path.isfile(llava_prompt_file) and os.path.isfile(llama_prompt_file)):
                        continue
                    with open(llava_prompt_file, "r", encoding="utf-8") as f:
                        llava_prompt = f.read()
                    with open(llama_prompt_file, "r", encoding="utf-8") as f:
                        llama_prompt = f.read()                    
                    for resolution in resolutions:
                        if resolution == "source":
                            screenshot_dir = os.path.join(screenshots_base, "source", f"{process_name}_screen")
                        else:
                            screenshot_dir = os.path.join(screenshots_base, "resolution", resolution, f"{process_name}_screen")
                        if not os.path.isdir(screenshot_dir):
                            continue
                        image_files = sorted([
                            os.path.join(screenshot_dir, f)
                            for f in os.listdir(screenshot_dir)
                            if f.lower().endswith(('.png', '.jpg', '.jpeg'))
                        ])
                        if not image_files:
                            continue
                        output_folder = os.path.join(output_base, prompt_type, resolution, str(folder_number))
                        os.makedirs(output_folder, exist_ok=True)
                        executor.submit(
                            generate_test,
                            project, process_name, html_data,
                            {"llava": llava_prompt, "llama": llama_prompt},
                            image_files, output_folder
                        )

print(f"FIN {(time.time() - start_time):.2f} seconds")

