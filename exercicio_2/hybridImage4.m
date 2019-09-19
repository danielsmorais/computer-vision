% H: hybrid image; I1: image 1; I2: image 2; G1: low-pass filter; (1?G2): high-pass filter
%H = I1*G1 + I2*(1-G2)

% Leitura da imagem original
Img1 = im2double(rgb2gray(imread('baby2.jpg')));
Img2 = im2double(rgb2gray(imread('polarbear.jpg')));
[m,n] = size(Img1);

I1 = fftshift(fft2(Img1));
I2 = fftshift(fft2(Img2));

% Criacao da matriz para armazenar a imagem filtrada
H1 = zeros(m,n);
H2 = zeros(m,n);

% Filtro
frequency = 25;
for u = 1:m
     for v = 1:n
         D = sqrt((u-m/2)^2 + (v-n/2)^2);
         if D > frequency
             G1 = 1;
             G2 = 0;
         else
             G1 = 0;
             G2 = 1;
         end
         H1(u,v) = G1*I1(u,v); 
         H2(u,v) = G2*I2(u,v);
     end
end

aux1 = real(ifft2(ifftshift(H1)));
aux2 = real(ifft2(ifftshift(H2)));

H = aux1 + aux2;

% Exibição imagem filtrada
figure(1)
imshow(H);
axis tight
imwrite(H,'ImgFiltrada.png');