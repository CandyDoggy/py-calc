"""
Calculator - Windowless Launcher
Runs without a console window on Windows.
"""
import os
import sys
import subprocess
import platform

def get_venv_python():
    """Get the path to the virtual environment's Python executable."""
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "venv", "Scripts", "pythonw.exe")

def main():
    """Main launcher logic."""
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    venv_python = get_venv_python()

    # If venv doesn't exist, create it and install deps
    if not os.path.exists(venv_python):
        python_exe = sys.executable
        subprocess.run(
            [python_exe, "-m", "venv", "venv"],
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        venv_python = get_venv_python()
        pip_exe = os.path.join(os.path.dirname(os.path.abspath(__file__)), "venv", "Scripts", "pip.exe")
        requirements = os.path.join(os.path.dirname(os.path.abspath(__file__)), "requirements.txt")
        subprocess.run(
            [pip_exe, "install", "-r", requirements],
            creationflags=subprocess.CREATE_NO_WINDOW
        )

    # Run calculator with pythonw (no console)
    main_py = os.path.join(os.path.dirname(os.path.abspath(__file__)), "main.py")
    subprocess.run([venv_python, main_py])

if __name__ == "__main__":
    main()
