# Tetration annotation update
Download inventory through Tetration API and then upload host-application mapping using custom annotations.

Dependencies - 
tetpyclient 
json

Credentials -
Create API key from Tetration system and save api_credentials.json to your base directory.

CSV Files -
Create download.csv and upload.csv files in your base directory.

Python Scripts -
Edit scripts with your system information:
  - API_Endpoint - the base URL of your Tetration system
  - File_path - path to your base directory where scripts run + the file name
  - root_app_scope_name - the Scope from Tetration that you want to download/upload annotations
  
 Tet_INV_Download.py - will download the inventory w/ annotations from your base scope.
 
  Tet_INV_Upload.py - will upload the inventory w/ annotations to your base scope.  Can add new annotations, update inventory, or add new hosts.
