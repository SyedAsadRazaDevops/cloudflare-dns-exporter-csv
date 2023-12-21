# Cloudflare DNS Exporter

This Python script fetches DNS records from Cloudflare for a specified zone and exports them into a CSV file.

## Prerequisites

- Python 3 installed
- `requests` library installed (`pip install requests`)

## Usage

1. **Clone Repository:**
   ```
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. **Update Script:**
   - Open `cloudflare_dns_export.py`.
   - Replace `'YOUR_ZONE_ID'` with your Cloudflare zone ID.
   - Replace `'YOUR_API_KEY'` with your Cloudflare API key.

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

