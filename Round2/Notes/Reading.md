1) In paper [Recognizing Image Style](https://sergeykarayev.com/files/1311.3715v3.pdf) by Berkeley UC and Adobe they claims that 
ImageNet performs better on representing styles of images than other hand-extracted features such as colors histogram. It seems that we
should just use the VGG net in Keras and not train any other models with similar topology.

2) It would be interesting to have a model looks like the one in https://devblogs.nvidia.com/parallelforall/understanding-aesthetics-deep-learning/. The authors claim that their model with a triplet hinge loss function "works well" with just 100,000 images in training set, although no performance details is provided. 
