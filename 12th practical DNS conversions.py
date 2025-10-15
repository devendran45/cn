import socket

def iptourl(ip_address):
    """Converts an IP address to a URL (hostname)."""
    try:
        url = socket.gethostbyaddr(ip_address)
        return url[0]
    except socket.herror as e:
        return f"Error: Could not find a host for IP address {ip_address}. ({e})"
    except socket.gaierror as e:
        return f"Error: Address-related error for IP {ip_address}. ({e})"

def urltoip(url):
    """Converts a URL (hostname) to an IP address."""
    try:
        ip_address = socket.gethostbyname(url)
        return ip_address
    except socket.gaierror as e:
        return f"Error: Could not resolve hostname {url}. ({e})"

def main():
    """Main function to run the DNS lookup program."""
    while True:
        print("\nDNS Lookup Program:")
        print("1. IP to URL.")
        print("2. URL to IP.")
        print("3. Exit.")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            ip_address = input("Enter IP address: ")
            result = iptourl(ip_address)
            print(f"URL: {result}")
        elif choice == "2":
            url = input("Enter the URL: ")
            result = urltoip(url)
            print(f"IP address: {result}")
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
