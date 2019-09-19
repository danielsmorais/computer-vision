%ATIVIDADE 2
%DANIEL MORAIS
%Implementar e gerar uma imagem híbrida conforme o artigo https://dl.acm.org/citation.cfm?id=1141919


% H: hybrid image; I1: image 1; I2: image 2; G1: low-pass filter; (1?G2): high-pass filter
%H = I1*G1 + I2*(1-G2)

% LEITURA DE IMAGEM
image1 = im2double(rgb2gray(imread('merkel.jpg')));
image2 = im2double(rgb2gray(imread('trump.jpg')));
[m,n] = size(image1);

% APLICA��O DA TRANSFORMADA DE FOURIER
I1 = fftshift(fft2(image1));           
I2 = fftshift(fft2(image2));        

% DEFINI��O DA IMAGEM FILTRADA
H1 = zeros(m,n);
H2 = zeros(m,n);

% FITRAGEM
D0 = 30;                                    % FREQU�NCIA DE CORTE
for u = 1:m
     for v = 1:n
         D = sqrt((u-m/2)^2+(v-n/2)^2);     % DIST�NCIA EUCLIDIANA        
         if D > D0
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

H1inv = real(ifft2(ifftshift(H1)));
H2inv = real(ifft2(ifftshift(H2)));

H = H1inv + H2inv;

figure(1)
imshow(H);
axis tight
imwrite(H,'imagemHibrida_30.jpg');