class script(object):
    START_TXT = """👋 Hello {},

I can give any Movie or TV Series to auto filter method. 🥳

All you have to do is add me to a group and give me admin. 😌

I will take care of the rest. 😎"""

    FORCESUB_TXT = """👋 Hello {},

First join my updates channel, Then try again. 😇"""

    ABOUT_TXT = """★ My Name: <a href=https://t.me/{}>{}</a>
★ Creator: <a href=https://t.me/Hansaka_Anuhas>Hansaka Anuhas</a> 🇱🇰

★ Bot Server: <a href=https://railway.app>Railway</a>
★ Database: <a href=https://www.mongodb.com>MongoDB</a>"""

    MANUALFILTERS_TXT = """• /filter or /add - Add Filter
• /filters or /viewfilters - List All Filters
• /del - Delete Filter
• /delall - Delete All Filters"""

    BUTTONS_TXT = """<b>URL Buttons:</b>
<code>[Button Text](buttonurl:https://t.me/{})</code>

<b>Alert Buttons:</b>
<code>[Button Text](buttonalert:Alert Message)</code>"""

    AUTOFILTERS_TXT = """Your Movies and TV Series give me:

1. If you have a Movies or TV Series channel, Add me to it and give me admin.
2. Forward me a message you like on your channel.
3. I will take care of the rest."""

    CONNECTIONS_TXT = """• /connect - Connect PM
• /disconnect - Disconnect PM
• /connections - List All Connections"""

    EXTRAMODS_TXT = """• /id - User ID
• /info - User Informations
• /imdb or /search - IMDb Search
• /status - Bot Database Status
• /settings - Change Group Settings
• /set_template - Set IMDb Template
• /link - Create Link One Post
• /batch - Create Link Multiple Posts"""

    OWNERMODS_TXT = """• /users - List All Users
• /chats - List All Groups
• /ban - Ban User
• /unban - Unban User
• /leave - Leave Group
• /disable - Disable Group
• /enable - Re-enable Group
• /invite_link - Generate Group Link
• /users_broadcast - Broadcast Message All Users
• /groups_broadcast - Broadcast Message All Groups"""

    BOTSTATUS_TXT = """★ Total Files: <code>{}</code>
★ Total Users: <code>{}</code>
★ Total Groups: <code>{}</code>
★ Used Storage: <code>{}</code>
★ Free Storage: <code>{}</code>"""

    LOG_TEXT_G = """#NewGroup
Title: {}
ID: <code>{}</code>
Total Members: {}
Added by: {}"""

    LOG_TEXT_P = """#NewUser
Name: {}
ID: <code>{}</code>"""
    
    NO_RESULT = """#NoResult
Group Name: {}
Group ID: <code>{}</code>
Name: {}
Message: {}"""
