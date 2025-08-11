========================
CODE SNIPPETS
========================
TITLE: Install instagrapi
DESCRIPTION: Installs the instagrapi Python library using pip. This command should be run in your terminal.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/getting-started.md#_snippet_0

LANGUAGE: bash
CODE:
```
python -m pip install instagrapi
```

----------------------------------------

TITLE: Setup.py Version Extraction
DESCRIPTION: Illustrates the technique used in `setup.py` to retrieve the package version without importing the package itself. This is crucial to avoid `ImportError` during installation from source.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/development-guide.md#_snippet_3

LANGUAGE: python
CODE:
```
# Example of version extraction logic in setup.py
# (Actual implementation uses regex to read __init__.py)
# version = get_version("instagrapi")
```

----------------------------------------

TITLE: Get User Following Example
DESCRIPTION: Illustrates fetching a user's following list and displaying the structure of the returned UserShort objects.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/user.md#_snippet_8

LANGUAGE: python
CODE:
```
>>> cl.user_following(cl.user_id)
{
  8530498223: UserShort(
    pk=8530498223,
    username="something",
    full_name="Example description",
    profile_pic_url=HttpUrl(
      'https://instagram.frix7-1.fna.fbcdn.net/v/t5...9217617140_n.jpg',
      scheme='https',
      host='instagram.frix7-1.fna.fbcdn.net',
      ...
    ),
  ),
  49114585: UserShort(
    pk=49114585,
    username='gx1000',
    full_name='GX1000',
    profile_pic_url=HttpUrl(
      'https://scontent-hel3-1.cdninstagram.com/v/t51.2885-19/10388...jpg',
      scheme='https',
      host='scontent-hel3-1.cdninstagram.com',
      ...
    )
  ),
  ...
}
```

----------------------------------------

TITLE: Enter Development Box with Docker Compose
DESCRIPTION: Starts a Docker container configured for development, allowing interactive execution of Python code and imports of the project's dependencies. This environment is useful for debugging and experimenting with the codebase.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/development-guide.md#_snippet_1

LANGUAGE: bash
CODE:
```
docker-compose run --rm devbox
```

----------------------------------------

TITLE: Instagrapi TOTP Usage Example
DESCRIPTION: Demonstrates how to use the Instagrapi library to manage Time-based One-Time Password (TOTP) for Two-Factor Authentication (2FA). This example covers logging in, generating a TOTP seed, generating a TOTP code, enabling 2FA with a code, and disabling 2FA.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/totp.md#_snippet_1

LANGUAGE: python
CODE:
```
from instagrapi import Client

# Replace with your actual username and password
USERNAME = "your_username"
PASSWORD = "your_password"

cl = Client()
cl.login(USERNAME, PASSWORD)

# Generate a TOTP seed
seed = cl.totp_generate_seed()
print(f"Generated Seed: {seed}")

# Generate a TOTP code using the seed
code = cl.totp_generate_code(seed)
print(f"Generated Code: {code}")

# Enable TOTP 2FA (requires a verification code, e.g., from Google Authenticator)
# Replace 'your_verification_code' with the actual code from your authenticator app
# backup_codes = cl.totp_enable("your_verification_code")
# print(f"Backup Codes: {backup_codes}")

# Disable TOTP 2FA
# disable_success = cl.totp_disable()
# print(f"TOTP Disabled: {disable_success}")

```

----------------------------------------

TITLE: Get User Info by Username Example
DESCRIPTION: Shows how to retrieve detailed information for a user specified by their username and convert it to a dictionary.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/user.md#_snippet_9

LANGUAGE: python
CODE:
```
>>> cl.user_info_by_username('example').dict()
{'pk': 1903424587,
 'username': 'example',
 'full_name': 'Example Example',
 'is_private': False,
 'profile_pic_url': HttpUrl('https://scontent-hel3-1.cdninstagram.com/v/t51.2885-19/s150x150/123884060_803537687159702_2508263208740189974_n.jpg?...', scheme='https', host='scontent-hel3-1.cdninstagram.com', tld='com', host_type='domain', ...),
 'is_verified': False,
 'media_count': 102,
 'follower_count': 576,
 'following_count': 538,
 'biography': 'Engineer: Python, JavaScript, Erlang',
 'external_url': HttpUrl('https://example.org/', scheme='https', host='example.org', tld='com', host_type='domain', path='/'),
 'is_business': False}
```

----------------------------------------

TITLE: Python: Instagram Highlight Management Examples
DESCRIPTION: Demonstrates practical usage of the instagrapi library for managing Instagram highlights. Includes examples for fetching highlight details, creating new highlights, modifying titles and covers, adding/removing stories, and deleting highlights.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/highlight.md#_snippet_1

LANGUAGE: python
CODE:
```
from instagrapi import Client
from pathlib import Path

cl = Client()
# cl.login(USERNAME, PASSWORD)

# Example 1: Get highlight info and print its dictionary representation
print(cl.highlight_info(17895485201104054).dict())

# Example 2: Get all highlights for a specific user
print(cl.user_highlights(29817608135))

# Example 3: Create a new highlight with a title and story IDs
print(cl.highlight_create("Test", ["2722223419628084989_29817608135"]))

# Example 4: Change the title of an existing highlight
print(cl.highlight_change_title(17907771728171896, "Example title"))

# Example 5: Change the cover of an existing highlight (requires a valid image path)
# print(cl.highlight_change_cover(17907771728171896, Path("/tmp/test.jpg")))

# Example 6: Add stories to an existing highlight
print(cl.highlight_add_stories(17907771728171896, ["2722223419628084989"]))

# Example 7: Remove stories from an existing highlight
print(cl.highlight_remove_stories(17907771728171896, ["2722223419628084989"]))

# Example 8: Delete a highlight
# print(cl.highlight_delete("17920472818962144"))
```

----------------------------------------

TITLE: Install instagrapi Package
DESCRIPTION: Installs the instagrapi Python library using pip. This is the initial step required before using the library's functionalities.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/README.md#_snippet_4

LANGUAGE: bash
CODE:
```
pip install instagrapi
```

----------------------------------------

TITLE: Download Story Media Example
DESCRIPTION: Demonstrates how to download story media using the instagrapi client, first by obtaining the story's primary key from a URL and then downloading the media.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/story.md#_snippet_2

LANGUAGE: python
CODE:
```
from instagrapi import Client

cl = Client()
# cl.login(USERNAME, PASSWORD) # Uncomment and replace with your credentials

# Example 1: Download story media by extracting PK from URL
story_url = 'https://www.instagram.com/stories/example/2581281926631793076/'
story_pk = cl.story_pk_from_url(story_url)
print(f"Downloaded story media: {cl.story_download(story_pk)}")

# Example 2: Download story media using its direct URL (e.g., video or thumbnail)
s = cl.story_info(2581281926631793076) # Fetch story info to get URLs

# Download video
print(f"Downloaded video from URL: {cl.story_download_by_url(s.video_url)}")

# Download thumbnail
print(f"Downloaded thumbnail from URL: {cl.story_download_by_url(s.thumbnail_url)}")
```

----------------------------------------

TITLE: Instagrapi Client Usage Examples
DESCRIPTION: Demonstrates common operations using the Instagrapi client, including fetching user IDs, retrieving detailed user information, and processing follower lists.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/user.md#_snippet_5

LANGUAGE: Python
CODE:
```
from instagrapi import Client
from instagrapi.types import UserShort, HttpUrl

# Assuming 'cl' is an authenticated Client instance
# cl = Client()
# cl.login(USERNAME, PASSWORD)

# Example 1: Get user's follower IDs
# print(cl.user_followers(cl.user_id).keys())

# Example 2: Fetch and display user following information
# print(cl.user_following(cl.user_id))

# Example 3: Get and display user info by username
# print(cl.user_info_by_username('example').dict())
```

----------------------------------------

TITLE: Download Video by URL Example
DESCRIPTION: Fetches a video's URL and then downloads it to a specified folder, returning the path to the saved file.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/media.md#_snippet_16

LANGUAGE: Python
CODE:
```
>>> video_url = cl.media_info(1913256444155036809).video_url
>>> cl.video_download_by_url(video_url, folder='/tmp')
PosixPath('/tmp/45588546_367538213983456_6830188946193737023_n.mp4')
```

----------------------------------------

TITLE: Python Example: Account Picture Change
DESCRIPTION: Illustrates how to change the user's profile picture. This involves downloading a media item to get a local path and then passing that path to the account_change_picture method.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/account.md#_snippet_2

LANGUAGE: python
CODE:
```
from instagrapi import Client
from pathlib import Path

USERNAME = "your_username"
PASSWORD = "your_password"

cl = Client()
cl.login(USERNAME, PASSWORD)

# Get media PK from a URL
media_pk = cl.media_pk_from_url('https://www.instagram.com/p/BWnh360Fitr/')

# Download the media to a temporary folder
profile_pic_path: Path = cl.photo_download(media_pk, folder='/tmp')

# Change the profile picture using the downloaded path
updated_user_short = cl.account_change_picture(profile_pic_path)
print(updated_user_short)
```

----------------------------------------

TITLE: Get User Followers Example
DESCRIPTION: Demonstrates how to retrieve and inspect the keys (user IDs) of a user's followers using the instagrapi client.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/user.md#_snippet_7

LANGUAGE: python
CODE:
```
>>> cl.user_followers(cl.user_id).keys()
dict_keys([5563084402, 43848984510, 1498977320, ...])
```

----------------------------------------

TITLE: Instagrapi Python Example: Fetching Hashtag Media
DESCRIPTION: Demonstrates how to log in to Instagrapi and fetch top media posts for a given hashtag. Shows retrieving hashtag info and then media details.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/hashtag.md#_snippet_1

LANGUAGE: python
CODE:
```
from instagrapi import Client

# Assuming USERNAME and PASSWORD are defined elsewhere
# USERNAME = "your_username"
# PASSWORD = "your_password"

cl = Client()
cl.login(USERNAME, PASSWORD)

# Get hashtag info
hashtag = cl.hashtag_info('downhill')
print(hashtag.dict())

# Get top media for a hashtag
medias_top = cl.hashtag_medias_top('downhill', amount=2)
print(medias_top[0].dict())

# Get recent media for a hashtag
medias_recent = cl.hashtag_medias_recent('downhill', amount=2)
# print(medias_recent[0].dict()) # Uncomment to print recent media details
```

----------------------------------------

TITLE: Python Example: Email and Phone Confirmation
DESCRIPTION: Shows how to send confirmation codes to a new email address or phone number. Demonstrates the expected dictionary return format for successful and unsuccessful attempts.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/account.md#_snippet_3

LANGUAGE: python
CODE:
```
from instagrapi import Client

USERNAME = "your_username"
PASSWORD = "your_password"

cl = Client()
cl.login(USERNAME, PASSWORD)

# Send confirmation email
email_response = cl.send_confirm_email("addr@example.com")
print(email_response)

# Send confirmation phone number
phone_response = cl.send_confirm_phone_number("+5599999999")
print(phone_response)
```

----------------------------------------

TITLE: Download Album Example
DESCRIPTION: Downloads all items (photos and videos) from an Instagram album associated with a given media primary key.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/media.md#_snippet_17

LANGUAGE: Python
CODE:
```
>>> cl.media_pk_from_url("http://www.instagram.com/p/BjNLpA1AhXM/")
1787135824035452364

>>> cl.album_download(1787135824035452364)
[PosixPath('/app/example_1787135361353462176.mp4'),
 PosixPath('/app/example_1787135762219834098.mp4'),
 PosixPath('/app/example_1787133803186894424.jpg')]
```

----------------------------------------

TITLE: Paginate Hashtag Media (v1 Chunk)
DESCRIPTION: Example demonstrating how to fetch media chunks for a hashtag and use the returned cursor for subsequent requests to load more posts.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/hashtag.md#_snippet_8

LANGUAGE: python
CODE:
```
>>> medias, cursor = cl.hashtag_medias_v1_chunk('test', max_amount=32, tab_key='recent')
>>> len(medias)
32
>>> cursor
QVFDR0dzT3FJT0V4amFjMaQ3czlGVzRKV3FNWDJqaE1mWmltWU5VWGYtbnV6RVpoOUlsR3dCN05RRmpLc2R5SVlCQTNaekV5bUVOV0F4Vno1MDkxN1Nndg==

# NEXT cursor:

>>> medias, cursor = cl.hashtag_medias_v1_chunk('test', max_amount=32, tab_key='recent', max_id=cursor)
>>> len(medias)
32
>>> cursor
QVFEUXpfM0RtaDdmMExPQ0k0UWRlaHFJa2RVdVlaX01LTzhkNF9Dd1N2UlhtVy1vSTZvMERfYW5XN205OTBRNFBCSVJ2ZTVfTG5ZMXVmY0VJbUM5TU9URQ==
```

----------------------------------------

TITLE: Set Breakpoint in Python with pdb++
DESCRIPTION: Inserts a breakpoint in Python code using the `breakpoint()` function, which leverages the installed `pdb++` debugger within the Docker environment. When execution reaches this line, it drops into an interactive debugging session.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/development-guide.md#_snippet_2

LANGUAGE: python
CODE:
```
def my_function():
    breakpoint()
    ...
```

----------------------------------------

TITLE: Instagrapi: Login and Get Media PK from Code
DESCRIPTION: Demonstrates initializing the Instagrapi client, logging in with user credentials, and retrieving the primary key (PK) of an Instagram media item using its short code. Requires USERNAME and PASSWORD to be defined.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/media.md#_snippet_8

LANGUAGE: python
CODE:
```
from instagrapi import Client

USERNAME = "your_username"
PASSWORD = "your_password"

cl = Client()
cl.login(USERNAME, PASSWORD)

media_code = "B-fKL9qpeab"
media_pk = cl.media_pk_from_code(media_code)
print(f"Media PK for code {media_code}: {media_pk}")
```

----------------------------------------

TITLE: Python Example: Fetching Instagram Insights
DESCRIPTION: Demonstrates how to log in to Instagram and use the instagrapi client to fetch media feed insights, account statistics, and specific media insights.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/insight.md#_snippet_1

LANGUAGE: python
CODE:
```
from instagrapi import Client

cl = Client()
cl.login(USERNAME, PASSWORD)

# Fetch insights for all videos from the last week, ordered by like count
cl.insights_media_feed_all("VIDEO", "ONE_WEEK", "LIKE_COUNT", 42)

# Get account-level statistics
cl.insights_account()

# Get insights for a specific media using its URL
media_pk = cl.media_pk_from_url('https://www.instagram.com/p/CP5h-I1FuPr/')
cl.insights_media(media_pk)
```

----------------------------------------

TITLE: Python Example: Account Info and Edit
DESCRIPTION: Demonstrates how to log in, retrieve account information, and update profile details like the external URL using the instagrapi library. Shows fetching account details and modifying the external URL.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/account.md#_snippet_1

LANGUAGE: python
CODE:
```
from instagrapi import Client

USERNAME = "your_username"
PASSWORD = "your_password"

cl = Client()
cl.login(USERNAME, PASSWORD)

# Get account info
account_details = cl.account_info()
print(account_details.dict())

# Edit account details, e.g., external URL
updated_account = cl.account_edit(external_url='https://github.com/subzeroid/instagrapi')
print(updated_account)
```

----------------------------------------

TITLE: Instagrapi Basic Direct Messaging Examples
DESCRIPTION: Demonstrates fundamental direct messaging operations using the Instagrapi library, including logging in, fetching threads, and accessing thread details like user information and messages.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/direct.md#_snippet_1

LANGUAGE: python
CODE:
```
from instagrapi import Client

# Replace with your actual username and password
USERNAME = "YOUR_USERNAME"
PASSWORD = "YOUR_PASSWORD"

cl = Client()
cl.login(USERNAME, PASSWORD)

# Get the first direct thread and print its primary key and users
thread = cl.direct_threads(1)[0]
print(f"Thread PK: {thread.pk}")
print(f"Thread Users: {thread.users}")

# Access and print details of the first message in the thread
if thread.messages:
    print(f"First Message: {thread.messages[0]}")

# Get the first thread from the pending inbox
pending_thread = cl.direct_pending_inbox(1)[0]
print(f"Pending Thread PK: {pending_thread.pk}")

```

----------------------------------------

TITLE: Instagrapi Notes Python Usage Example
DESCRIPTION: Demonstrates how to use the Instagrapi library in Python to create, retrieve, and delete Instagram Notes. Includes example output for created notes and retrieved note lists.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/notes.md#_snippet_1

LANGUAGE: python
CODE:
```
>>> # Assuming 'cl' is an authenticated Instagrapi client instance
>>> note = cl.create_note("Hello from Instagrapi, everyone can see it!", 0)
>>> print(note.dict())
{'id': '17849203563031468', 
'text': 'Hello from Instagrapi, everyone can see it!', 
'user_id': 12312312312, 
'user': {
  'pk': '12312312312', 
  'username': 'something', 
  'full_name': 'merimi on top',
  'profile_pic_url': 'https://scontent-dus1-1.cdninstagram.com/v/t51.2885-19/364347953_6289474204435297_7603222331512295081_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent-dus1-1.cdninstagram.com&_nc_cat=101&_nc_ohc=DVaE0MQwn0YAX8-S8dm&edm=AE-H4JwBAAAA&ccb=7-5&oh=00_AfAnH4mHGMl7B5tqzU7b9PMz9qSC4QE_-EX067lwPHnN1w&oe=64DDA1CB&_nc_sid=cff473', 
  'profile_pic_url_hd': None, 
  'is_private': False, 
  'stories': []},
'audience': 0, 
'created_at': '2023-08-13T14:33:43+00:00',
'expires_at': '2023-08-14T14:33:43+00:00',
'is_emoji_only': False, 
'has_translation': False, 
'note_style': 0}

>>> notes = cl.get_notes()
>>> print(notes)
[Note(id='17849203563031468', text='Hello from Instagrapi, everyone can see it!', ..., has_translation=False, note_style=0), Note(id='17902958207826742', text='Am so happy 💃💃💃💃🙈🤭', ..., has_translation=False, note_style=0)]

>>> cl.last_seen_update_note()

>>> cl.delete_note(note.id)
```

----------------------------------------

TITLE: Search Places by Name
DESCRIPTION: Illustrates how to search for places by their name. The example retrieves a specific place from the search results and accesses its dictionary representation.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/location.md#_snippet_4

LANGUAGE: python
CODE:
```
>>> place = cl.fbsearch_places('Perch')[2]
>>> place.dict()
{
 'pk': 3824034,
 'name': 'Perch',
 'phone': '',
 'website': '',
 'category': '',
 'hours': {},
 'address': None,
 'city': None,
 'zip': None,
 'lng': -118.25135,
 'lat': 34.04882,
 'external_id': 207298912632228,
 'external_id_source': 'facebook_places'
}
```

----------------------------------------

TITLE: Instagrapi: Get User Media (GQL)
DESCRIPTION: Demonstrates fetching a user's media using the GraphQL API, specifying the user's PK and the desired amount of media. Returns a list of media objects, each containing detailed information.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/media.md#_snippet_13

LANGUAGE: python
CODE:
```
from instagrapi import Client

USERNAME = "your_username"
PASSWORD = "your_password"

cl = Client()
cl.login(USERNAME, PASSWORD)

user_id = 1903424587 # Example User PK

# Fetch the latest media for the user
user_media = cl.user_medias_gql(user_id, amount=1)

if user_media:
    print(user_media[0].dict())
else:
    print(f"No media found for user ID {user_id}")
```

----------------------------------------

TITLE: Instagrapi Client Initialization and Basic Usage
DESCRIPTION: Demonstrates how to initialize the instagrapi client, log in to an Instagram account, set proxy configurations, and retrieve basic account information. It includes examples for standard login, login with 2FA, and login via session ID.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/interactions.md#_snippet_0

LANGUAGE: python
CODE:
```
from instagrapi import Client

# Initialize client with optional settings
# settings = {
#    "uuids": {
#       "phone_id": "57d64c41-a916-3fa5-bd7a-3796c1dab122",
#       "uuid": "8aa373c6-f316-44d7-b49e-d74563f4a8f3",
#       "client_session_id": "6c296d0a-3534-4dce-b5aa-a6a6ab017443",
#       "advertising_id": "8dc88b76-dfbc-44dc-abbc-31a6f1d54b04",
#       "device_id": "android-e021b636049dc0e9"
#    },
#    "cookies":  {},
#    "last_login": 1596069420.0000145,
#    "device_settings": {
#       "cpu": "h1",
#       "dpi": "640dpi",
#       "model": "h1",
#       "device": "RS988",
#       "resolution": "1440x2392",
#       "app_version": "117.0.0.28.123",
#       "manufacturer": "LGE/lge",
#       "version_code": "168361634",
#       "android_release": "6.0.1",
#       "android_version": 23
#    },
#    "user_agent": "Instagram 117.0.0.28.123 Android (23/6.0.1; ...US; 168361634)"
# }
# cl = Client(settings)

cl = Client()

# Login examples
cl.login("instagrapi", "42")
# cl.login("instagrapi", "42", verification_code="123456")  # with 2FA verification_code
# cl.login_by_sessionid("peiWooShooghahdi2Eip7phohph0eeng")

# Proxy settings
cl.set_proxy("socks5://127.0.0.1:30235")
# cl.set_proxy("http://username:password@127.0.0.1:8080")
# cl.set_proxy("socks5://username:password@127.0.0.1:30235")
# cl.set_proxy("socks5h://username:password@exampleproxy.tld:30235")

# Get settings and user info
print(cl.get_settings())
print(cl.user_info(cl.user_id))

```

----------------------------------------

TITLE: Instagrapi User Clips Fetch Example
DESCRIPTION: Demonstrates how to fetch Reels (clips) for a specific user ID using the instagrapi library's `user_clips_v1` method. It shows retrieving the first clip and accessing its data as a dictionary.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/media.md#_snippet_23

LANGUAGE: Python
CODE:
```
>>> clips = cl.user_clips_v1(25025320, amount=2)
>>> clips[0].dict()

{
 'pk': '3052048407587698594',
 'id': '3052048407587698594_25025320',
 'code': 'CpbDdszj7ei',
 'taken_at': datetime.datetime(2023, 3, 5, 21, 50, 4, tzinfo=datetime.timezone.utc),
 'media_type': 2,
 'product_type': 'clips',
 'thumbnail_url': 'https://scontent-den4-1.cdninstagram.com/v/t51.2885-15/333966975_152901010970043_8971338145148712917_n.jpg?stp=dst-jpg_e15_p150x150&_nc_ht=scontent-den4-1.cdninstagram.com&_nc_cat=1&_nc_ohc=rRuJ7u4YrqEAX-UEMFq&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=MzA1MjA0ODQwNzU4NzY5ODU5NA%3D%3D.2-ccb7-5&oh=00_AfC_tNEWVjJLM5RQYUiQJFHQZSmvnDtAcpzs42DRSYt1pQ&oe=6409C451&_nc_sid=4a9e64',
 'location': {
  'pk': 213011753,
  'name': 'Sydney, Australia',
  'phone': '',
  'website': '',
  'category': '',
  'hours': {},
  'address': '',
  'city': '',
  'zip': None,
  'lng': 151.20797,
  'lat': -33.86751,
  'external_id': 110884905606108,
  'external_id_source': 'facebook_places'
 }
}

```

----------------------------------------

TITLE: Instagrapi Download Track by URL
DESCRIPTION: Downloads a music track to a specified folder using its URI. This example first retrieves the track URI and then initiates the download.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/track.md#_snippet_3

LANGUAGE: python
CODE:
```
from instagrapi import Client
from instagrapi.types import HttpUrl
from pathlib import Path

cl = Client()
# Assuming cl is already logged in
# cl.login(USERNAME, PASSWORD)

# Example canonical ID to get track URI
canonical_id = '18159860503036324'
track_info = cl.track_info_by_canonical_id(canonical_id)
track_uri: HttpUrl = track_info.uri

# Specify download folder
download_folder = "/tmp"

# Download the track
downloaded_path: Path = cl.track_download_by_url(track_uri, folder=download_folder)
print(f"Track downloaded to: {downloaded_path}")
```

----------------------------------------

TITLE: Run Tests with Docker Compose
DESCRIPTION: Executes the project's test suite, linting, and code coverage checks within a Docker container. This command ensures that all automated quality checks pass before code merging, mirroring the CI pipeline.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/development-guide.md#_snippet_0

LANGUAGE: bash
CODE:
```
docker-compose run --rm test
```

----------------------------------------

TITLE: Upload Story with Mentions, Links, Hashtags, and Polls Example
DESCRIPTION: Illustrates uploading a video to an Instagram story, including tagging other users, adding a swipe-up link, a hashtag, and a poll using instagrapi.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/story.md#_snippet_3

LANGUAGE: python
CODE:
```
from instagrapi import Client
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag, StoryPoll
from pathlib import Path

# Replace with your actual username and password
USERNAME = "your_username"
PASSWORD = "your_password"

cl = Client()
cl.login(USERNAME, PASSWORD)

# --- Prepare data for upload ---
# Get media PK to use in StoryMedia (optional, for referencing other media)
media_pk = cl.media_pk_from_url('https://www.instagram.com/p/CGgDsi7JQdS/')

# Download media to upload (replace with your actual media path or download logic)
# For demonstration, assume 'media_path' is a Path object to a video file
# media_path = cl.video_download(media_pk) # Example if you want to download first
media_path = Path("/path/to/your/video.mp4") # Replace with actual path

# Get user info for mention
example_user = cl.user_info_by_username('instagram') # Example: tag the official Instagram account

# Get hashtag info
hashtag_info = cl.hashtag_info('instagram')

# --- Upload story ---
cl.video_upload_to_story(
    media_path,
    "Check out this cool feature! #instagrapi",
    thumbnail=None, # Optional: path to a thumbnail image
    mentions=[StoryMention(user=example_user, x=0.49892962, y=0.703125, width=0.8333333333333334, height=0.125)],
    links=[StoryLink(webUri='https://github.com/subzeroid/instagrapi')],
    hashtags=[StoryHashtag(hashtag=hashtag_info, x=0.23, y=0.32, width=0.5, height=0.22)],
    medias=[StoryMedia(media_pk=media_pk, x=0.5, y=0.5, width=0.6, height=0.8)], # Reference another media
    polls=[StoryPoll(x = 0.5, y = 0.5, width = 0.7, height = 0.5, question = "What do you think?", options = ["Great", "Awesome"])]
    # extra_data={"audience": "besties"} # Uncomment to upload to close friends
)

print("Story uploaded successfully!")
```

----------------------------------------

TITLE: Instagrapi Location Data Handling Example
DESCRIPTION: Demonstrates a typical workflow for using Instagrapi's location features, including logging in, searching for a location by coordinates, retrieving and completing location details, building serialized data, fetching location information, and retrieving top media posts.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/location.md#_snippet_1

LANGUAGE: python
CODE:
```
from instagrapi import Client

# Assuming USERNAME and PASSWORD are defined elsewhere
# cl = Client()
# cl.login(USERNAME, PASSWORD)

# Example usage:
# location_search_result = cl.location_search(59.96, 30.29)
# if location_search_result:
#     first_location = location_search_result[0]
#     print(first_location.dict())

#     completed_location = cl.location_complete(first_location)
#     print(completed_location.dict())

#     serialized_location = cl.location_build(completed_location)
#     print(serialized_location)

#     location_info = cl.location_info(107617247320879)
#     print(location_info.dict())

#     top_medias = cl.location_medias_top(107617247320879, amount=2)
#     if top_medias:
#         print(top_medias[0].dict())

# fb_places = cl.fbsearch_places("New York")
# print(fb_places)
```

----------------------------------------

TITLE: Configuring Location and Timezone Settings
DESCRIPTION: Example demonstrating how to configure proxy, locale, and timezone settings for different geographical locations (Los Angeles and Moscow) to simulate user activity from those regions.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/interactions.md#_snippet_6

LANGUAGE: python
CODE:
```
# Los Angles user:
cl = Client()
cl.set_proxy('http://los:angeles@proxy.address:8080')
cl.set_locale('en_US')
cl.set_timezone_offset(-7 * 60 * 60)  # Los Angeles UTC (GMT) -7 hours == -25200 seconds
print(cl.get_settings())
# Expected output snippet:
# {
#     ...
#     'user_agent': 'Instagram 194.0.0.36.172 Android (26/8.0.0; 480dpi; 1080x1920; Xiaomi; MI 5s; capricorn; qcom; en_US; 301484483)',
#     'country': 'US',
#     'country_code': 1,
#     'locale': 'en_US',
#     'timezone_offset': -25200
# }

# Moscow user:
cl = Client()
cl.set_proxy('socks5://moscow:proxy@address:8080')
cl.set_locale('ru_RU')
cl.set_country_code(7)  # +7
cl.set_timezone_offset(3 * 3600)  # Moscow UTC+3
print(cl.get_settings())
# Expected output snippet:
# {
#     ...
#     'user_agent': 'Instagram 194.0.0.36.172 Android (26/8.0.0; 480dpi; 1080x1920; Xiaomi; MI 5s; capricorn; qcom; ru_RU; 301484483)',
#     'country': 'RU',
#     'country_code': 7,
#     'locale': 'ru_RU',
#     'timezone_offset': 10800
# }
```

----------------------------------------

TITLE: Python: Photo Upload with Usertags and Location using Instagrapi
DESCRIPTION: Shows how to upload a photo with additional metadata like user tags and location using instagrapi. This example includes fetching user information and creating Location objects. It builds upon the basic upload by adding `usertags` and `location` parameters.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/media.md#_snippet_21

LANGUAGE: python
CODE:
```
from instagrapi import Client
from instagrapi.types import Usertag, Location

cl = Client()
cl.login(USERNAME, PASSWORD)

example = cl.user_info_by_username('example')
media = cl.photo_upload(
    "/app/image.jpg",
    "Test caption for photo with #hashtags and mention users such @example",
    usertags=[Usertag(user=example, x=0.5, y=0.5)],
    location=Location(name='Russia, Saint-Petersburg', lat=59.96, lng=30.29)
)

media.dict()
```

----------------------------------------

TITLE: Instagrapi Hashtag Media Chunk Example
DESCRIPTION: Demonstrates how to fetch paginated media items for a hashtag using the `hashtag_medias_v1_chunk` method. It shows how to retrieve an initial chunk of media and then use the returned cursor (`max_id`) to fetch subsequent pages of results.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/hashtag.md#_snippet_5

LANGUAGE: python
CODE:
```
>>> # Initial request to get the first chunk of recent media
>>> medias, cursor = cl.hashtag_medias_v1_chunk('test', max_amount=32, tab_key='recent')
>>> len(medias)
32
>>> cursor
'QVFDR0dzT3FJT0V4amFjMaQ3czlGVzRKV3FNWDJqaE1mWmltWU5VWGYtbnV6RVpoOUlsR3dCN05RRmpLc2R5SVlCQTNaekV5bUVOV0F4Vno1MDkxN1Nndg=='

>>> # NEXT cursor: Request the next chunk of media using the previous cursor
>>> medias, cursor = cl.hashtag_medias_v1_chunk('test', max_amount=32, tab_key='recent', max_id=cursor)
>>> len(medias)
32
>>> cursor
'QVFEUXpfM0RtaDdmMExPQ0k0UWRlaHFJa2RVdVlaX01LTzhkNF9Dd1N2UlhtVy1vSTZvMERfYW5XN205OTBRNFBCSVJ2ZTVfTG5ZMXVmY0VJbUM5TU9URQ=='
```

----------------------------------------

TITLE: Python Example: News Inbox
DESCRIPTION: Demonstrates fetching inbox news, including story mentions and login activity notifications. The output is a dictionary containing counts, last checked timestamp, and details of new and old stories.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/account.md#_snippet_5

LANGUAGE: python
CODE:
```
from instagrapi import Client

USERNAME = "your_username"
PASSWORD = "your_password"

cl = Client()
cl.login(USERNAME, PASSWORD)

# Get news inbox data
inbox_data = cl.news_inbox_v1()
print(inbox_data)
```

----------------------------------------

TITLE: Instagrapi: Get Media Information
DESCRIPTION: Shows how to retrieve detailed information about a specific media item using its primary key (PK). The output is returned as a dictionary, providing various attributes like likes, comments, caption, and user details.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/media.md#_snippet_10

LANGUAGE: python
CODE:
```
from instagrapi import Client

USERNAME = "your_username"
PASSWORD = "your_password"

cl = Client()
cl.login(USERNAME, PASSWORD)

media_pk = 1787135824035452364 # Example PK
media_info = cl.media_info(media_pk)
print(media_info.dict())
```

----------------------------------------

TITLE: Instagram Media Data Structure Example
DESCRIPTION: Illustrates the typical dictionary structure returned for Instagram media items, including details like like count, caption text, user tags, and video URLs. This structure is often a result of API calls.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/media.md#_snippet_22

LANGUAGE: Python
CODE:
```
{
 'like_count': 0,
 'has_liked': None,
 'caption_text': 'Test caption for photo with #hashtags and mention users such @example',
 'usertags': [
  {
   'user': {
    'pk': 1903424587,
    'username': 'example',
    'full_name': 'Example Example',
    'profile_pic_url': 'https://instagram.fhel5-1.fna.fbcdn.net/v/t51.2885-19/s150x150/156689363_269505058076642_6448820957073669709_n.jpg?tp=1&_nc_ht=instagram.fhel5-1.fna.fbcdn.net&_nc_ohc=EtzrL0pAdg8AX-Xq8yS&edm=ACqnv0EBAAAA&ccb=7-4&oh=e2fd6a9d362f8587ea8123f23b248f1b&oe=60C2CB91&_nc_sid=9ec724',
    'stories': []
   },
   'x': 0.5,
   'y': 0.5
  }
 ],
 'video_url': None,
 'view_count': 0,
 'video_duration': 0.0,
 'title': '',
 'resources': []
}
```

----------------------------------------

TITLE: Instagrapi: Get Media PK from URL
DESCRIPTION: Illustrates how to fetch the primary key (PK) of an Instagram media item by providing its complete URL. This is useful for identifying media when only a URL is available.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/media.md#_snippet_9

LANGUAGE: python
CODE:
```
from instagrapi import Client

USERNAME = "your_username"
PASSWORD = "your_password"

cl = Client()
cl.login(USERNAME, PASSWORD)

media_url = "https://www.instagram.com/p/BjNLpA1AhXM/"
media_pk = cl.media_pk_from_url(media_url)
print(f"Media PK for URL {media_url}: {media_pk}")
```

----------------------------------------

TITLE: Instagrapi Python Example: Commenting on Posts
DESCRIPTION: Demonstrates how to use the Instagrapi library in Python to log in, find a media post, add comments (including replies), retrieve comments, and fetch them in chunks.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/comment.md#_snippet_1

LANGUAGE: python
CODE:
```
from instagrapi import Client

# Replace with your actual username and password
USERNAME = "YOUR_USERNAME"
PASSWORD = "YOUR_PASSWORD"

# Initialize the client
cl = Client()

# Login to Instagram
cl.login(USERNAME, PASSWORD)

# Get media ID from a URL
media_url = 'https://www.instagram.com/p/ByU3LAslgWY/'
media_id = cl.media_id(cl.media_pk_from_url(media_url))

# Add a new comment
print(f"Adding a comment to media ID: {media_id}")
comment = cl.media_comment(media_id, "Test comment")
print(f"Comment added: {comment.pk}")

# Add a reply to the previous comment
print(f"Replying to comment ID: {comment.pk}")
reply_comment = cl.media_comment(media_id, "Test comment 2", replied_to_comment_id=comment.pk)
print(f"Reply comment added: {reply_comment.pk}")

# Get all comments for the media
print(f"Fetching all comments for media ID: {media_id}")
comments = cl.media_comments(media_id)
print(f"Retrieved {len(comments)} comments.")
if comments:
    print(f"First comment PK: {comments[0].pk}, Text: {comments[0].text}")

# Get comments in chunks
print(f"Fetching comments in chunks for media ID: {media_id}")
comments_part1, next_min_id = cl.media_comments_chunk(media_id, 100)
print(f"Fetched {len(comments_part1)} comments in the first chunk.")
if next_min_id:
    print(f"Next min_id for pagination: {next_min_id}")
    # Example of fetching the next chunk if needed
    # comments_part2, next_min_id_2 = cl.media_comments_chunk(media_id, 100, min_id=next_min_id)
    # print(f"Fetched {len(comments_part2)} comments in the second chunk.")
else:
    print("No more comments available in chunks.")

# Example of liking a comment (replace with a valid comment_pk)
# try:
#     cl.comment_like(comment.pk)
#     print(f"Liked comment {comment.pk}")
# except Exception as e:
#     print(f"Could not like comment {comment.pk}: {e}")

# Example of unliking a comment (replace with a valid comment_pk)
# try:
#     cl.comment_unlike(comment.pk)
#     print(f"Unliked comment {comment.pk}")
# except Exception as e:
#     print(f"Could not unlike comment {comment.pk}: {e}")

# Example of pinning a comment (replace with a valid comment_pk)
# try:
#     cl.comment_pin(media_id, comment.pk)
#     print(f"Pinned comment {comment.pk}")
# except Exception as e:
#     print(f"Could not pin comment {comment.pk}: {e}")

# Example of unpinning a comment (replace with a valid comment_pk)
# try:
#     cl.comment_unpin(media_id, comment.pk)
#     print(f"Unpinned comment {comment.pk}")
# except Exception as e:
#     print(f"Could not unpin comment {comment.pk}: {e}")

# Example of bulk deleting comments (replace with valid comment_pks)
# try:
#     # Ensure you have comments to delete, e.g., comment.pk and reply_comment.pk
#     comments_to_delete = [comment.pk, reply_comment.pk]
#     cl.comment_bulk_delete(media_id, comments_to_delete)
#     print(f"Deleted comments: {comments_to_delete}")
# except Exception as e:
#     print(f"Could not delete comments {comments_to_delete}: {e}")

```

----------------------------------------

TITLE: Release Instagrapi using Python Build and Twine
DESCRIPTION: To release a new version of the Instagrapi library, you need to execute specific build and upload commands. The `python -m build` command compiles the project into distributable artifacts (like wheels and source distributions) stored in the 'dist/' directory. Subsequently, `twine upload dist/*` uploads these artifacts to the Python Package Index (PyPI), making the library available for installation by others.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/README.md#_snippet_10

LANGUAGE: Python
CODE:
```
python -m build
twine upload dist/*
```

----------------------------------------

TITLE: Instagram Media Data Structure Example
DESCRIPTION: Demonstrates the structure of Instagram media data, likely obtained from the instagrapi library. It includes details like primary key, ID, caption, user information, and resource URLs. This format is useful for parsing and processing fetched media content.

SOURCE: https://github.com/subzeroid/instagrapi/blob/master/docs/usage-guide/hashtag.md#_snippet_2

LANGUAGE: Python
CODE:
```
>>> medias[0].dict()
{
    'pk': 2574205305714324167,
    'id': '2574205305714324167_2984719638',
    'code': 'CO5ahY6BzLH',
    'taken_at': datetime.datetime(2021, 5, 15, 14, 33, 27, tzinfo=datetime.timezone.utc),
    'media_type': 8,
    'product_type': '',
    'thumbnail_url': None,
    'location': {
        'pk': 703017966745848,
        'name': 'Le Canyon Du Diable',
        'address': '',
        'lng': 3.4480762482,
        'lat': 43.6966105493,
        'external_id': 703017966745848,
        'external_id_source': 'facebook_places'
    },
    'user': {
        'pk': 2984719638,
        'username': 'lilian.champion',
        'full_name': 'Lilian \ud83c\uddeb\uddf7',
        'profile_pic_url': HttpUrl('https://scontent-hel3-1.cdninstagram.com/v/t51.2885-19/s150x150/169115203_291696755653751_6779914563403118432_n.jpg?tp=1&_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_ohc=VEqYwd5W1FYAX_7ID-6&edm=AP_V10EBAAAA&ccb=7-4&oh=7fe193da2e706c0cafd9e1d432734891&oe=60C59786&_nc_sid=4f375e', scheme='https', host='scontent-hel3-1.cdninstagram.com', tld='com', host_type='domain', path='/v/t51.2885-19/s150x150/169115203_291696755653751_6779914563403118432_n.jpg', query='tp=1&_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_ohc=VEqYwd5W1FYAX_7ID-6&edm=AP_V10EBAAAA&ccb=7-4&oh=7fe193da2e706c0cafd9e1d432734891&oe=60C59786&_nc_sid=4f375e'),
        'stories': []
    },
    'comment_count': 0,
    'like_count': 0,
    'has_liked': None,
    'caption_text': "Quand on te prend en photo sans que tu aies demandé et que la personne t'envoie tout par mail après...\ud83d\ude02\ud83d\ude0e\ud83d\udc4c\n\n#downhill #mountainlovers #ytowners #vanlife #vanlifefrance",
    'usertags': [],
    'video_url': None,
    'view_count': 0,
    'video_duration': 0.0,
    'title': '',
    'resources': [
        {
            'pk': 2574205301050111226,
            'video_url': None,
            'thumbnail_url': HttpUrl('https://instagram.fhel3-1.fna.fbcdn.net/v/t51.2885-15/e35/184312115_2977220092557985_8274386175388868273_n.jpg?tp=1&_nc_ht=instagram.fhel3-1.fna.fbcdn.net&_nc_cat=101&_nc_ohc=YoLLGA0cAhsAX8MxnSo&edm=AP_V10EBAAAA&ccb=7-4&oh=b0f2740aaff1d80c5f5219ffa267a186&oe=60C4273E&_nc_sid=4f375e', scheme='https', host='instagram.fhel3-1.fna.fbcdn.net', tld='net', host_type='domain', path='/v/t51.2885-15/e35/184312115_2977220092557985_8274386175388868273_n.jpg', query='tp=1&_nc_ht=instagram.fhel3-1.fna.fbcdn.net&_nc_cat=101&_nc_ohc=YoLLGA0cAhsAX8MxnSo&edm=AP_V10EBAAAA&ccb=7-4&oh=b0f2740aaff1d80c5f5219ffa267a186&oe=60C4273E&_nc_sid=4f375e'),
            'media_type': 1
        },
        {
            'pk': 2574205301083731874,
            'video_url': None,
            'thumbnail_url': HttpUrl('https://instagram.fhel6-1.fna.fbcdn.net/v/t51.2885-15/e35/186524178_143770224434390_4909324648747352588_n.jpg?tp=1&_nc_ht=instagram.fhel6-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=w6z9v4MwYg8AX9FdWk0&edm=AP_V10EBAAAA&ccb=7-4&oh=99295fa82472bf4a425fc49bd03c1310&oe=60C40AFC&_nc_sid=4f375e', scheme='https', host='instagram.fhel6-1.fna.fbcdn.net', tld='net', host_type='domain', path='/v/t51.2885-15/e35/186524178_143770224434390_4909324648747352588_n.jpg', query='tp=1&_nc_ht=instagram.fhel6-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=w6z9v4MwYg8AX9FdWk0&edm=AP_V10EBAAAA&ccb=7-4&oh=99295fa82472bf4a425fc49bd03c1310&oe=60C40AFC&_nc_sid=4f375e'),
            'media_type': 1
        },
        {
            'pk': 2574205301066842492,
            'video_url': None,
            'thumbnail_url': HttpUrl('https://scontent-hel3-1.cdninstagram.com/v/t51.2885-15/e35/186787154_332065288355469_7843843424299639709_n.jpg?tp=1&_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_cat=109&_nc_ohc=-qZy9_HakCQAX-Cqk9v&edm=AP_V10EBAAAA&ccb=7-4&oh=031077ab2f56db0bab7ffbc920f80a41&oe=60C4F57B&_nc_sid=4f375e', scheme='https', host='scontent-hel3-1.cdninstagram.com', tld='com', host_type='domain', path='/v/t51.2885-15/e35/186787154_332065288355469_7843843424299639709_n.jpg', query='tp=1&_nc_ht=scontent-hel3-1.cdninstagram.com&_nc_cat=109&_nc_ohc=-qZy9_HakCQAX-Cqk9v&edm=AP_V10EBAAAA&ccb=7-4&oh=031077ab2f56db0bab7ffbc920f80a41&oe=60C4F57B&_nc_sid=4f375e'),
            'media_type': 1
        },
        {
            'pk': 2574205301075310332,
            'video_url': None,
            'thumbnail_url': HttpUrl('https://instagram.fhel3-1.fna.fbcdn.net/v/t51.2885-15/e35/185727252_524026898594344_9165723485744355754_n.jpg?tp=1&_nc_ht=instagram.fhel3-1.fna.fbcdn.net&_nc_cat=104&_nc_ohc=45NguRpEtZQAX83VSGE&edm=AP_V10EBAAAA&ccb=7-4&oh=c8c087ecfba444d9d85f7bd059f42a2a&oe=60C5C3C2&_nc_sid=4f375e', scheme='https', host='instagram.fhel3-1.fna.fbcdn.net', tld='net', host_type='domain', path='/v/t51.2885-15/e35/185727252_524026898594344_9165723485744355754_n.jpg', query='tp=1&_nc_ht=instagram.fhel3-1.fna.fbcdn.net&_nc_cat=104&_nc_ohc=45NguRpEtZQAX83VSGE&edm=AP_V10EBAAAA&ccb=7-4&oh=c8c087ecfba444d9d85f7bd059f42a2a&oe=60C5C3C2&_nc_sid=4f375e'),
            'media_type': 1
        }
    ]
}
```
