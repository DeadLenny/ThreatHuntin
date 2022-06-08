# Readme

### Update
- I recently got feedback on this code and was made aware that I should be using json parsing instead of regex.

- VTHashLookup is the file with the json parsing and the file I will be making updates to, but I left the original one up because it shows that regex can be used even though it is not ideal.

- I also implemented the Malware Bazaar api for hashlookups as well. If this script goes through multiple reputable hashlookup sources then it give a more holistic over view in the output.

- I'm still looking for more tools to use for IOC Hashlookup, some I am looking into right now are Anomali Threatstream and ThreatMiner.

- No idea when I will have any of this implemented by

### Background

I'm currently interning as a Threat Hunter and during one of my recents hunts I noticed there wasn't an easy way to lookup a bulk of hashes.

This is important because most enterprise environments won't hash things in multiple forms of hashes because in bigger environments it becomes a lot more costly and resource intensive to do so.

Instead larger companies just hash files in either MD5, SHA1, or SHA256 . Our company just uses MD5.

Hashes aren't the holy grail of threat hunting , since they are at the bottom of the pyramid of pain, but they are still an easy way to check the environment for files that might be worth investigating.

The problem is that when you're looking at a piece of intel it usually has the hashes listed in SHA256, which isn't hard to lookup the MD5 hash in VirusTotal.

It just becomes tedious when you need to lookup 30+ hashes. So I decided to write a script that would use the virustotal api, and maybe other api's in the future, to lookup the MD5/SHA1/SHA256 hashes and write it out to a csv file. The script takes in either MD5, SHA1 or SHA256 and outputs the other two automatically.

This would very convenient for anyone conducting an intel based Threat Hunt


### Important Notes
The program uses environment variables to store the api key. 

When importing the script to your ide, you're gonna have to create a .env file and create a 'api_key_vti' variable and store your Virustotal API Key in there.

___Note: This program will not run write if you don't have a VirusTotal API Key___ 

