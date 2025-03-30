#!/usr/bin/env python3
import subprocess

def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print("Error:", result.stderr)
    else:
        print(result.stdout)
        print(command)

def main():
    commit_message = input("Enter commit message: ")
    
    # Add all changes
    run_command(["git", "add", "."])
    
    # Commit with the provided message
    run_command(["git", "commit", "-m", commit_message])
    
    # Push changes
    run_command(["git", "push"])

if __name__ == "__main__":
    main()
