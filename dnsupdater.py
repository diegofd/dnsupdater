#!/usr/bin/env python3

import argparse
import boto3
import logging
import requests


logging.basicConfig(level=logging.ERROR)

def get_ip():
    r = requests.get('http://ifconfig.co/ip')
    if r.status_code == 200:
        return r.text.strip()
    else:
        return None

def update_dns(hosted_zone, name, ip):
    client = boto3.client('route53')

    response = client.change_resource_record_sets(
        HostedZoneId=hosted_zone,
        ChangeBatch={
            "Comment": "Automatic record update",
            "Changes": [{
                "Action": "UPSERT",
                "ResourceRecordSet": {
                    "Name": name,
                    "Type": "A",
                    "TTL": 300,
                    "ResourceRecords": [{
                        "Value": ip
                    }]
                }
            }]
        }
    )

    logging.debug(response)

def main():
    parser = argparse.ArgumentParser(
        description="DNSupdater: Update an AWS Hosted Zone with your current IP"
    )
    parser.add_argument("--hosted-zone-id", type=str, required=True, help="Hosted Zone ID")
    parser.add_argument("--name", type=str, required=True, help="Record name")
    args = parser.parse_args()

    ip = get_ip()
    if ip:
        update_dns(
            hosted_zone=args.hosted_zone_id,
            name=args.name,
            ip=ip
        )
        print(f"IP on {args.hosted_zone_id} for {args.name} updated to {ip}.")
    else:
        logging.error('IP cannot be retrieved.')

if __name__== "__main__":
  main()
