from aiogram import types

from loader import dp

from utils.ImageSearch import ImageSearch
from keyboards.inline.ShowMoreKeyboard import generate_button

# Image search
@dp.message_handler(state=None)
async def Image_Search_Handler(message: types.Message):
    
    item = message.text
    
    pictures = await ImageSearch(item, 0)
    
    if len(pictures) > 1:
        album = types.MediaGroup()
        for i in pictures:
            album.attach_photo(photo=i)
        await message.answer_media_group(media=album)
        button = await generate_button(item, 1)
        await message.answer("Tap below button to show more pictures", reply_markup=button)
        
    else:
        await message.reply("Not FOUND")

