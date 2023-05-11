import instaloader
from PIL import Image

ig=instaloader.Instaloader()
dp=input("Введите id")
ig.download_profile(dp, profile_pic_only=True)
dp=str(dp)

img=Image.open(r'C:\Users\Nasta\PycharmProjects\pythonProject3')
img.show()