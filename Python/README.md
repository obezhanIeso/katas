# Python Katas

This assumes you already have a version of Python installed on your machine. Then:

1. Create a virtual environment for this project. This ensures that dependencies remain
   isolated from the rest of your machine.

   ```bash
   # Bash, Zsh, etc.
   python -m venv venv
   source venv/bin/activate
   ```

   ```pwsh
   # PowerShell
   python -m venv venv
   . ./venv/Scripts/Activate.ps1
   ```

2. Install dependencies. This will automatically target the venv you created, if you did.

   ```bash
   pip install -r requirements.txt
   ```

   On some systems you may need to invoke pip as a Python module, like `python -m pip ...`

3. In all cases and shells, when you've finished the kata, run `deactivate` to deactivate the
   virtual environment.