# Python Programming Agent

## Description
This project is based off a course given by Boot.dev. This project created an AI agent that is able to identify bugs in a python project, i.e. Calculator, and fix said bugs. The agent has 4 tools that it can use to complete it's tasks.
    - get\_files\_info: List a directory, its subdirectories and their files to see what is in the project.
    - get\_file\_content: Reads the content of the file for later use of the agent.
    - run\_python\_file: Executes a python script.
    - write\_file: Writes content to a specified file.

The base of this AI agent is Google's Gemini models and api. Specfically, this project uses Gemini Flash 2.5 model for the agent. The following set-up guidelines is based on a Ubuntu-based system.

## Environment Set-up

1. Install uv
This is a kick-ass Python project and package manager. To install:

```
    curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Clone the repo

```
# HTTPS
git clone https://github.com/jhopkins2/agent.git
```
or

```
# SSH
git@github.com:jhopkins2/agent.git
```

For SSH you will need to create an SSH key for Github. The documentation can be found here: [Create SSH Key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

3. Required Packages
These packages will be installed when you initialize the project using uv with the pyproject.toml file. 

google-genai>=1.56.0
python-dotenv==1.1.0

4. Initializing the project
Navigate to the project's directory in a terminal and execute the following command:

```
uv init .
```

This will use the preexisting toml file to initialize the project.

Make sure that a virtual environment has been created for the project. If it has not, run this command:

```
uv venv
```

This will create a .venv directory and then you can activate the virtual environment with:

```
source .venv/bin/activate
```

Make sure that the packages have been installed in the venv using

```
uv pip list
```

5. Create you Gemini API key
Go to [Google AI studio](https://aistudio.google.com) to create an API key that your project can use. Once you have created that key, make an ".env" file. 

In that file write "GEMINI\_API\_KEY='your api key'". Make sure you do not share or upload your API key with anyone else. Make sure you have a ".gitignore" file in the root of the project that contains your ".env" file. 
