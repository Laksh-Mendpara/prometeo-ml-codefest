# ML Codefest

Welcome to the **ML Codefest** repository! Follow the steps below to get started with the project.

---

## Getting Started

### 1. Clone and Enter the Repository
```bash
git clone https://github.com/Aradhya2708/ml-codefest.git
cd ml-codefest
```

### 2. Install Dependencies
Navigate to the `server` directory and install the required dependencies:
```bash
pip install -r ./server/requirements.txt
```

---

## Environment Setup

### 3. Create a `.env` File
In the main directory (`ml-codefest`), create a file named `.env` with the following content:
```
OPENAI_API_KEY=your_openai_api_key_here
COMPOSIO_API_KEY=your_composio_api_key_here
```
> **Note:** Replace `your_openai_api_key_here` and `your_composio_api_key_here` with your actual API keys.

---

## Run the Application

### 4. Start the Main Script
Run the main Python script:
```bash
python server/src/agents/main.py
```

### 5. Enter Your Task
Follow the instructions in the script to input and execute your task.

---

## Troubleshooting
- Ensure you have Python 3.8 or higher installed.
- Verify that all dependencies are installed using the `requirements.txt` file.
- Double-check your `.env` file for proper key-value formatting.

---

Happy Coding! 🚀
