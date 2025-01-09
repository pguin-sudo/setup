import subprocess


def do_or_skip(prompt, command) -> bool:
    answer = input(f"\033[34m::\033[0m {prompt} [Y/n]? ").strip().lower()
    if answer in ("", "y"):
        return subprocess.run(command, shell=True).returncode == 1
    else:
        print("Ok, skipping...")
        return False


print("<|==============|          Applying config           |==============|>")
do_or_skip("Processing?", "cp -vri $(pwd)/.config ~/ ")
print("Config has been copied successfully")

print("<|==============| Packages that are included in HyDE |==============|>")
do_or_skip("Processing?", "yay -S eza fish starship")

print("<|==============|           Fixes for fish           |==============|>")
do_or_skip("Processing?", "yay -S noto-fonts-emoji")

print("<|==============|      Very important packages       |==============|>")
do_or_skip("Processing?", "yay -S helix htop")

print("<|==============|           Others packages          |==============|>")
do_or_skip(
    "Processing?",
    "yay -S telegram-desktop cava krita libreoffice steam obs-studio byedpi-bin",
)
