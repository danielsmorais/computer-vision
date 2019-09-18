%ATIVIDADE 3
%DANIEL MORAIS
%Verificar ruídos nas imagens

image = imread('cristoRedentor/cristo.jpg');
[linha, coluna] = size(image);
h = zeros(256,1);

for i=1:linha
    for j=1:coluna
        aux = image(i,j);
        h(aux+1) = h(aux+1) + 1;
    end
end

bar(0:255,h); %plot do histograma
%set(gcf, 'Position', [0, 255, 0, max(h)]);

set(gca,'xtick',0:255)
set(gca,'ytick',0:max(h))