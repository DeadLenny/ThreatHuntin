# Readme

### Background

I'm currently interning as a Threat Hunter and during one of my recents hunts I noticed there wasn't an easy way to lookup a bulk of hashes.

This is important because most enterprise environments won't hash things in multiple forms of hashes because in bigger environments it becomes a lot more costly and resource intensive to do so.

Instead larger companies just hash files in either MD5, SHA1, or SHA256 . Our company just uses MD5.

Hashes aren't the holy grail of threat hunting , since they are at the bottom of the pyramid of pain, but they are still an easy way to check the environment for files that might be worth investigating.

The problem is that when you're looking at a piece of intel it usually has the hashes listed in SHA256, which isn't hard to lookup the MD5 hash in virustotal.

The problem becomes when you need to lookup 30+ hashes, then it becomes painful. So I decided to write a script that would use the virustotal api to lookup the hashes and write it out to a csv file.


### Important Notes
The program uses environment variables to store the api key. 

When importing the script to your ide, you're gonna have to create a .env file and create a VTI_API_KEY variable and store your Virustotal API Key in there.

___Note: This program will not run write if you don't have a VirusTotal API Key___ 

