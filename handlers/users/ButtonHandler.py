
import logging
from aiogram import types


from loader import dp

from keyboards.inline.ShowMoreKeyboard import generate_button
from keyboards.inline.callback_data import show_callback

from utils.ImageSearch import ImageSearch


@dp.callback_query_handler(show_callback.filter())
async def buy_courses(call: types.CallbackQuery, callback_data: dict):
    index = int(callback_data["index"])
    name = callback_data["item_name"]

    pics = await ImageSearch(name, index)

    if len(pics) > 1:
        album = types.MediaGroup()
        for i in pics:
            album.attach_photo(photo=i)
        await call.message.answer_media_group(media=album)
        
        button = await generate_button(name, index+1)
        await call.message.answer("Tap below button to show more pictures", reply_markup=button)
        await call.message.delete()
    else:
        await call.answer("No more Pictures", cache_time=60, show_alert=True)
    
    await call.message.delete()
    

