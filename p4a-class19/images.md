```python
from io import BytesIO
url = 'http://animals.sandiegozoo.org/sites/default/files/juicebox_slides/parma_wallaby_01.jpg'
img_response = requests.get('http://some.domain.foo/image.jpg')
img = Image.open(BytesIO(img_response.content))
img.show()
```

```python
image_binary = BytesIO()
img.save(image_binary, 'PNG')
image_binary.seek(0)
response = send_file(image_binary, mimetype='image/png')
return response
```

