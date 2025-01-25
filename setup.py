import subprocess


# FUNCTIONS


def ask(prompt):
    """Ask user for a yes/no input and return True for 'yes' and False for 'no'."""
    answer = input(f"\033[34m::\033[0m {prompt} [Y/n]? ").strip().lower()
    return answer in ("", "y")


def execute_commands(*commands):
    """Execute a list of commands."""
    for command in commands:
        subprocess.run(command, shell=True)


# BLOCKS


def process_config():
    """Process the configuration setup."""
    print("<|==============|          Applying config           |==============|>")
    if ask("Processing?"):
        execute_commands("cp -vri $(pwd)/config/* ~/.config/ ")
        print("Config has been copied successfully")


def install_hyde_packages():
    """Install HyDE related packages."""
    print("<|==============| Packages that are included in HyDE |==============|>")
    if ask("Processing?"):
        execute_commands("yay -S eza", "yay -S fish", "yay -S starship")


def install_fish_fixes():
    """Install fixes for fish."""
    print("<|==============|           Fixes for fish           |==============|>")
    if ask("Processing?"):
        execute_commands("yay -S noto-fonts-emoji")


def install_important_packages():
    """Install important packages."""
    print("<|==============|      Very important packages       |==============|>")
    if ask("Processing?"):
        execute_commands("yay -S helix", "yay -S htop")


def install_other_packages():
    """Install other packages."""
    print("<|==============|           Others packages          |==============|>")
    if ask("Processing?"):
        execute_commands(
            "yay -S telegram-desktop",
            "yay -S cava",
            "yay -S krita",
            "yay -S libreoffice",
            "yay -S steam",
            "yay -S obs-studio",
            "yay -S byedpi-bin",
        )


def setup_notepad_environment():
    """Setup the notepad environment."""
    print("<|==============|     Setup notepad environment      |==============|>")
    if ask("Processing?"):
        execute_commands(
            "cp -vr $(pwd)/Notepad ~/",
            "yay -S cron",
            "(crontab -l 2>/dev/null; echo '*/5 * * * * cd ~/Documents/Notepad ./sync.sh') | crontab -",
        )


def main():
    """Main function to execute all setup steps."""
    process_config()
    install_hyde_packages()
    install_fish_fixes()
    install_important_packages()
    install_other_packages()
    setup_notepad_environment()
    print("<|==============|            That's all...           |==============|>")


if __name__ == "__main__":
    main()
