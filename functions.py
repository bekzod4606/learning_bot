from aiogram.types import Message

async def get_user_info(message: Message) -> None:
    user = await message.bot.get_chat(message.from_user.id)
    user_photo = await message.bot.get_user_profile_photos(message.from_user.id)
    matn = (
        f"{message.from_user.mention_html('User Info:')} \n"
        f"USER ID: {message.from_user.id}\n"
    )
    if user.bio: matn += f"Bio: {user.bio}\n"
    if user.username: matn += f"Username: @{user.username}"
    if user_photo.photos:
        await message.answer_photo(user_photo.photos[0][-1].file_id, caption=matn, parse_mode="HTML")
    else:
        await message.answer(matn, parse_mode="HTML")
