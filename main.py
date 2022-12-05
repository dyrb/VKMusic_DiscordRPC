import vk_api
from pypresence import Presence
import time

# VK API TOKEN  https://vkhost.github.io/  https://vk.com/editapp?act=create
vk = vk_api.VkApi(token="")
# Discord APPLICATION ID
id = ""
rpc = Presence(id)
rpc.connect()


while True:
    status = vk.method("status.get")
    audio = status['audio']
    artist = audio['artist']
    song = audio['title']

    rpc.update(
        state=f"{song}",
        details=f"{artist}",
        large_image="sdksk",
        large_text="Слушает VK Музыку"
    )

    time.sleep(15)
