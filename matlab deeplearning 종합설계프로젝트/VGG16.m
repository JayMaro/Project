%%
net = vgg16() ;

%analyzeNetwork(net);
%%
imds = imageDatastore('Data\train',...
    'IncludeSubfolders',true,...
    'LabelSource','foldernames');
%%
[imdsTrain,imdsValidation] = splitEachLabel(imds,0.8,'randomized')

%%
inputSize = net.Layers(1).InputSize

layersTransfer = net.Layers(1:end-3);

numClasses = numel(categories(imdsTrain.Labels))
%%
layers = [
    layersTransfer
    fullyConnectedLayer(numClasses,'WeightLearnRateFactor',20,'BiasLearnRateFactor',20)
    softmaxLayer
    classificationLayer];
analyzeNetwork(layers);
%%
pixelRange = [-30 30];
imageAugmenter = imageDataAugmenter('RandXReflection',true,'RandXTranslation',pixelRange,'RandYTranslation',pixelRange);

augimdsTrain = augmentedImageDatastore(inputSize(1:2), imdsTrain,'DataAugmentation',imageAugmenter,'ColorPreprocessing','gray2rgb');
augimdsValidation = augmentedImageDatastore(inputSize(1:2), imdsValidation,'DataAugmentation',imageAugmenter,'ColorPreprocessing','gray2rgb');
%%
options = trainingOptions('sgdm',...
    'MiniBatchSize',128,...
    'MaxEpochs',20,...
    'InitialLearnRate',1e-4,...
    'Shuffle','every-epoch',...
    'ValidationData',augimdsValidation,...
    'ValidationFrequency',3,...
    'Verbose',false,...
    'Plots','training-progress',...
    'ExecutionEnvironment','cpu');

netTransfer = trainNetwork(augimdsTrain,layers,options);
%%
filename = 'vgg_test20.onnx';
exportONNXNetwork(netTransfer,filename)


%%
imdsTest = imageDatastore('Data\test',...
    'IncludeSubfolders',true,...
    'LabelSource','foldernames');
augimdsTest = augmentedImageDatastore(inputSize(1:2), imdsTest,'ColorPreprocessing','gray2rgb');
%%
[Ypred,scores] = classify(netTransfer,augimdsTest,'ExecutionEnvironment','cpu');
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