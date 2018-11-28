def img(url, filename):
    
    from PIL import Image
    import requests
    import shutil
   

    response = requests.get(url, stream = True)

    with open(filename, 'wb') as file:
        shutil.copyfileobj(response.raw, file)

    del response

    img = Image.open(filename)
    img.show()
    
    

