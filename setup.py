import subprocess


def do_or_skip(prompt, *commands):
    answer = input(f"\033[34m::\033[0m {prompt} [Y/n]? ").strip().lower()
    if answer in ("", "y"):
        for command in commands:
            subprocess.run(command, shell=True)
    else:
        print("Ok, skipping...")


print("<|==============|          Applying config           |==============|>")
do_or_skip("Processing?", "cp -vri $(pwd)/.config ~/ ")
print("Config has been copied successfully")

print("<|==============| Packages that are included in HyDE |==============|>")
do_or_skip("Processing?", "yay -S eza", "yay -S fish", "yay -S starship")

print("<|==============|           Fixes for fish           |==============|>")
do_or_skip("Processing?", "yay -S noto-fonts-emoji")

print("<|==============|      Very important packages       |==============|>")
do_or_skip("Processing?", "yay -S helix", "yay -S htop")

print("<|==============|           Others packages          |==============|>")
do_or_skip(
    "Processing?",
    "yay -S telegram-desktop",
    "yay -S cava",
    "yay -S krita",
    "yay -S libreoffice",
    "yay -S steam",
    "yay -S obs-studio",
    "yay -S byedpi-bin",
)

print("<|==============|     Setup notepad environment      |==============|>")
do_or_skip(
    "Processing?",
    "cp -vr $(pwd)/Notepad ~/",
    "yay -S cron",
    "(crontab -l 2>/dev/null; echo '*/5 * * * * cd ~/Documents/Notepad",
    "./sync.sh') | crontab -",
)

print("<|==============|            That's all...           |==============|>")
