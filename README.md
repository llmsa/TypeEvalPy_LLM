<p align="center">
<img src="TypeEvalPy.jpg" width="75%" align="center">
<br>

<h3 align="center"> A Micro-benchmarking Framework for Python Type Inference Tools </h3>
</p>

## 📌 **Features**:


- 📜 Contains **154 code snippets** to test and benchmark.
- 🏷 Offers **845 type annotations** across a diverse set of Python functionalities.
- 📂 Organized into **18 distinct categories** targeting various Python features.
- 🚢 Seamlessly manages the execution of **containerized tools**.
- 🔄 Efficiently transforms inferred types into a **standardized format**.
- 📊 Automatically produces **meaningful metrics** for in-depth assessment and comparison.


## 🛠️ Supported Tools

| Supported :white_check_mark:                               | In-progress :wrench:                                                 | Planned :bulb:                             |
| -------------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------------------ |
| [HeaderGen](https://github.com/ashwinprasadme/headergen) | [Intellij PSI](https://plugins.jetbrains.com/docs/intellij/psi.html) |       |
| [Jedi](https://github.com/davidhalter/jedi)              | [Pyre](https://github.com/facebook/pyre-check)                       |       |
| [Pyright](https://github.com/microsoft/pyright)          | [PySonar2](https://github.com/yinwang0/pysonar2)                     |
| [HiTyper](https://github.com/JohnnyPeng18/HiTyper)       | [Pytype](https://github.com/google/pytype)                           |
| [Scalpel](https://github.com/SMAT-Lab/Scalpel/issues)    | [TypeT5](https://github.com/utopia-group/TypeT5)                     |
| [Type4Py](https://github.com/saltudelft/type4py)         |                                                                      |
| [GPT-4](https://openai.com/research/gpt-4) | | 
| [Ollama](https://ollama.ai) | |
---

## 🏆 TypeEvalPy Leaderboard

Below is a comparison showcasing exact matches across different tools, coupled with `top_n` predictions for ML-based tools.

| Rank | 🛠️ Tool | Top-n | Function Return Type | Function Parameter Type | Local Variable Type | Total |
|----|----|----|----|----|----|----|
| 1 | **[GPT-4](https://openai.com/research/gpt-4)** | 1 | 225 | 85 | 465 | 775 |
| 2 | **[Finetuned GPT3.5](https://platform.openai.com/docs/models/gpt-3-5)** | 1 | 209 | 85 | 436 | 730 |
| 3 | **[CodeLLaMA](https://huggingface.co/docs/transformers/main/model_doc/code_llama)** | 1 | 199 | 75 | 425 | 699 |
| 4 | **[HeaderGen](https://github.com/ashwinprasadme/headergen)** | 1 | 186 | 56 | 322 | 564 |
| 5 | **[Jedi](https://github.com/davidhalter/jedi)** | 1 | 122 | 0 | 293 | 415 |
| 6 | **[Pyright](https://github.com/microsoft/pyright)** | 1 | 100 | 8 | 297 | 405 |
| 7 | **[HiTyper](https://github.com/JohnnyPeng18/HiTyper)** | 1<br>3<br>5 | 163<br>173<br>175 | 27<br>37<br>37 | 179<br>225<br>229 | 369<br>435<br>441 |
| 8 | **[HiTyper (static)](https://github.com/JohnnyPeng18/HiTyper)** | 1 | 141 | 7 | 102 | 250 |
| 9 | **[Scalpel](https://github.com/SMAT-Lab/Scalpel/issues)** | 1 | 155 | 32 | 6 | 193 |
| 10 | **[Type4Py](https://github.com/saltudelft/type4py)** | 1<br>3<br>5 | 39<br>103<br>109 | 19<br>31<br>31 | 99<br>167<br>174 | 157<br>301<br>314 |

*<sub>(Auto-generated based on the the analysis run on 20-10-23 14:51)</sub>*

---
## :whale: Running with Docker

### 1️⃣ Clone the repo

```bash
git clone https://github.com/ashwinprasadme/TypeEvalPy.git
```

### 2️⃣ Build Docker image

```bash
docker build -t typeevalpy .
```

### 3️⃣ Run TypeEvalPy

🕒 Takes about 30mins on first run to build Docker containers.

📂 Results will be generated in the `results` folder within the root directory of the repository.
Each results folder will have a timestamp, allowing you to easily track and compare different runs.

```bash
docker run \
      -v /var/run/docker.sock:/var/run/docker.sock \
      -v ./results:/app/results \
      typeevalpy
```

🔧 **Optionally**, run analysis on specific tools:

```bash
docker run \
      -v /var/run/docker.sock:/var/run/docker.sock \
      -v ./results:/app/results \
      typeevalpy --runners headergen scalpel
```

🛠️ Available options: `headergen`, `pyright`, `scalpel`, `jedi`, `hityper`, `type4py`, `hityperdl`

---

<details>
  <summary><b>Running From Source...</b></summary>

   ## 1. 📥 Installation

   1. **Clone the repo**

      ```bash
      git clone https://github.com/ashwinprasadme/TypeEvalPy.git
      ```


   2. **Install Dependencies and Set Up Virtual Environment**

      Run the following commands to set up your virtual environment and activate the virtual environment.

      ```bash
      python3 -m venv .env
      ```

      ```bash
      source .env/bin/activate
      ```

      ```bash
      pip install -r requirements.txt
      ```

   ---

   ## 2. 🚀 Usage: Running the Analysis

   1. **Navigate to the `src` Directory**

      ```bash
      cd src
      ```

   2. **Execute the Analyzer**

      Run the following command to start the benchmarking process on all tools:

      ```bash
      python main_runner.py
      ```

      or

      Run analysis on specific tools

      ```
      python main_runner.py --runners headergen scalpel
      ```

</details>


---

### 🤝 Contributing

Thank you for your interest in contributing! To add support for a new tool, please utilize the Docker templates provided in our repository. After implementing and testing your tool, please submit a pull request (PR) with a descriptive message. Our maintainers will review your submission, and merge them.

---

### ⭐️ Show Your Support

Give a ⭐️ if this project helped you!
