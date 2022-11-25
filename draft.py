import requests

response = requests.get(f'https://random-d.uk/api/random')
a = response.json()
img = requests.get(a['url'])

with open ('new_image.jpg', 'wb') as f:
    f.write(img.content)

# img = requests.get(
#     'https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Rubber_Duck_%288374802487%29.jpg/640px-Rubber_Duck_%288374802487%29.jpg')
# out = open("new_image.jpg", "wb")
# out.write(img.content)
# out.close()
# print(type(img))
# bla bla bla