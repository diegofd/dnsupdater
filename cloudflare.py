import logging

import CloudFlare


def update_dns(domain, name, ip):
    ip = '81.39.42.64'
    # Will use ~/.cloudflare/cloudflare.cfg
    # or env var CLOUDFLARE_API_TOKEN
    cf = CloudFlare.CloudFlare()

    try:
        response = cf.zones.get(params={'name': domain})
    except CloudFlare.CloudFlareAPIError as e:
        logging.error('/zones.get %s - %d %s' % (domain, e, e))
        return False
    except Exception as e:
        logging.error('/zones.get %s - %s' % (domain, e))
        return False

    if len(response) != 1:
        logging.error("Cloudflare returned wrong number of zones")
        return False
    
    zone_id = response[0]['id']

    # Find if the record already exists
    response = cf.zones.dns_records.get(zone_id)
    record = next((item for item in response if item["name"] == f"{name}.{domain}"), None)

    dns_record = {
        'name': name,
        'type':'A',
        'content': ip
    }

    if record:
        record_id = record['id']
        old_ip = record['content']
        logging.debug(f"Record already exist. Zone {zone_id}, record {record_id}, ip {old_ip}")
        if ip == old_ip:
            logging.info("IP didn't change. Not updating.")
        else:
            response = cf.zones.dns_records.put(zone_id, record_id, data=dns_record)
    else:
        response = cf.zones.dns_records.post(zone_id, data=dns_record)

    return True
