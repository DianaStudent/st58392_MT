## Prerequisites

For correct execution of the pipeline, the following components must be installed and configured:

- **Locally deployed web applications**  
   All target systems (Cezerin, nopCommerce, PrestaShop, Shopizer) must be installed and accessible on `localhost`.
  All of them are available in GitHub:
  Cezerin https://github.com/Cezerin/cezerin
  nopCommerce https://github.com/nopSolutions/nopCommerce
  PrestaShop https://github.com/PrestaShop/PrestaShop
  Shopizer https://github.com/shopizer-ecommerce/shopizer
  Medusa https://github.com/medusajs/medusa

## 1. Data Collection

Each project has a dedicated script folder for collecting DOM structure (HTML) and screenshots for specific user flows.

### 1.1 Script Location

All data collection scripts are located at:
code/Projects/<ProjectName>/Data/getData/

Each script corresponds to a specific user flow based on projects. Example filenames:

- getDataAddtocart.py
- getDataCheckout.py
- getDataFilter.py
- getDataLogin.py
- getDataRegister.py
- getDataUi.py

Scripts are specific to each project, but follow the same naming and structure convention.

### 1.2 Output Locations

- **HTML structure (as JSON):**
  code/Projects/<ProjectName>/Data/getData/sourceData/

### 1.3 How to Run

Run App via Docker or CMD
To collect data for a specific process:
cd code/Projects/<ProjectName>/Data/getData
python getData<ProcessName>.py

## 2. Data Preprocessing

### 2.1 HTML Cleaning

For each project, a dedicated script is used to clean and compress the raw HTML files by removing irrelevant tags, styles, and scripts.

- Scripts are located at:
  code/Scripts/compress_html/
  Examples:

  - compressHTMLceserin.py
  - compressHTMLnopcommerce.py
  - compressHTMLprestashop.py
  - compressHTMLshopizer.py

  - Output cleaned HTML files are saved as JSON:
    code/Projects/<ProjectName>/Data/cleanData/<process>\_html.json

### 2.2 Screenshot Resolution Generation

To create resolution-specific versions of screenshots (for simulating different screen sizes), the following script is used:
code/Scripts/resolution_scr/resolutionCh.py - For each screenshot set, resized copies are created in the following resolutions: - 672x672 - 768x768 - 1024x1024

    - Output folder structure:
    	code/Projects/<ProjectName>/Data/screenshots/resolution/<resolution>/<process>_screen/
    Example:
    	code/Projects/Cezerin/Data/screenshots/resolution/672/addtocart_screen/

### 2.3 How to Run

Run the corresponding cleaning script:
cd code/Scripts/compress_html
python compressHTML<project>.py
Run screenshot rescaling:
cd code/Scripts/resolution_scr
python resolutionCh.py

## 3. Prompt Management

Prompts are manually created and stored per model, project, and task type. Each prompt is tied to a specific user process (e.g., Add to Cart, Checkout) and level of detail.

### 3.1 Prompt Folders

Prompts are stored under:
code/Projects/<ProjectName>/Data/prompts/<ModelName>/<PromptType>/

#### Prompt types:

- zeroshot/ — manually written base prompts
- feedback/ — initial prompts + updated versions for feedback loop

Example (GPT-4o, Cezerin):
code/Projects/Cezerin/Data/prompts/gpt4o/zeroshot/
code/Projects/Cezerin/Data/prompts/gpt4o/feedback/

Each file follows the naming pattern:
<process>\_<complexity>\_prompt.txt
e.g.: - addtocart_detailed_prompt.txt - checkout_loop_prompt.txt - filter_initial_prompt.txt

### 3.2 LLaVA-Compatible Prompts

To convert existing GPT-4o prompts to be compatible with LLaVA (different image processing format), two scripts are used:
code/Scripts/prompts/prepLlamaPrompts.py
code/Scripts/prompts/prepLlamaPromtsHTML.py - These scripts take existing GPT-4o prompts and modify them to fit LLaVA’s expected input format. - One script is for screenshot-based prompts, the other — for HTML-only cases.

## 4. Script Execution and Test Generation

All scripts are organized into logical subfolders based on functionality: model type, purpose, or execution role.

### 4.1 Script Structure

Scripts are located at:
code/Scripts/<Category>/

#### Script Categories:

- **Loop/**

  - getGPTLoop.py — performs iterative test generation using GPT-4o with feedback loop.
  - collectLoopResults.py — collects and structures outputs from GPT-4o feedback loop generations.

- **gemini/** - NEED UPDATE

  - getGPT.py — generates Selenium tests using GPT-4o with HTML + screenshots.
  - getGPTui.py — generates UI-specific test cases using GPT-4o.
  - getGPTuiHTML.py — same as above but without screenshots.
  - getGPTHTML.py — experimental script for HTML-only prompt generation.
  - openai_key.env — OpenAI key for accessing GPT-4o. **NOT PROVIDED IN REPO**

- **gpt/**

  - getGPT.py — generates Selenium tests using GPT-4o with HTML + screenshots.
  - getGPTui.py — generates UI-specific test cases using GPT-4o.
  - getGPTuiHTML.py — same as above but without screenshots.
  - getGPTHTML.py — experimental script for HTML-only prompt generation.
  - openai_key.env — OpenAI key for accessing GPT-4o. **NOT PROVIDED IN REPO**

- **LLaMa/**

  - getLlamaBig.py, getLlamaBigStructure.py — LLaVA 79B: with and without screenshots.
  - getLlamaSmall.py, getLlamaSmallStructure.py — LLaVA 7B: with and without screenshots.
  - getSeleniumLLaMaProcNew.py — main script for launching LLaVA-based test generation (all configurations).
  - getSeleniumLLaMaProc.py — legacy version (not used).

- **PromptsGenLLaMa/**

  - prepLlamaPromts.py — transforms GPT prompts into LLaVA format (image-based).
  - prepLlamaPromtsHTML.py — same transformation for HTML-only prompts.

- **testExecution/**

  - runAllTests.py — main test runner. Executes all tests, counts steps, generates reports.
  - runTests.py, runTestsUI.py, runTestsHTML.py, runTestsUIHTML.py — older or mode-specific variants (mostly deprecated).
  - step_counter_patch.py — utility for comparing generated step count and actual execution results.

- **mutation/**

  - runTestsMut.py, runTestsMutOld.py — executes mutation testing, checks test resiliency.
  - collectSuccess.py — extracts successful tests only (used in mutation testing).

- **other/**
  - newRun.py — unclear functionality, under inspection.
  - stepCoverage.py — deprecated script for test step coverage (not used).

---

### 4.2 Output File Structure

#### Generated Tests

All test outputs are saved inside the following path:
code/Projects/<ProjectName>/GeneratedTests/tests/<Model>/<PromptType>/<PromptComplexity>/<Resolution>/<RunNumber>/
Examples: - With screenshots:
code/Projects/Cezerin/GeneratedTests/tests/gpt4o/zeroshot/simple/1024/2/
code/Projects/Cezerin/GeneratedTests/tests/llava7bllama3.1.8b/zeroshot/detailed/672/2/ - Without screenshots (HTML-only):
code/Projects/Cezerin/GeneratedTests/tests/gpt4oHTML/ui/medium/5/ - Feedback loop results:
code/Projects/Cezerin/GeneratedTests/tests/gpt4o/feedback/3/success/
code/Projects/Cezerin/GeneratedTests/tests/gpt4o/feedback/3/loops/

Naming logic includes:

- Model: gpt4o, gpt4oHTML, llava7bllama3.1.8b, etc.
- Prompt type: zeroshot, feedback, ui
- Prompt complexity: simple, medium, detailed
- Resolution: 672, 768, 1024 (if screenshots are used)
- Run number: 1, 2, 3, ...

#### Reports

Test execution and feedback loop reports are stored here:
code/Documantation/
