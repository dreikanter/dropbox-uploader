# Dropbox Uploader

A simple script to backup files to Dropbox. Client installation not required.

## Setup

To use the script first you should register a new app at dropbox.com
[https://www.dropbox.com/developers/apps](developer area), get Dropbox API
key and secret values, and  acquire an access token using `gettoken.py` script:

    python getaccess.py <dropbox-api-key> <dropbox-api-secret>  <output-file-name>

This command will ask you to visit a confirmation URL, and create a file named
according to `<output-file-name>` argument with the following lines:

1. Dropbox API key
2. Dropbox API secret
3. Access token key
4. Access token secret

## Usage

    python dbup.py <dropbox-tokens-file> /directory/to/backup <output-file-name>

Where `<dropbox-tokens-file>` is a path to `dropbox.tokens` from the first part,
and the second argument is a path to the directory to zip and upload to Dropbox.

Dropbox API documentation example code was used gratefully.
