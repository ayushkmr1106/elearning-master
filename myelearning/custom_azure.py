from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'elearningstorageacc' # Must be replaced by your <storage_account_name>
    account_key = 'ChUnkWaFLZ4gbo6nkdQjbg2N+OgMytillvb8mhTn1+QpZRVRBa4qGBD8eFSJwlTu/zTlmAokghO7+AStD6wy9Q==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'elearningstorageacc' # Must be replaced by your storage_account_name
    account_key = 'ChUnkWaFLZ4gbo6nkdQjbg2N+OgMytillvb8mhTn1+QpZRVRBa4qGBD8eFSJwlTu/zTlmAokghO7+AStD6wy9Q==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None