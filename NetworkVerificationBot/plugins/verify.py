from NetworkVerificationBot import app, VERIFICATION_CHANNEL_ID,START_IMG,TOS_LINK
from pyrogram import filters ,enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup,CallbackQuery 
    
VERIFY_MSG="""
ʜᴇʏ **{}** ɪɴ ᴏʀᴅᴇʀ ᴛᴏ ᴠᴇʀɪғʏ ʏᴏᴜʀsᴇʟғ , ᴀʀᴇ ʏᴏᴜ ᴀᴄᴄᴇᴘᴛɪɴɢ ᴏᴜʀ [ᴛᴇʀᴍs ᴀɴᴅ ᴄᴏɴᴅɪᴛɪᴏɴs]({}) (TOS) ?
ɪғ ʏᴇs ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʏᴇs,ɪ ᴀᴄᴄᴇᴘᴛ ʙᴜᴛᴛᴏɴ ᴇʟsᴇ ɴᴏ,ɪ ᴅᴇᴄʟɪɴᴇ.
"""
VERIFY_BUTTONS= [
         [
           InlineKeyboardButton (text="ʏᴇs , ɪ ᴀᴄᴄᴇᴘᴛ",callback_data="yes_verify")
         ],
         [
          InlineKeyboardButton (text="ɴᴏ, ɪ ᴅᴇᴄʟɪɴᴇ",callback_data="no_verify")        
         ],
      ]

VERIFY_BUTTON= [
         [
           InlineKeyboardButton (text="approved",callback_data="yes_approved")
         ],
         [
          InlineKeyboardButton (text="unapproved",callback_data="no_approved")        
         ],
      ]


@app.on_message(filters.command("verify"))
async def verify(_,msg):
    await msg.reply_text(VERIFY_MSG.format(msg.from_user.first_name,TOS_LINK),
      reply_markup=InlineKeyboardMarkup(VERIFY_BUTTONS)
      )

@app.on_callback_query(filters.regex("yes_verify"))
async def yos(_, CallbackQuery):
    query = CallbackQuery.message
    await query.edit_text("""
    ᴜsᴇ /continue ᴛᴏ ᴘʀᴏᴄᴇᴇᴅ
ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ɪᴛ, ᴡʜᴇɴ ʏᴏᴜʀ ғᴏʀ ᴡɪʟʟ ʙᴇ ғɪʟʟᴇᴅ ɪ ᴡɪʟʟ ᴅɪʀᴇᴄᴛʟʏ sᴇɴᴅ ɪᴛ ɪɴ ᴍʏ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴄʜᴀɴɴᴇʟ.
    """)
        
      
@app.on_callback_query(filters.regex("no_verify"))
async def nope(_, CallbackQuery):
    query=CallbackQuery.message
    await query.edit_text("ɪᴛs sᴏ sᴀᴅ ғᴏʀ ᴏᴜʀ ɴᴇᴛᴡᴏʀᴛ ᴛᴏ ɴᴏʏ ʜᴀᴠᴇ ᴀ ᴅɪᴀᴍᴏɴᴅ ʟɪᴋᴇ ʏᴏᴜ.ʙᴜᴛ ɪғ ᴇᴠᴇʀ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ᴍɪɴᴅ ᴛʜᴇɴ ʟᴇᴍᴍᴇ ᴋɴᴏᴡ.")
  

@app.on_message(filters.command("continue"))
async def verify(client,msg):
    id=msg.chat.id   
    first_name = msg.from_user.first_name
    username = msg.from_user.username
    user_id = msg.from_user.id
    dc_id = msg.from_user.dc_id            
    full_name = await client.ask(id,"ᴡʜᴀᴛ ɪs ʏᴏᴜʀ ғᴜʟʟ ɴᴀᴍᴇ ?")
    age = await client.ask(id,"ʜᴏᴡ ᴏʟᴅ ᴀʀᴇ ʏᴏᴜ ?")
    gender = await client.ask(id,"ᴡʜᴀᴛ's ʏᴏᴜʀ ɢᴇɴᴅᴇʀ ?")
    channels = await client.ask(id,"ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴜsᴇʀɴᴀᴍᴇs")
    groups = await client.ask(id,"ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇs")
    bots = await client.ask(id,"ʏᴏᴜʀ ʙᴏᴛ ᴜsᴇʀɴᴀᴍᴇs")
    country = await client.ask(id,"ғʀᴏᴍ ᴡʜɪᴄʜ ᴄᴏᴜɴᴛʀʏ ʏᴏᴜ ʙᴇʟᴏɴɢ ᴛᴏ ?")
    skills = await client.ask(id,"ʜᴀᴠᴇ ᴀɴʏ sᴋɪʟʟ ?")
    github = await client.ask(id,"ʜᴀᴠᴇ ɢɪᴛʜᴜʙ ᴀᴄᴄᴏᴜᴛ..?\nɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ʟɪɴᴋ")
    about = await client.ask(id,"ᴛᴇʟʟ ᴍᴇ sᴏᴍᴇᴛʜɪɴɢ ᴀʙᴏᴜᴛ ʏᴏᴜʀsᴇʟғ.")
    tag = await client.ask(id,"ᴄᴀɴ ʏᴏᴜ ᴘᴜᴛ ᴏᴜʀ ɴᴇᴛᴡᴏʀᴋ ᴛᴀɢ ᴏɴ ʏᴏᴜʀ ɴᴀᴍᴇ ?")
    reason = await client.ask(id,"ʜᴀᴠᴇ ᴀɴʏ  ʀᴇᴀsᴏɴ ᴛᴏ ᴊᴏɪɴɪɴɢ ᴏᴜʀ ɴᴇᴛᴡᴏʀᴋ, ɪғ ʜᴀᴠᴇ ᴛʜᴇɴ ᴡʀɪᴛᴇ ɪᴛ ᴅᴏᴡɴ.")    
    await app.send_message(VERIFICATION_CHANNEL_ID,
    f"""
 ❍═❰ 𝚅𝙴𝚁𝙸𝙵𝙸𝙲𝙰𝚃𝙸𝙾𝙽 𝙵𝙾𝚁𝙼 ❱═❍
◎ ─━──━─❖─━──━─ ◎
➻ **ғɪʀsᴛ ɴᴀᴍᴇ :** `{first_name}`
➻ **ᴜsᴇʀɴᴀᴍᴇ :** @{username}
➻ **ᴜsᴇʀ ɪᴅ :** `{user_id}`
➻ **ᴅᴄ ɪᴅ :** `{dc_id}`   
◎ ─━──━─❖─━──━─ ◎
➻ **ғᴜʟʟ ɴᴀᴍᴇ :** `{full_name.text}`
➻ **ᴀɢᴇ :** `{age.text}`
➻ **ɢᴇɴᴅᴇʀ :** `{gender.text}`
➻ **ᴄʜᴀɴɴᴇʟs :** {channels.text}
➻ **ɢʀᴏᴜᴘs :** {groups.text}
➻ **ʙᴏᴛs :** {bots.text}
➻ **ᴄᴏᴜɴᴛʀʏ** : `{country.text}`
◎ ─━──━─❖─━──━─ ◎
➻ **sᴋɪʟʟs :** `{skills.text}`
➻ **ɢɪᴛʜᴜʙ ʟɪɴᴋ :** {github.text}
➻ **ᴀʙᴏᴜᴛ :** `{about.text}`
➻ **ᴄᴀɴ ᴘᴜᴛ ɴᴇᴛᴡᴏʀᴋ's ᴛᴀɢ :** `{tag.text}`
➻ **ʀᴇᴀsᴏɴ :** `{reason.text}`
◎ ─━──━─❖─━──━─ ◎
""",
      reply_markup=InlineKeyboardMarkup (VERIFY_BUTTON)
     )
    await msg.reply_text("""
    sᴜᴄᴄᴇssғᴜʟʟʏ ʏᴏᴜʀ ғᴏʀᴍ sᴜʙᴍɪᴛᴛᴇᴅ ᴛᴏ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴄʜᴀɴɴᴇʟ. ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ғᴏʀ sᴏᴍᴇᴛɪᴍᴇ ᴛᴏ ɢᴇᴛ ᴏғғɪᴄɪᴀʟʏ ᴠᴇʀɪғɪᴇᴅ.
ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ.
     """)
    
@app.on_callback_query(filters.regex("yes_approved")
async def _aproved(bot:app,callback_query:CallbackQuery):
    admins=[]
    for m in bot.get_chat_members(
         VERIFICATION_CHANNEL_ID,filter=enums.ChatMembers.ADMINISTRATORS):
        admins.append(m.user.id)
    if callback_query.from_user.id in admins:
        callback_query.message.edit_text("hii")
    else:
        pass


 
