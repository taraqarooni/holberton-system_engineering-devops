# 0x19. Postmortem

## Issue Summary :
From May 19 12:30 p.m to May 21 9:30 p.m Requests to the website responded with an ERROR 500, this affected 35% of users since the requests corresponded to a query module. The suspension was due to an incorrect file name in the last update.

## Timeline (Eastern Standard Time)
May 19
* 12:30 p.m : Code push to server
* 1:30 p.m : Deploy code 
* 1:45 p.m : Outage begins

From 1:50 p.m to May 21 9:30 am check and validate every process associated to apache with strace

* May 21 9:00 am: Found error on deploy
* May 21 9:25 am: Run script to fix it
* May 21 9:30 am: Error fixed and requests responded 200

### Root Cause and Resolution 
The root of the problem was due to an incorrect file name in the last update of the site, specifically in the extension of the updated php module
Initially it was verified that the files were in the appropriate apache path “sites / available”, with the `ps aux` command the processes associated with apache were verified, then with the `strace` command the returns were checked the file was identified, a script was generated to correct the problem, it was validated with the `curl` command and access from the browser.

### Corrective and Preventative Measures
In light of the incident in the last two days, an evaluation and review of the update process carried out was made, it was determined that stages were omitted for the release of this module to production, to prevent future incidents, the following improvements were implemented:

* A QA team was formed that will be in charge of validating and testing changes and updates
* A QA environment was created where pre-production integration tests are carried out
* Github CI/CD services were integrated to deployment updates and code revisions
