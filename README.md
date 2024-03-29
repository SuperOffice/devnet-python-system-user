# devnet-python-system-user

Demonstrates how to obtain a system user ticket from a system user token.

## Try It Out

Update the following files:

1. private key file: private.xml or private.pem
2. main.py: change the following five settings:

```python
from SystemUserToken import SystemUserToken

# create instance of SystemUserToken
#   application_token: application secret
#   private_key_file:  file with .xml (RSAXML) or .pem file extension
#   environment:       'sod' | 'stage' | 'online'

systemuser = SystemUserToken(
    'application_token', 'private_key_file', 'environment')

# get the system user ticket
#   system_user_token:  claim received by admin successful interactive login
#   context_identifier: customer id, i.e. Cust12345
#

ticket = systemuser.get_system_user_ticket(
    'system_user_token', 'context_identifier')

print('System user ticket: ' + ticket)
```
