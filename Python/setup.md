# Python Setup Guide (Windows & Mac)

## 1. Install Python

### Windows
1. Download the installer from https://www.python.org/downloads/windows/
2. Run the installer. **Check "Add python.exe to PATH"** before clicking Install.
3. Verify the install:
   ```
   python --version
   ```

### Mac
Use [Homebrew](https://brew.sh):
```bash
brew install python
```
Verify the install:
```bash
python3 --version
```

> Alternative (recommended if you need multiple Python versions): use [pyenv](https://github.com/pyenv/pyenv) (Mac) or [pyenv-win](https://github.com/pyenv-win/pyenv-win) (Windows) to install and switch between specific versions, e.g. `pyenv install 3.11.9`.

## 2. Create a Virtual Environment (venv)

A virtual environment keeps a project's dependencies isolated from your system Python.

### Windows
```powershell
python -m venv venv
venv\Scripts\activate
```

### Mac
```bash
python3 -m venv venv
source venv/bin/activate
```

Once activated, your terminal prompt will be prefixed with `(venv)`.

## 3. Install Dependencies

With the venv activated:
```bash
pip install -r requirements.txt
```

Or install packages individually:
```bash
pip install <package-name>
```

To save installed packages to a requirements file:
```bash
pip freeze > requirements.txt
```

## 4. Deactivate the Virtual Environment

When you're done working:
```bash
deactivate
```

## Notes
- Always activate the venv before running scripts or installing packages for this project.
- Add `venv/` to your `.gitignore` so the environment itself isn't committed.
