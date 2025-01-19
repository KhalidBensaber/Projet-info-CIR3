import subprocess
import sys

def start_server():
    try:
        print("Starting the server...")
        subprocess.check_call([sys.executable, "manage.py", "runserver", "0.0.0.0:8000"])
    except KeyboardInterrupt:
        print("\nServer stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # 1. Installer les dépendances
    from install_dependencies import install_requirements
    install_requirements()

    # 2. Lancer le serveur Django
    start_server()
