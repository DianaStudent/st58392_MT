## Prerequisites

For correct execution of the pipeline, the following components must be installed and configured:

**Valid API keys**  
 API credentials (for OpenAI and VertexAI) must be saved in maps:

- `Scripts/gemini`
- `Scripts/gpt4o`
- `Scripts/loop`

**Locally installed LLM models**  
Open-source models must be downloaded, configured, and fully operational on the local machine:

- `LLaVA-LLaMA3.1:8B`
- `LLaVA-7B`
- `LLaVA-LLaMA3`

**Locally deployed web applications**  
 All target systems (Cezerin, nopCommerce, PrestaShop, Shopizer) must be installed and accessible on `localhost`.
All of them are available in GitHub:

- Cezerin https://github.com/Cezerin/cezerin
- nopCommerce https://github.com/nopSolutions/nopCommerce
- PrestaShop https://github.com/PrestaShop/PrestaShop
- Shopizer https://github.com/shopizer-ecommerce/shopizer
- Medusa https://github.com/medusajs/medusa

## Project Contents

The repository is organized into the following top-level components:

- **Projects/**  
  Contains per-application folders (`Cezerin`, `Medusa`, `nopCommerce`, `PrestaShop`, `Shopizer`), each including:

  - `Data/` — HTML data, prompts, screenshots
  - `GeneratedTests/` — structured outputs of test generation and execution

- **Scripts/**  
  All core pipeline logic:

  - `compress_html/` — HTML cleaning scripts per project
  - `gpt/`, `gemini/`, `lLaMa/` — test generation scripts for each model
  - `loop/` — feedback-loop generation
  - `manualValidation/` — fix scripts used during and after manual validation
  - `mutation/` — mutation testing scripts
  - `resolution_scr/`— screenshot resolutions scripts
  - `testExecution/` — running and evaluating generated tests

- **Visualizations/**  
  Reports and artifacts used for evaluation and documentation:

  - `ManualValidation/` — manually annotated CSV file
  - `Results/` — final evaluation outputs and summary notebooks
  - `StateOfTheArt/` — citation data and visualizations for the literature review

- **README.md**  
  Pipeline documentation and usage guide.

## Project Contents

## 1. Data Collection

Each project has a dedicated script folder for collecting DOM structure (HTML) and screenshots for specific user flows.

### 1.1 Script Location

All data collection scripts are located at:
`Projects/<ProjectName>/Data/getData/`

Each script corresponds to a specific user flow based on projects. Example filenames:

- `getDataAddtocart.py`
- `getDataCheckout.py`
- `getDataFilter.py`
- `getDataLogin.py`
- `getDataRegister.py`
- `getDataUi.py`

Scripts are specific to each project, but follow the same naming and structure.

### 1.2 Output Locations

- **HTML structure (as JSON):**
  `Projects/<ProjectName>/Data/getData/sourceData/`

### 1.3 How to Run

Run Web App via Docker or CMD
To collect data for a specific process:

<pre>cd Projects/&lt;ProjectName&gt;/Data/getData 
python getData&lt;ProcessName&gt;.py</pre>

## 2. Data Preprocessing

### 2.1 HTML Cleaning

For each project, a dedicated script is used to clean and compress the raw HTML files by removing irrelevant tags, styles and scripts.

- Scripts are located at:
  `Scripts/compress_html/`

Examples:

- `compressHTMLceserin.py`
- `compressHTMLnopcommerce.py`
- `compressHTMLprestashop.py`
- `compressHTMLshopizer.py`

- Output cleaned HTML files are saved as JSON:
  `Projects/<ProjectName>/Data/cleanData/<process>\_html.json`

### 2.2 Screenshot Resolution Generation

To create resolution-specific versions of screenshots (for simulating different screen sizes), the following script is used:
`Scripts/resolution_scr/resolutionCh.py` - For each screenshot set, resized copies are created in the following resolutions:

- `672x672`
- `768x768`
- `1024x1024`

- Output folder structure:
  `Projects/<ProjectName>/Data/screenshots/resolution/<resolution>/<process>\_screen`
  Example:
  `Projects/Cezerin/Data/screenshots/resolution/672/addtocart_screen/addtocart_screen1.png`

### 2.3 How to Run

Run the corresponding cleaning script:

<pre>cd Scripts/compress_html
python compressHTML<project>.py</pre>

Run screenshot rescaling:

<pre>cd Scripts/resolution_scr
python resolutionCh.py</pre>

## 3. Prompt Management

Prompts are manually created and stored per model, project and task type. Each prompt is tied to a specific user process and level of detail.

### 3.1 Prompt Folders

Prompts are stored under:
`Projects/<ProjectName>/Data/prompts/<ModelName>/<PromptType>/`

#### Prompt types:

- zeroshot/ — written prompts with 3 deatail level - simple, medium and detailed
- feedback/ — initial prompts + updated versions for feedback loop

Example (GPT-4o, Cezerin):
`Projects/Cezerin/Data/prompts/gpt4o/zeroshot/`
`Projects/Cezerin/Data/prompts/gpt4o/feedback/`

Each file follows the naming pattern:
`<process>_<complexity>_prompt.txt`
e.g.:

- `addtocart_detailed_prompt.txt`
- `checkout_loop_prompt.txt`
- `filter_initial_prompt.txt`

## 4. Script Execution and Test Generation

All test generation and evaluation scripts are located in the `Scripts/` directory. They are organized into subfolders based on their functionality: model type, generation strategy, mutation handling and test execution.

### 4.1. Subfolders and Core Scripts

- **gemini/**  
  Test generation using Gemini-2.0-flash-001. API KEYS AREN'T NOT PROVIDED
  - `getGemini.py` — for test generation in full data mode (HTML + screenshots)
  - `getGeminiHTML.py` — for test generation in partial data mode (HTML-only)

<pre>cd Scripts/gemini
python getGemini.py</pre>

- **gpt/**  
  Test generation using GPT-4o. API KEYS AREN'T NOT PROVIDED
  - `getGPT.py` — for functional test generation in full data mode (HTML + screenshots)
  - `getGPTui.py` — for UI test generation in full data mode (HTML + screenshots)
  - `getGPTHTML.py` — for all test generation in partial data mode (HTML only)

<pre>cd Scripts/gpt
python getGPT.py</pre>

- **lLaMa/**  
  Scripts for LLaMA-based test generation across different model sizes.

  - `getLLaMa3.py` — for test generation in full data mode (HTML + screenshots) with LLaVA-LLaMA3 (llava-llama-3-8b-v1.1)
  - `getLLaMa3HTML.py` — for test generation in partial data mode (HTML-only) with LLaVA-LLaMA3 (llava-llama-3-8b-v1.1)
  - `getLLaMa3.1.8B.py` — for test generation in full data mode (HTML + screenshots) with LLaVA:7b combined with LLaMA3.1:8b
  - `getLLaMa3.1.8BHTML.py` — for test generation in partial data mode (HTML-only) with LLaMA3.1:8b

<pre>cd Scripts/lLaMa
python getLLaMa3.1.8B.py</pre>

- **loop/**  
  Implements multi-step test generation with feedback loop.
  - `getGPTLoop.py` — performs iterative generation using GPT-4o and adaptive prompts.
  - `getGeminiLoop.py` — performs iterative generation using Gemini-2.0-flash-001 and adaptive prompts.
  - `collectLoopResults.py` — aggregates outputs across feedback iterations.

<pre>cd Scripts/loop
python getGPTLoop.py</pre>

- **testExecution/**  
  Scripts for running generated tests, collecting execution statistics and generates reports.

  - `runTestsBatch.py` — main test runner; splits execution into small batches (25 tests) for performance.
  - `runAll.py` — script called by `runTestsBatch.py` to execute each batch.
  - `step_counter_patch.py` — counts executed steps per test without modifying the test source code. Used internally by `runAll.py`.

<pre>cd Scripts/testExecution
python runTestsBatch.py</pre>

- **mutation/**  
  Scripts for performing mutation testing to evaluate test robustness under changes in UI structure or functionality.

  - `collectSuccess.py` — selects and copies only the tests that passed in the original (non-mutated) execution phase. These are used as input for mutation testing.
  - `runTestsMut.py` — executes existing successful tests under mutation conditions (e.g., removed buttons, layout changes). Logs execution results to `mutation_report_FIN.csv`, including expected outcomes and pass/fail mismatches.

<pre>
cd Scripts/mutation
python collectSuccess.py     # Collects successful original tests
python runTestsMut.py        # Executes tests under mutation and logs results
</pre>

### 4.2 Output File Structure

All generated outputs are saved under the corresponding project folder inside `Projects/<ProjectName>/GeneratedTests/`

#### Test Outputs (`tests/`)

Initial generated test scripts are saved in structured directories based on:

- Model used (`gpt4o`, `gemini`, `llava7bllama3.1.8b`, etc.)
- Prompt type (`zeroshot`, `feedback`, `ui`)
- Prompt complexity (`simple`, `medium`, `detailed`)
- Screenshot resolution (`672`, `768`, `1024`)
- Run number (`1`, `2`, `3`, ...)

`Projects/<ProjectName>/GeneratedTests/tests/<Model>/<PromptType>/<Complexity>/<Resolution>/<RunNumber>/`

Examples:

`Projects/Cezerin/GeneratedTests/tests/gpt4o/zeroshot/simple/1024/2/test_addtocart.py`
`Projects/nopCommerce/GeneratedTests/tests/llava7bllama3.1.8b/ui/detailed/768/1/test_filter.py`
`Projects/PrestaShop/GeneratedTests/tests/geminiHTML/feedback/medium/3/test_checkout.py`

_For HTML-only generations, the `<Resolution>` folder is omitted._

#### Test Outputs (`testsURLchange/`)

This folder contains updated versions of initially generated tests (`tests/`) with corrected or normalized URLs.

- Files were copied from `tests/`
- The script `scripts/manualValidation/URLUpdate.py` automatically fixed incorrect or inconsistent URLs inside test scripts.

<pre>
cd scripts/manualValidation
python URLUpdate.py
</pre>

---

#### Test Outputs (`testsDriverChange/`)

This folder contains updated versions of tests with corrected or improved WebDriver interaction logic.

- Files were copied from `testsURLchange/`.
- The script `scripts/manualValidation/driverUpdate.py` was used to fix known issues with driver configuration.

<pre>
cd scripts/manualValidation
python driverUpdate.py
</pre>

---

#### Test Outputs (`failed/`)

After running tests from `testsDriverChange/`, failed tests were fixed:

- The script `scripts/manualValidation/copyFailed.py` copied only failing tests from `testsURLchange/` into `failed/`.
- `fixClick.py` applied automatic fixes to wrong `.click()` elements and replaced `presence_of_element_located` ↔ `element_to_be_clickable` depending on defined rules.

<pre>
python copyFailed.py
python fixClick.py
</pre>

#### Example: Full Recovery Flow

A typical post-validation flow for one project (e.g., `shopizer`) looks like:

<pre>
cd scripts/manualValidation

# 1. Fix URLs in validated tests
python URLUpdate.py

# 2. Fix driver logic
python driverUpdate.py

# 3. Run all tests in batches
cd ../testExecution
python runTestsBatch.py

# 4. Extract failures and patch click errors
cd ../manualValidation
python copyFailed.py
python fixClick.py
</pre>

This workflow allows semi-automated recovery and repair of partially broken LLM-generated tests after initial generation.

#### Feedback Loop Outputs

Scripts executed via `getGPTLoop.py` or `getGeminiLoop.py` produce structured outputs per iteration:

`Projects/<ProjectName>/GeneratedTests/tests/<Model>/feedback/<RunNumber>/`

loops/ # All looped generations per prompt
success/ # Final successful version (if any)

Example:
`Projects/Shopizer/GeneratedTests/tests/gpt4o/feedback/3/success/test_addtocart.py`

#### Reports and Logs

Evaluation summaries, logs and feedback/mutation results are saved under:
`Visualizations/`
Key files:

- `all_fulldump_fin.csv` — full execution dump
- `mutation_report_FIN.csv` — generated by `runTestsMut.py`
- `feedback_report_all_FIN.csv` — feedback loop statistics
- `resultsFIN.ipynb` — plotting and evaluation notebook

---

All generated tests are saved as standalone `.py` scripts and are executable via `runTestsBatch.py`
