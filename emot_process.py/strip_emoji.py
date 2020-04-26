import re

def strip_emoji(text):
    RE_EMOJI = re.compile(u'(\u00a9|\u00ae|[\u2000-\u3300]|\ud83c[\ud000-\udfff]|\ud83d[\ud000-\udfff]|\ud83e[\ud000-\udfff])')
    return RE_EMOJI.sub(r'', text)


print(strip_emoji('🙄🤔'))