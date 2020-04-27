from scene_detection import SceneDetector

model = SceneDetector()
print(model.predict_from_path('../places365bak/test.jpg'))