def save_picture(picture) -> str:
    filename = picture.filename
    path = f'./upload/{filename}'
    picture.save(path)
    return path
