# Scene Detection


### Usage

```
from scene_detection import SceneDetector

model = SceneDetector()
print(model.predict_from_path('test.jpg'))
```

### Reference
Link: [Places2 Database](http://places2.csail.mit.edu), [Places1 Database](http://places.csail.mit.edu)

Please cite the following [IEEE Transaction on Pattern Analysis and Machine Intelligence paper](http://places2.csail.mit.edu/PAMI_places.pdf) if you use the data or pre-trained CNN models.

```
 @article{zhou2017places,
   title={Places: A 10 million Image Database for Scene Recognition},
   author={Zhou, Bolei and Lapedriza, Agata and Khosla, Aditya and Oliva, Aude and Torralba, Antonio},
   journal={IEEE Transactions on Pattern Analysis and Machine Intelligence},
   year={2017},
   publisher={IEEE}
 }

```
