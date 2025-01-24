

# Aurora AI Agent ✨🤖

Welcome to **Aurora AI Agent**—an intelligent, interactive program powered by OpenAI API! This tool allows you to conveniently enter text, it will perofrm automated tasks, and run it locally on your system. Enjoy a straightforward GUI built using Tkinter, complete with formatting and color customization. 🌈
<p align="center">
  <img src="https://github.com/tomtyiu/aurora-ai-agent/blob/main/aurora-agent.JPG" height="300" alt="AgentGPT Logo"/>
</p>

---

## 📦 Features
1. **Interactive GUI:** Easily enter text or instructions into a scrolled text box.
2. **Automated Task:** Aurora AI Agent uses OpenAI’s powerful models(o1-mini) to perform automated tasks (recommended) or ollama local run model.  (Default llama 3.1)
3. **AI coding Agent** Aurora AI agent doesn't perform tasks, it also generate code and execute code for advance coding commands 
4. **Local Execution:** Generated Python code is saved to a `.py` file and run locally—no complex setup required.
5. **Customizable Appearance:** Change font family, size, text color, and background color to suit your preferences.
6. **File Management:** Quickly open and save files with built-in file dialogs.

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
Input: Go to Amazon and search for laptop
```bash
Open Edge browser
go to URL: http://amazon.com
In Search for, type: laptop
click on search
and keep browser open
```

Input: Write notes using notepad

```bash
Open  Notepad
Write to do list of groceries: bannanas, apples, eggs
```

Input: advance capability:
```bash
Open Edge browser
go to URL: https://html5-editor.net/ 

On left editor, copy and paste HTML to html5-editor
Hello world!

This is my first text. I need to see how it would look like when programmed with HTML.

Some parts should be red.

Some bold.

Some italic.

Some underlined.

Until my lesson is complete, and we shift to the other side.

edit the editor: 
Hello world! should have header 2 applied
The sentence below it should be a regular paragraph text.
The sentence mentioning red should be normal text and red
The sentence mentionnihg bold should be normal text bolded
Sentence mentioning italic should be italicized
The final sentence should be aligned to the right instead of the usual left

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
