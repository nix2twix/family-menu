import subprocess

def main():
    subprocess.run(["streamlit", "run", "family_menu.py", "--server.address=0.0.0.0", "--server.port=8501"])

if __name__ == "__main__":
    main()
