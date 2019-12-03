%ATIVIDADE 3
%DANIEL MORAIS
%Retirar ruídos nas imagens

% ELIMINAR RUIDO GAUSSIANO
% image = imread('ibirapuera/ruidoGaussiano.jpg');
% [linha, coluna] = size(image);
% fmedia = ones(3,3)*(1/9);
% imagemedia = zeros(linha,coluna);
% imagemedia = imfilter(image, fmedia);
% imwrite(imagemedia,'semruidoGaussiano.jpg');

% ELIMINAR RUIDO SAL E PIMENTA
% image = imread('ibirapuera/ruidoSalPimenta.jpg');
% [linha, coluna] = size(image);
% imagemediana = zeros(linha,coluna,'uint8');
% vv = zeros(9,1);
% for i=2:linha-1
%     for j=2:coluna-1
%         vv(1,1) = image(i - 1, j - 1);
%         vv(2,1) = image(i - 1, j);        
%         vv(3,1) = image(i - 1, j + 1);
%         vv(4,1) = image(i, j - 1);
%         vv(5,1) = image(i, j);
%         vv(6,1) = image(i, j + 1);
%         vv(7,1) = image(i + 1, j - 1);
%         vv(8,1) = image(i + 1, j);
%         vv(9,1) = image(i + 1, j + 1);
%         
%         imagemediana(i,j) = median(vv);
%     end
% end
% 
% imwrite(imagemediana,'semruidoSalPimenta.jpg');

% ELIMINAR RUIDO GAUSSIANO E SAL E PIMENTA
% image = imread('ibirapuera/ruidoGaussianoSalPimenta.jpg');
% [linha, coluna] = size(image);
% 
% imagemedian = zeros(linha,coluna,'uint8');
% vv = zeros(9,1);
% for i=2:linha-1
%     for j=2:coluna-1
%         vv(1,1) = image(i - 1, j - 1);
%         vv(2,1) = image(i - 1, j);        
%         vv(3,1) = image(i - 1, j + 1);
%         vv(4,1) = image(i, j - 1);
%         vv(5,1) = image(i, j);
%         vv(6,1) = image(i, j + 1);
%         vv(7,1) = image(i + 1, j - 1);
%         vv(8,1) = image(i + 1, j);
%         vv(9,1) = image(i + 1, j + 1);
%         
%         imagemedian(i,j) = median(vv);
%     end
% end
% 
% fmedia = ones(3,3)*(1/9);
% imagefinal = zeros(linha,coluna);
% imagefinal = imfilter(imagemedian, fmedia);
% imwrite(imagefinal,'semruidoGaussianoSalPimenta.jpg');


% ELIMINAR RUIDO SAL

image = imread('ibirapuera/ruidoSal.jpg');
[linha, coluna] = size(image);

imagesal = zeros(linha,coluna,'uint8');
vv = zeros(9,1);
for i=2:linha-1
    for j=2:coluna-1
        vv(1,1) = image(i - 1, j - 1);
        vv(2,1) = image(i - 1, j);        
        vv(3,1) = image(i - 1, j + 1);
        vv(4,1) = image(i, j - 1);
        vv(5,1) = image(i, j);
        vv(6,1) = image(i, j + 1);
        vv(7,1) = image(i + 1, j - 1);
        vv(8,1) = image(i + 1, j);
        vv(9,1) = image(i + 1, j + 1);
        
        imagesal(i,j) = min(vv);
    end
end
imwrite(imagesal,'semruidoSal.jpg');


% ELIMINAR RUIDO PIMENTA

image = imread('ibirapuera/ruidoPimenta.jpg');
[linha, coluna] = size(image);

imagepimenta = zeros(linha,coluna,'uint8');
vv = zeros(9,1);
for i=2:linha-1
    for j=2:coluna-1
        vv(1,1) = image(i - 1, j - 1);
        vv(2,1) = image(i - 1, j);        
        vv(3,1) = image(i - 1, j + 1);
        vv(4,1) = image(i, j - 1);
        vv(5,1) = image(i, j);
        vv(6,1) = image(i, j + 1);
        vv(7,1) = image(i + 1, j - 1);
        vv(8,1) = image(i + 1, j);
        vv(9,1) = image(i + 1, j + 1);
        
        imagepimenta(i,j) = max(vv);
    end
end
imwrite(imagepimenta,'semruidoPimenta.jpg');





figure(1);
imshow(imagepimenta);