""" Documentation later """
from models.engine.file_storage import FileStorage



storage = FileStorage()
classes = {"BaseModel", "User", "State", "City", "Amenity", "Place", "Review"}
storage.reload()
