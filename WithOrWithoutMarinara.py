#BetaTestDev

#Welcome Branch

#Libraries Imported Here
import sys          # Allows us to write to the terminal without a newline
import time         # Allows us to add delays (sleep)

# ANSI color codes for terminal text
RESET = "\033[0m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
BOLD = "\033[1m"

# Display welcome messages
print(f"\n{CYAN}{BOLD}Welcome Branch - Developer: Cohen Smith{RESET}")
print(f"\n{CYAN}Welcome to InfoTechCenter V.1.0{RESET}")

# Initialize counters
x = 0               # Controls how long the boot sequence runs
ellipsis = 0        # Controls how many dots appear in the animation

# Boot animation loop
while x != 20:
    x += 1          # Increase loop counter

    # Create the boot message with animated dots
    ellipsisMessage = f"{YELLOW}InfoTechCenter OS Booting{'.' * ellipsis}{RESET}"
    ellipsis += 1

    # Rewrite the same terminal line instead of printing a new one
    sys.stdout.write("\r\033[K" + ellipsisMessage)
    sys.stdout.flush()

    # Pause to control animation speed
    time.sleep(0.5)

    # Reset dots after three dots
    if ellipsis == 4:
        ellipsis = 0

    # Final message after boot completes
    if x == 20:
        print(f"\n{GREEN}{BOLD}Operating System Booted Up - Retina Scanned - Access Granted{RESET}")