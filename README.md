## FeLine (Command line client for LLM)

### Install
- Clone the repository `git git@github.com:gonzaloaxx/FeLine.git`
- Get your API key on the Google Studio platform [aistudio](https://aistudio.google.com/app/apikey)

- Make your virtual enviroment with python on FeLine folder
`python3 -m pip install virtualenv && python3 -m virtualenv .venv`
- Activate `source .venv/bin/activate`
- Install dependences `python -m pip install -r requirements.txt`
- Now deactivate `deactivate`
- Edit the .bashrc file with the environment variables. For example:
```
export GEMINI_API_KEY="SerialStringHere"
export FELINE_ENV="$HOME/FeLine/.venv/bin"
export FELINE_PY="$HOME/FeLine/feline.py"

alias feline="$HOME/FeLine/wrapper.sh"
```
- Refresh file `source ~/.bashrc`
- Run feline app like: `feline -m "Hello! This is a feline test."`

