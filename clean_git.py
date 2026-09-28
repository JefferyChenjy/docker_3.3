import os
import subprocess
import sys

def run_cmd(cmd):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(f"Success: {result.stdout}")
    return result

def purge_large_files():
    # 1. Force remove the large terraform directory from all historical commits
    print("--- Removing large terraform files from Git history ---")
    filter_cmd = (
        'git filter-branch --force --index-filter '
        '"git rm -r --cached --ignore-unmatch github-oidc-bootstrap/.terraform .terraform"'
        ' --prune-empty --tag-name-filter cat -- --all'
    )
    run_cmd(filter_cmd)

    # 2. Clean up reflogs and force garbage collection to shrink .git folder
    print("--- Cleaning up Git references and running Garbage Collection ---")
    run_cmd("rm -rf .git/refs/original/")
    run_cmd("git reflog expire --expire=now --all")
    run_cmd("git gc --prune=now --aggressive")

    print("\nCleanup complete! Check your file size now.")

if __name__ == "__main__":
    purge_large_files()