pip install git+https://github.com/ageitgey/face_recognition.git
import face_recognition
from PIL import Image, ImageDraw

def face_rec():
  vit_face_img = face_recognition.load_image_file("img\faces\Andreev_Vitaliy.jpg")
  vit_face_location = face_recognition.face_locations(vit_face_img)

  pil_img1 = Image.from_array(vit_face_img)
  draw1 = ImageDraw.Draw(pil_img1)

  for (top, right, bottom, left) in vit_face_location:
    draw1.rectangle(((left, top),(right, bottom)), outline=(240, 128, 128), width=4)
  
  del draw1
  pil_img1.save("img\faces\new_Vit.jpg")

  from face_recognition.api import face_locations
def extracing_faces(img_path):
  count = 0
  faces = face_recognition.load_image_file(img_path)
  faces_location = face_recognition.face_location(faces)

  for face_location in face_locations:
    top, right, bottom, left = face_location

    face_img = faces[top:bottom, left:right]
    pil_img = Image.fromarray(face_img)
    count += 1
  
  return f"Found {count} face(s) in this photo"

  def main():
    print(extracting_faces("img\faces\Andreev_Vitaliy.jpg"))