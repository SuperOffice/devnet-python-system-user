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
