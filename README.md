## DNSupdater

Update an Amazon Route53 record with your current public IP address.

### How to run
```
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
./dnsupdater.py --hosted-zone-id HOSTED_ZONE_ID --name RECORD_NAME
```