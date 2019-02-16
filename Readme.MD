# Fill replicon timesheets

## Why ?
I know you're busy or might be out of office. But it is important to fill the replicon time sheets for the sake of program managers. So, this program will help you to automatically submit the replicon for you.

## Setup

### Clone the repo

    cd ~/
    git clone git@github.com:parthakonda/fill_timesheets.git

### Install virtualenv and requirements

    cd ~/
    virtualenv -p python3 venv
    source ~/venv/bin/activate
    cd fill_timesheets/
    pip3 install -r requirements.txt

## Have chromedrive in your PATH

## Export credentials
    
    export REPLICON_COMPANY=<company_name>
    export REPLICON_USERNAME=<username>
    export REPLICON_PASSWORD=<password>

## Run

    cd ~/fill_timesheets
    behave features

## Setup a cronjob

    crontab fill_timesheets_cron.txt



