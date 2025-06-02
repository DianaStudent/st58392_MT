import json
import os
import requests
import base64
import time
from concurrent.futures import ThreadPoolExecutor

projects = ["Cezerin", "shopizer", "prestashop", "nopCommerce"]
prompt_types = ["simple", "medium", "detailed"]
resolutions = ["source", "672"]
iterations = 1
start_time = time.time()
base_path = r"C:\Diana\MasterCode\Code\Projects"
model_name = "llava-llama3:latest"
llava_url = "http://localhost:11434/api/generate"

def load_prompt_template(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
def encode_images(image_paths):
    encoded = []
    names = []
    for img_path in image_paths:
        with open(img_path, "rb") as f:
            encoded.append(base64.b64encode(f.read()).decode("utf-8"))
            names.append(os.path.basename(img_path))
    return encoded, names
def generate_test(process_name, html_data, prompt_llava, prompt_llama, image_files, output_folder):
    try:
        encoded_images, image_names = encode_images(image_files)
        prompt_screens = prompt_llava.format(process_name=process_name, screenshot_names=", ".join(image_names))

        response1 = requests.post(llava_url, json={
            "model": model_name,
            "prompt": prompt_screens,
            "images": encoded_images,
            "stream": False
        }, timeout=180)
        screen_description = response1.json().get("response", "").strip()
        final_prompt = prompt_llama.format(
            process_name=process_name,
            html_data=json.dumps(html_data, indent=2),
            screen_description=screen_description
        )
        response2 = requests.post(llava_url, json={
            "model": model_name,
            "prompt": final_prompt,
            "stream": False
        }, timeout=180)
        result = response2.json().get("response", "").strip()
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
    screenshots_base = os.path.join(project_path, "data", "screenshots")
    prompts_base = os.path.join(project_path, "data", "prompts", "llava7b-llama3.18b", "zeroshot")
    output_base = os.path.join(project_path, "tests", "llava-llama3-latest", "zeroshot")
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
                            llava_prompt = load_prompt_template(os.path.join(prompts_base, f"ui_{prompt_type}_llava_prompt.txt"))
                            llama_prompt = load_prompt_template(os.path.join(prompts_base, f"ui_{prompt_type}_llama_prompt.txt"))
                        except Exception as e:
                            continue
                        for res in resolutions:
                            if res == "source":
                                screenshot_dir = os.path.join(screenshots_base, "source", "UI", ui_name)
                            else:
                                screenshot_dir = os.path.join(screenshots_base, "resolution", res, "UI", ui_name)
                            if not os.path.isdir(screenshot_dir):
                                continue
                            image_files = [
                                os.path.join(screenshot_dir, f)
                                for f in os.listdir(screenshot_dir)
                                if f.lower().endswith((".png", ".jpg", ".jpeg"))
                            ]
                            if not image_files:
                                continue
                            out_folder = os.path.join(output_base, "ui", prompt_type, res, str(iteration + 1))
                            os.makedirs(out_folder, exist_ok=True)
                            executor.submit(generate_test, ui_name, html_data, llava_prompt, llama_prompt, image_files, out_folder)
            html_files = [f for f in os.listdir(input_structures) if f.endswith("_html.json") and not f.startswith("UI")]
            for html_file in html_files:
                process_name = html_file.replace("_html.json", "")
                with open(os.path.join(input_structures, html_file), "r", encoding="utf-8") as f:
                    html_data = json.load(f)
                for prompt_type in prompt_types:
                    try:
                        llava_prompt = load_prompt_template(os.path.join(prompts_base, f"{process_name}_{prompt_type}_llava_prompt.txt"))
                        llama_prompt = load_prompt_template(os.path.join(prompts_base, f"{process_name}_{prompt_type}_llama_prompt.txt"))
                    except Exception:
                        continue
                    for res in resolutions:
                        if res == "source":
                            screenshot_dir = os.path.join(screenshots_base, "source", f"{process_name}_screen")
                        else:
                            screenshot_dir = os.path.join(screenshots_base, "resolution", res, f"{process_name}_screen")
                        if not os.path.isdir(screenshot_dir):
                            continue
                        image_files = [
                            os.path.join(screenshot_dir, f)
                            for f in os.listdir(screenshot_dir)
                            if f.lower().endswith((".png", ".jpg", ".jpeg"))
                        ]
                        if not image_files:
                            continue
                        out_folder = os.path.join(output_base, prompt_type, res, str(iteration + 1))
                        os.makedirs(out_folder, exist_ok=True)
                        executor.submit(generate_test, process_name, html_data, llava_prompt, llama_prompt, image_files, out_folder)

print(f"FIN {(time.time() - start_time):.2f} seconds")

