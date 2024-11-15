from roboflow import Roboflow
rf = Roboflow(api_key="r7qSIBlL0ryPm5qonSPH")
project = rf.workspace("school-95f9t").project("human-detection-uerkn")
version = project.version(3)
dataset = version.download("yolov11")
                