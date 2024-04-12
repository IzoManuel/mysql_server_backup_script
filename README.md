# Database Backup Script

This script is designed to automatically backup a MySQL database daily at 2 AM using a cron job. It utilizes Python and the `mysqldump` utility to create backups.

## Usage

1. Clone or download the repository to your EC2 instance.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Copy the `.env.example` file and rename it to `.env`. Update the variables with your SMTP server settings and email addresses.
4. Configure the cron job.

