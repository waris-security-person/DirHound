DirHound  simple directory/endpoint checker

A tiny Python tool that checks which paths from a wordlist exist on a given domain by making HTTP GET requests.

Important: Use this tool only for authorized testing on systems you own or have explicit permission to test. The author is not responsible for misuse.

Features
- Appends entries from a newline-separated wordlist to a base domain.
- Makes HTTP GET requests using the requests library.
- Prints URLs that return HTTP 200 OK.

Requirements
- Python 3.7+
- requests library

Install dependency:
python3 -m pip install requests

Usage
1. Save the script as dirscan.py.
2. Prepare a wordlist file (one path per line). Example wordlist.txt:

admin
login
dashboard
robots.txt
images/

3. Run the script:
python3 dirscan.py

The script will prompt for:
- Enter domain name: e.g. http://example.com/ or https://example.com/
- Enter wordlist name: path to the wordlist file, e.g. wordlist.txt

Output example:
http://example.com/admin
http://example.com/login

Behavior details
- The script concatenates the provided domain string with each wordlist line (stripping the trailing newline).
- It prints any URL that returns an HTTP 200 response.
- No retries, timeouts, or concurrency are used in the base script—requests may block if the server is slow.

Security & Legal
- Do not scan systems without explicit permission. Unauthorized scanning can be illegal and may be considered hostile activity.
- Respect rate limits and the target’s terms of service.
- Consider checking robots.txt and contacting the owner before performing broad scans.

Recommended improvements (optional)
- Command-line arguments via argparse (non-interactive usage).
- Input validation and domain normalization (ensure http:// or https://, normalize trailing slashes).
- Timeouts and error handling (requests.get(..., timeout=5) plus try/except).
- Concurrency (e.g., concurrent.futures.ThreadPoolExecutor) with configurable rate limits.
- Logging / output to CSV or JSON.
- Show and store non-200 status codes and response sizes.
- Optional SSL verification toggle for testing local servers.
- Progress indicator and configurable user-agent header.

License
MIT License. Use and modify freely, with the understanding that you are responsible for legal and ethical use.
