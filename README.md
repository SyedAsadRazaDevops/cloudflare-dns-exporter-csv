# Cloudflare DNS Exporter

This Python script fetches DNS records from Cloudflare for a specified zone and exports them into a CSV file.

## Prerequisites

- Python 3 installed
- `requests` library installed (`pip install requests`)

## Usage

1. **Clone Repository:**
   ```
   git clone https://github.com/SyedAsadRazaDevops/cloudflare-dns-exporter-csv.git
   cd cloudflare-dns-exporter-csv
   ```

2. **Update Script:**
   - Open `cloudflare_dns_export.py`.
   - Replace `'YOUR_ZONE_ID'` with your Cloudflare zone ID.
   - Replace `'YOUR_API_KEY'` with your Cloudflare API key.

Certainly! Here's how you can obtain your Cloudflare Zone ID and API key:
### Cloudflare Zone ID:

1. **Log in to Cloudflare:** Go to [Cloudflare](https://www.cloudflare.com/) and log in to your account.
2. **Select Domain:** Choose the domain for which you want to fetch DNS records.
3. **Get Zone ID:**
   - Once logged in and viewing the desired domain, go to the dashboard or overview section.
   - Scroll down to the bottom right. Under the "API" section, you'll find the Zone ID. It's a string of characters (alphanumeric) unique to your domain.

### Cloudflare API Key:

1. **Access API Tokens:** In Cloudflare, navigate to the "My Profile" or "Profile" section.
2. **Create API Token:**
   - Look for the "API Tokens" or "API Keys" section.
   - Click on "Create Token" or a similar option to generate a new API token.
3. **Token Permissions:**
   - Choose the appropriate permissions needed for the token. For DNS record access, select permissions related to "Zone: Read."
4. **Generate Token:**
   - After selecting permissions, generate the token. You'll receive an API token, which acts as your API key.
5. **Note the API Key:**
   - Copy the generated API key/token and securely store it.

### Using the Obtained Information:

- Replace `'YOUR_ZONE_ID'` in the Python script with the Zone ID you retrieved from Cloudflare.
- Replace `'YOUR_API_KEY'` in the Python script with the API key/token you generated.
  
By replacing these placeholders in the script with your actual Zone ID and API key, the script will authenticate and fetch DNS records for the specified domain via the Cloudflare API.

3. **Run Script:**
   ```
   python3 cloudflare_dns_export.py
   ```
4. **Output:**
   - The script will generate a file named `cloudflare_dns_records.csv` containing all DNS records fetched from Cloudflare.

## Notes

- This script utilizes Cloudflare's API to fetch DNS records. Ensure you have the necessary permissions and correct API credentials.
- Adjust pagination settings (`per_page`) in the script based on the number of DNS records in your Cloudflare zone.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

