import subprocess
import requests


# FUNCTIONS


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class formatting:
    HEADER = "<|==============|"
    HEADER_END = "|==============|>"
    WARNING = "[WARNING] "


def ask(prompt):
    """Ask user for a yes/no input and return True for 'yes' and False for 'no'."""
    answer = input(f"{bcolors.OKBLUE}::{bcolors.ENDC} {prompt} [Y/n]? ").strip().lower()
    return answer in ("", "y")


def execute_commands(*commands):
    """Execute a list of commands."""
    for command in commands:
        subprocess.run(command, shell=True)


# BLOCKS


def process_config():
    """Process the configuration setup."""
    print(
        f"{bcolors.HEADER}{formatting.HEADER}          Applying config           {formatting.HEADER_END}{bcolors.ENDC}"
    )
    if ask("Processing?"):
        execute_commands("cp -vri $(pwd)/config/* ~/.config/ ")
        print("Config has been copied successfully")


def install_hyde_packages():
    """Install HyDE related packages."""
    print(
        f"{bcolors.HEADER}{formatting.HEADER} Packages that are included in HyDE {formatting.HEADER_END}{bcolors.ENDC}"
    )
    if ask("Processing?"):
        execute_commands("yay -S eza", "yay -S fish", "yay -S starship")


def install_fish_fixes():
    """Install fixes for fish."""
    print(
        f"{bcolors.HEADER}{formatting.HEADER}           Fixes for fish           {formatting.HEADER_END}{bcolors.ENDC}"
    )
    if ask("Processing?"):
        execute_commands("yay -S noto-fonts-emoji")


def install_important_packages():
    """Install important packages."""
    print(
        f"{bcolors.HEADER}{formatting.HEADER}      Very important packages       {formatting.HEADER_END}{bcolors.ENDC}"
    )
    if ask("Processing?"):
        execute_commands("yay -S helix", "yay -S htop")


def install_other_packages():
    """Install other packages."""
    print(
        f"{bcolors.HEADER}{formatting.HEADER}           Others packages          {formatting.HEADER_END}{bcolors.ENDC}"
    )
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


def setup_zapret_and_dns_proxy():
    """Setup zapret and DNS proxy."""
    print(
        f"{bcolors.HEADER}{formatting.HEADER}     Setup zapret and dns proxy     {formatting.HEADER_END}{bcolors.ENDC}"
    )
    if ask("Processing?"):
        url = "https://api.github.com/repos/bol-van/zapret/releases/latest"
        response = requests.get(url)
        if response.status_code == 200:
            release_data = response.json()
            download_url = next(
                (
                    asset["browser_download_url"]
                    for asset in release_data["assets"]
                    if ".tar.gz" in asset["name"] and "openwrt" not in asset["name"]
                ),
                None,
            )
            if download_url:
                print(f"Downloading from {download_url}")
                tar_file = download_url.split("/")[-1]

                execute_commands(f"sudo rm -f ./{tar_file}")

                execute_commands(f"sudo wget {download_url}")

                print(f"Extracting {tar_file} ({tar_file[:-7]})")
                execute_commands(
                    "sudo mkdir /opt/zapret",
                    f"sudo tar -xzvf ./{tar_file}",
                    f"sudo cp -r $(pwd)/{tar_file[:-7]}/* /opt/zapret",
                    f"sudo rm -rf $(pwd)/{tar_file[:-7]}",
                    f"sudo rm $(pwd)/{tar_file}",
                )
            else:
                print("No suitable tar.gz file found in the release assets.")
        else:
            print(f"Failed to fetch release info: {response.status_code}")

        execute_commands(
            "sudo /opt/zapret/install_bin.sh",
            "sudo /opt/zapret/install_prereq.sh",
            "yay -S dnscrypt-proxy",
            "sudo cp $(pwd)/etc/dnscrypt-proxy/dnscrypt-proxy.toml /etc/dnscrypt-proxy/dnscrypt-proxy.toml",
            "sudo chattr -i /etc/resolv.conf",
            "sudo cp $(pwd)/etc/resolv.conf /etc/resolv.conf",
            "sudo chattr +i /etc/resolv.conf",
            "sudo systemctl enable dnscrypt-proxy.service",
            "sudo systemctl start dnscrypt-proxy.service",
            "sudo systemctl enable systemd-resolved.service",
            "sudo systemctl start systemd-resolved.service",
        )
        print(
            f"{bcolors.WARNING}{formatting.WARNING}IF YOU DO NOT HAVE WORKING STRATEGY YOU WILL NOT ABLE TO SETUP CONFIG IN ZAPRET{bcolors.ENDC}"
        )
        if ask("Run blockcheck.sh for searching strategy?"):
            execute_commands(
                "sudo /opt/zapret/blockcheck.sh",
            )
        if ask("Run discord fix?"):
            execute_commands(
                "sudo cp /opt/zapret/init.d/custom.d.examples.linux/50-discord /opt/zapret/init.d/sysv/custom.d/50-discord",
            )
        print(
            f"{bcolors.WARNING}{formatting.WARNING}DO NOT JUST PRESS ENTER WHILE SETUP ZAPERT{bcolors.ENDC}"
        )
        if ask("Copy autors' zapret config?"):
            execute_commands("sudo cp $(pwd)/opt/zapret/config /opt/zapret/config")
        execute_commands("sudo /opt/zapret/install_easy.sh")


def setup_notepad_environment():
    """Setup the notepad environment."""
    print(
        f"{bcolors.HEADER}{formatting.HEADER}     Setup notepad environment      {formatting.HEADER_END}{bcolors.ENDC}"
    )
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
    setup_zapret_and_dns_proxy()
    setup_notepad_environment()
    print(
        f"{bcolors.HEADER}{formatting.HEADER}            That's all...           {formatting.HEADER_END}{bcolors.ENDC}"
    )


if __name__ == "__main__":
    main()
