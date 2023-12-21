import requests
import csv

# Cloudflare API endpoint for DNS records
url = "https://api.cloudflare.com/client/v4/zones/YOUR_ZONE_ID/dns_records"

# Replace 'YOUR_ZONE_ID' with your actual Cloudflare zone ID
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}

dns_records = []

# Make requests to fetch all DNS records (handle pagination)
page = 1
while True:
    params = {'page': page, 'per_page': 50}  # Adjust per_page as needed
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        page_records = response.json()["result"]
        if len(page_records) == 0:
            break  # No more records, end loop
        dns_records.extend(page_records)
        page += 1
    else:
        print("Failed to fetch DNS records. Status code:", response.status_code)
        break

# Write DNS records to CSV file
if dns_records:
    csv_file = "cloudflare_dns_records.csv"

    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Type", "Content", "TTL"])
        for record in dns_records:
            writer.writerow([record["name"], record["type"], record["content"], record["ttl"]])
    print(f"Total {len(dns_records)} DNS records exported to {csv_file} successfully!")
else:
    print("No DNS records found.")
