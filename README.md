## DNSupdater

Update an Amazon Route53 record with your current public IP address.

### Credentials configuration

Easiest way is to install AWS CLI from [here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and then configure the credentials executing `aws configure` and provide access key and secret key for an IAM user with enough permissions to update the Route53 hosted zone. 

### How to run

```
$ pwd
/home/user 
$ git clone git@github.com:diegofd/dnsupdater.git
$ cd dnsupdater
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ ./dnsupdater.py --hosted-zone-id HOSTED_ZONE_ID --name RECORD_NAME
```

### How to schedule it with cron

Follow the steps above to install and configure a cron job to run every hour:
```
0 *     * * *   diego   cd /home/user/dnsupdater && .venv/bin/python3 dnsupdater.py --hosted-zone-id ZXXXXXXXXXXX --name sub.example.com
```
