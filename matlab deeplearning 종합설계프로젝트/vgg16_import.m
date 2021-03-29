modelfile = 'vgg_test20.onnx';
classes = ["COVID19" "NORMAL" "PNEUMONIA"];
net = importONNXNetwork(modelfile,'OutputLayerType','classification','Classes',classes);

analyzeNetwork(net);
%%
imdsTest = imageDatastore('Data\test',...
    'IncludeSubfolders',true,...
    'LabelSource','foldernames');
augimdsTest = augmentedImageDatastore(inputSize(1:2), imdsTest,'ColorPreprocessing','gray2rgb');
%%
[Ypred,scores] = classify(net,augimdsTest,'ExecutionEnvironment','cpu');
%%
flag = 0;
Number = numel(Ypred)
for i = 1:Number
    if imdsTest.Labels(i) == Ypred(i)
    flag = flag+1;
    end
end
%%
flag/Number*100