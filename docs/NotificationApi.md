# focs_gitea.NotificationApi

All URIs are relative to *http://localhost/git/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notify_get_list**](NotificationApi.md#notify_get_list) | **GET** /notifications | List users&#39;s notification threads
[**notify_get_repo_list**](NotificationApi.md#notify_get_repo_list) | **GET** /repos/{owner}/{repo}/notifications | List users&#39;s notification threads on a specific repo
[**notify_get_thread**](NotificationApi.md#notify_get_thread) | **GET** /notifications/threads/{id} | Get notification thread by ID
[**notify_new_available**](NotificationApi.md#notify_new_available) | **GET** /notifications/new | Check if unread notifications exist
[**notify_read_list**](NotificationApi.md#notify_read_list) | **PUT** /notifications | Mark notification threads as read, pinned or unread
[**notify_read_repo_list**](NotificationApi.md#notify_read_repo_list) | **PUT** /repos/{owner}/{repo}/notifications | Mark notification threads as read, pinned or unread on a specific repo
[**notify_read_thread**](NotificationApi.md#notify_read_thread) | **PATCH** /notifications/threads/{id} | Mark notification thread as read by ID


# **notify_get_list**
> list[NotificationThread] notify_get_list(all=all, status_types=status_types, since=since, before=before, page=page, limit=limit)

List users's notification threads

### Example
```python
from __future__ import print_function
import time
import focs_gitea
from focs_gitea.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = focs_gitea.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = focs_gitea.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = focs_gitea.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = focs_gitea.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = focs_gitea.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: TOTPHeader
configuration = focs_gitea.Configuration()
configuration.api_key['X-GITEA-OTP'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GITEA-OTP'] = 'Bearer'
# Configure API key authorization: Token
configuration = focs_gitea.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = focs_gitea.NotificationApi(focs_gitea.ApiClient(configuration))
all = 'all_example' # str | If true, show notifications marked as read. Default value is false (optional)
status_types = ['status_types_example'] # list[str] | Show notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread & pinned. (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Only show notifications updated after the given time. This is a timestamp in RFC 3339 format (optional)
before = '2013-10-20T19:20:30+01:00' # datetime | Only show notifications updated before the given time. This is a timestamp in RFC 3339 format (optional)
page = 56 # int | page number of results to return (1-based) (optional)
limit = 56 # int | page size of results (optional)

try:
    # List users's notification threads
    api_response = api_instance.notify_get_list(all=all, status_types=status_types, since=since, before=before, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->notify_get_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all** | **str**| If true, show notifications marked as read. Default value is false | [optional] 
 **status_types** | [**list[str]**](str.md)| Show notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread &amp; pinned. | [optional] 
 **since** | **datetime**| Only show notifications updated after the given time. This is a timestamp in RFC 3339 format | [optional] 
 **before** | **datetime**| Only show notifications updated before the given time. This is a timestamp in RFC 3339 format | [optional] 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**list[NotificationThread]**](NotificationThread.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notify_get_repo_list**
> list[NotificationThread] notify_get_repo_list(owner, repo, all=all, status_types=status_types, since=since, before=before, page=page, limit=limit)

List users's notification threads on a specific repo

### Example
```python
from __future__ import print_function
import time
import focs_gitea
from focs_gitea.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = focs_gitea.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = focs_gitea.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = focs_gitea.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = focs_gitea.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = focs_gitea.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: TOTPHeader
configuration = focs_gitea.Configuration()
configuration.api_key['X-GITEA-OTP'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GITEA-OTP'] = 'Bearer'
# Configure API key authorization: Token
configuration = focs_gitea.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = focs_gitea.NotificationApi(focs_gitea.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
all = 'all_example' # str | If true, show notifications marked as read. Default value is false (optional)
status_types = ['status_types_example'] # list[str] | Show notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread & pinned (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Only show notifications updated after the given time. This is a timestamp in RFC 3339 format (optional)
before = '2013-10-20T19:20:30+01:00' # datetime | Only show notifications updated before the given time. This is a timestamp in RFC 3339 format (optional)
page = 56 # int | page number of results to return (1-based) (optional)
limit = 56 # int | page size of results (optional)

try:
    # List users's notification threads on a specific repo
    api_response = api_instance.notify_get_repo_list(owner, repo, all=all, status_types=status_types, since=since, before=before, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->notify_get_repo_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **all** | **str**| If true, show notifications marked as read. Default value is false | [optional] 
 **status_types** | [**list[str]**](str.md)| Show notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread &amp; pinned | [optional] 
 **since** | **datetime**| Only show notifications updated after the given time. This is a timestamp in RFC 3339 format | [optional] 
 **before** | **datetime**| Only show notifications updated before the given time. This is a timestamp in RFC 3339 format | [optional] 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**list[NotificationThread]**](NotificationThread.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notify_get_thread**
> NotificationThread notify_get_thread(id)

Get notification thread by ID

### Example
```python
from __future__ import print_function
import time
import focs_gitea
from focs_gitea.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = focs_gitea.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = focs_gitea.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = focs_gitea.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = focs_gitea.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = focs_gitea.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: TOTPHeader
configuration = focs_gitea.Configuration()
configuration.api_key['X-GITEA-OTP'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GITEA-OTP'] = 'Bearer'
# Configure API key authorization: Token
configuration = focs_gitea.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = focs_gitea.NotificationApi(focs_gitea.ApiClient(configuration))
id = 'id_example' # str | id of notification thread

try:
    # Get notification thread by ID
    api_response = api_instance.notify_get_thread(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->notify_get_thread: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of notification thread | 

### Return type

[**NotificationThread**](NotificationThread.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notify_new_available**
> NotificationCount notify_new_available()

Check if unread notifications exist

### Example
```python
from __future__ import print_function
import time
import focs_gitea
from focs_gitea.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = focs_gitea.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = focs_gitea.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = focs_gitea.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = focs_gitea.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = focs_gitea.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: TOTPHeader
configuration = focs_gitea.Configuration()
configuration.api_key['X-GITEA-OTP'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GITEA-OTP'] = 'Bearer'
# Configure API key authorization: Token
configuration = focs_gitea.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = focs_gitea.NotificationApi(focs_gitea.ApiClient(configuration))

try:
    # Check if unread notifications exist
    api_response = api_instance.notify_new_available()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->notify_new_available: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NotificationCount**](NotificationCount.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notify_read_list**
> notify_read_list(last_read_at=last_read_at, all=all, status_types=status_types, to_status=to_status)

Mark notification threads as read, pinned or unread

### Example
```python
from __future__ import print_function
import time
import focs_gitea
from focs_gitea.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = focs_gitea.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = focs_gitea.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = focs_gitea.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = focs_gitea.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = focs_gitea.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: TOTPHeader
configuration = focs_gitea.Configuration()
configuration.api_key['X-GITEA-OTP'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GITEA-OTP'] = 'Bearer'
# Configure API key authorization: Token
configuration = focs_gitea.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = focs_gitea.NotificationApi(focs_gitea.ApiClient(configuration))
last_read_at = '2013-10-20T19:20:30+01:00' # datetime | Describes the last point that notifications were checked. Anything updated since this time will not be updated. (optional)
all = 'all_example' # str | If true, mark all notifications on this repo. Default value is false (optional)
status_types = ['status_types_example'] # list[str] | Mark notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread. (optional)
to_status = 'to_status_example' # str | Status to mark notifications as, Defaults to read. (optional)

try:
    # Mark notification threads as read, pinned or unread
    api_instance.notify_read_list(last_read_at=last_read_at, all=all, status_types=status_types, to_status=to_status)
except ApiException as e:
    print("Exception when calling NotificationApi->notify_read_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_read_at** | **datetime**| Describes the last point that notifications were checked. Anything updated since this time will not be updated. | [optional] 
 **all** | **str**| If true, mark all notifications on this repo. Default value is false | [optional] 
 **status_types** | [**list[str]**](str.md)| Mark notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread. | [optional] 
 **to_status** | **str**| Status to mark notifications as, Defaults to read. | [optional] 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notify_read_repo_list**
> notify_read_repo_list(owner, repo, all=all, status_types=status_types, to_status=to_status, last_read_at=last_read_at)

Mark notification threads as read, pinned or unread on a specific repo

### Example
```python
from __future__ import print_function
import time
import focs_gitea
from focs_gitea.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = focs_gitea.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = focs_gitea.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = focs_gitea.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = focs_gitea.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = focs_gitea.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: TOTPHeader
configuration = focs_gitea.Configuration()
configuration.api_key['X-GITEA-OTP'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GITEA-OTP'] = 'Bearer'
# Configure API key authorization: Token
configuration = focs_gitea.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = focs_gitea.NotificationApi(focs_gitea.ApiClient(configuration))
owner = 'owner_example' # str | owner of the repo
repo = 'repo_example' # str | name of the repo
all = 'all_example' # str | If true, mark all notifications on this repo. Default value is false (optional)
status_types = ['status_types_example'] # list[str] | Mark notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread. (optional)
to_status = 'to_status_example' # str | Status to mark notifications as. Defaults to read. (optional)
last_read_at = '2013-10-20T19:20:30+01:00' # datetime | Describes the last point that notifications were checked. Anything updated since this time will not be updated. (optional)

try:
    # Mark notification threads as read, pinned or unread on a specific repo
    api_instance.notify_read_repo_list(owner, repo, all=all, status_types=status_types, to_status=to_status, last_read_at=last_read_at)
except ApiException as e:
    print("Exception when calling NotificationApi->notify_read_repo_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **all** | **str**| If true, mark all notifications on this repo. Default value is false | [optional] 
 **status_types** | [**list[str]**](str.md)| Mark notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread. | [optional] 
 **to_status** | **str**| Status to mark notifications as. Defaults to read. | [optional] 
 **last_read_at** | **datetime**| Describes the last point that notifications were checked. Anything updated since this time will not be updated. | [optional] 

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notify_read_thread**
> notify_read_thread(id, to_status=to_status)

Mark notification thread as read by ID

### Example
```python
from __future__ import print_function
import time
import focs_gitea
from focs_gitea.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = focs_gitea.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = focs_gitea.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = focs_gitea.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = focs_gitea.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = focs_gitea.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: TOTPHeader
configuration = focs_gitea.Configuration()
configuration.api_key['X-GITEA-OTP'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GITEA-OTP'] = 'Bearer'
# Configure API key authorization: Token
configuration = focs_gitea.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = focs_gitea.NotificationApi(focs_gitea.ApiClient(configuration))
id = 'id_example' # str | id of notification thread
to_status = 'read' # str | Status to mark notifications as (optional) (default to read)

try:
    # Mark notification thread as read by ID
    api_instance.notify_read_thread(id, to_status=to_status)
except ApiException as e:
    print("Exception when calling NotificationApi->notify_read_thread: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of notification thread | 
 **to_status** | **str**| Status to mark notifications as | [optional] [default to read]

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

