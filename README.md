# Aurora AI Agent ✨🤖

Welcome to **Aurora AI Agent**—an intelligent, interactive program powered by OpenAI! This tool allows you to conveniently enter text, generate Python code based on your input, and run it locally on your system. Enjoy a straightforward GUI built using Tkinter, complete with formatting and color customization. 🌈

---

## 📦 Features
1. **Interactive GUI:** Easily enter text or instructions into a scrolled text box.
2. **Automated Task:** Aurora AI Agent uses OpenAI’s powerful models(o1-mini) to perform automated tasks or ollama local run model.  (Default llama 3.1)
3. **Local Execution:** Generated Python code is saved to a `.py` file and run locally—no complex setup required.
4. **Customizable Appearance:** Change font family, size, text color, and background color to suit your preferences.
5. **File Management:** Quickly open and save files with built-in file dialogs.

---

## 🚀 Getting Started

1. **Clone or Download** this repository to your local machine.
2. **Install Python 3.7+** (if not already installed).  For local model: Install Ollama, **Ollama download** [link](https://ollama.com/download/windows)
3. For Ollama, for quick start host model type:
```bash
 ollama run llama3.1
```
5. **OpenAI model:** Make sure you have the **OpenAI ,Selenium Python library** installed:

```bash
   pip install openai selenium tkinter 
```

Set Your OpenAI API Key as an environment variable:
```bash
Windows: set OPENAI_API_KEY=your_api_key or ollama do not require key
macOS/Linux: export OPENAI_API_KEY=your_api_key
```

## How to install
### Create a virtual environment
```bash
python -m venv venv
```

### Activate the virtual environment
```bash
source venv/bin/activate
```

### run the program
```bash
python aiagentv1.py

#or for ollama

python aiagentv1-ollama.py

```

### Examples
Input:
```bash
Open Edge browser
go to URL: http://amazon.com
In Search for, type: laptop
click on search
and keep browser open
```

##  🔒 Security & Privacy

This application uses your OpenAI API key. Keep it private and secure.

Local Execution: The code runs on your local system, ensuring data remains under your control.

##  🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request to help us improve this AI Agent.

##  📄 License

This project is licensed under the MIT License. See LICENSE file for details

Stay curious, code on, and have a great time exploring Aurora AI Agent! 🎉
